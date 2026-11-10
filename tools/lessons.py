#!/usr/bin/env python3
"""Herramientas del repositorio de lecciones de inglés con énfasis en speaking.

Subcomandos:
  validate   Valida currículo y lecciones (estructura, metadatos, tiempo de habla, códigos L1).
  index      Genera lessons/INDEX.md a partir del currículo y las lecciones (--check para CI).
  new        Crea una lección nueva desde templates/lesson-template.md.

Ejemplos:
  python tools/lessons.py validate
  python tools/lessons.py index
  python tools/lessons.py index --check
  python tools/lessons.py new --track GEN --level A1 --unit 2 --lesson 1 \\
      --slug my-family --title "This is my family" --author "Nombre Apellido"

Requiere Python 3.10+ y PyYAML (pip install -r requirements.txt).
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]

# --- Políticas del repositorio (documentadas en docs/02-estructura-de-leccion.md) ---------------
MIN_SPEAKING_RATIO = 0.60  # tiempo planificado de habla del estudiante / duración total
MIN_L1_FOCUS, MAX_L1_FOCUS = 3, 7

LEVELS = ("A1", "A2", "B1", "B2", "C1")
VARIETIES = ("en-US", "en-GB")
STATUSES = ("draft", "review", "published")
STATUS_LABELS = {"draft": "borrador", "review": "en revisión", "published": "publicada"}

# Ciclo de enseñanza del speaking (adaptado de Goh y Burns, 2012). Todas las etapas son obligatorias.
STAGE_TYPES = (
    "warm_up",
    "input",
    "task_1",
    "language_focus",
    "pronunciation",
    "task_2",
    "feedback",
)

REQUIRED_SECTIONS = (
    "Objetivos (can-do)",
    "Lenguaje clave",
    "Foco L1 para hispanohablantes",
    "Secuencia de la clase",
    "Evaluación del speaking",
    "Práctica autónoma",
    "Práctica con IA (role-play)",
    "Notas para el facilitador",
)

REQUIRED_KEYS: dict[str, Any] = {
    "id": str,
    "title": str,
    "track": str,
    "level": str,
    "unit": int,
    "lesson": int,
    "duration_min": int,
    "variety": str,
    "status": str,
    "version": str,
    "last_reviewed": (dt.date, str),
    "authors": list,
    "can_do": list,
    "speaking_functions": list,
    "grammar": list,
    "vocabulary": list,
    "l1_focus": list,
    "stages": list,
}
OPTIONAL_KEYS: dict[str, Any] = {
    "reviewers": list,
    "ai_assisted": bool,
    "tags": list,
    "prerequisites": list,
    "materials": list,
}

ID_RE = re.compile(r"^(?P<track>[A-Z]{3})-(?P<level>A1|A2|B1|B2|C1)-U(?P<unit>\d{2})-L(?P<lesson>\d{2})$")
CODE_RE = re.compile(r"^(PRON|GRAM|VOC|PRAG)-\d{2}$")
CATALOG_ROW_RE = re.compile(r"^\|\s*((?:PRON|GRAM|VOC|PRAG)-\d{2})\s*\|\s*([^|]+?)\s*\|", re.M)
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FOLDER_RE = re.compile(r"^u(?P<unit>\d{2})-l(?P<lesson>\d{2})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)$")

INDEX_HEADER = "<!-- Archivo generado por `python tools/lessons.py index`. No lo edites a mano. -->"


# --- Contexto del repositorio -----------------------------------------------------------------


@dataclass
class Repo:
    root: Path
    catalog: dict[str, str]  # código → fenómeno
    syllabus: dict[str, Any]

    @property
    def lessons_dir(self) -> Path:
        return self.root / "lessons"

    def track(self, code: str) -> dict[str, Any] | None:
        return (self.syllabus.get("tracks") or {}).get(code)

    def unit(self, track: str, level: str, unit: int) -> dict[str, Any] | None:
        t = self.track(track)
        if not t:
            return None
        lvl = (t.get("levels") or {}).get(level)
        if not lvl:
            return None
        for u in lvl.get("units") or []:
            if u.get("unit") == unit:
                return u
        return None


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def load_catalog(path: Path) -> tuple[dict[str, str], list[str]]:
    """Lee los códigos de las tablas del catálogo. Devuelve (catálogo, errores)."""
    catalog: dict[str, str] = {}
    errors: list[str] = []
    for code, phenomenon in CATALOG_ROW_RE.findall(read_text(path)):
        if code in catalog:
            errors.append(f"{path.name}: código duplicado en el catálogo: {code}")
        catalog[code] = phenomenon.strip()
    if not catalog:
        errors.append(f"{path.name}: no se encontraron códigos en el catálogo")
    return catalog, errors


def load_repo(root: Path = ROOT) -> tuple[Repo, list[str]]:
    catalog, errors = load_catalog(root / "docs" / "01-interferencias-l1.md")
    syllabus = yaml.safe_load(read_text(root / "curriculum" / "syllabus.yml")) or {}
    return Repo(root=root, catalog=catalog, syllabus=syllabus), errors


# --- Validación del currículo ------------------------------------------------------------------


def validate_syllabus(repo: Repo) -> list[str]:
    errors: list[str] = []
    where = "curriculum/syllabus.yml"
    tracks = repo.syllabus.get("tracks")
    if not isinstance(tracks, dict) or not tracks:
        return [f"{where}: falta el mapa 'tracks'"]
    slugs: set[str] = set()
    for code, track in tracks.items():
        if not re.fullmatch(r"[A-Z]{3}", str(code)):
            errors.append(f"{where}: código de track inválido '{code}' (3 letras mayúsculas)")
        slug = track.get("slug", "")
        if not SLUG_RE.match(str(slug)):
            errors.append(f"{where}: track {code}: slug inválido '{slug}'")
        if slug in slugs:
            errors.append(f"{where}: slug de track duplicado '{slug}'")
        slugs.add(slug)
        for key in ("name", "levels"):
            if not track.get(key):
                errors.append(f"{where}: track {code}: falta '{key}'")
        for level, lvl in (track.get("levels") or {}).items():
            if level not in LEVELS:
                errors.append(f"{where}: track {code}: nivel inválido '{level}'")
            seen: set[int] = set()
            for u in lvl.get("units") or []:
                n = u.get("unit")
                label = f"{code}-{level}-U{n}"
                if not isinstance(n, int) or isinstance(n, bool) or n < 1:
                    errors.append(f"{where}: {label}: 'unit' debe ser entero positivo")
                if n in seen:
                    errors.append(f"{where}: {label}: unidad duplicada")
                seen.add(n)
                for key in ("title", "speaking_goal", "l1_focus"):
                    if not u.get(key):
                        errors.append(f"{where}: {label}: falta '{key}'")
                for c in u.get("l1_focus") or []:
                    if c not in repo.catalog:
                        errors.append(f"{where}: {label}: código L1 desconocido '{c}'")
                if u.get("l1_focus") and not any(str(c).startswith("PRON-") for c in u["l1_focus"]):
                    errors.append(f"{where}: {label}: 'l1_focus' debe incluir al menos un código PRON-")
    return errors


# --- Validación de lecciones -------------------------------------------------------------------


def split_front_matter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("el archivo debe empezar con front matter YAML ('---')")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("front matter sin cierre ('---')")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError("el front matter debe ser un mapa YAML")
    return data, text[end + 5 :]


def headings(body: str) -> list[tuple[int, str]]:
    """Encabezados (nivel, texto) en orden, ignorando bloques de código."""
    found: list[tuple[int, str]] = []
    in_fence = False
    for line in body.split("\n"):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        m = re.match(r"^(#{1,6}) (.+?)\s*$", line)
        if not in_fence and m:
            found.append((len(m.group(1)), m.group(2)))
    return found


def h2_headings(body: str) -> list[str]:
    return [text for level, text in headings(body) if level == 2]


def stage_heading_minutes(body: str, section: str = "Secuencia de la clase") -> list[int]:
    """Minutos declarados en los H3 '### N. Etapa (M min)' dentro de la sección de secuencia."""
    minutes: list[int] = []
    inside = False
    for level, text in headings(body):
        if level == 2:
            inside = text == section
        elif inside and level == 3:
            m = re.search(r"\((\d+) min\)$", text)
            if m:
                minutes.append(int(m.group(1)))
    return minutes


def _type_ok(value: Any, expected: Any) -> bool:
    if expected is int:
        return isinstance(value, int) and not isinstance(value, bool)
    return isinstance(value, expected)


def _str_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value)


def validate_lesson(repo: Repo, rel_path: Path, text: str) -> list[str]:
    """Valida una lección. `rel_path` es relativo a lessons/ (p. ej. general/a1/u01-l01-x/lesson.md)."""
    where = f"lessons/{rel_path.as_posix()}"
    try:
        fm, body = split_front_matter(text)
    except (ValueError, yaml.YAMLError) as exc:
        return [f"{where}: {exc}"]

    errors: list[str] = []

    def err(msg: str) -> None:
        errors.append(f"{where}: {msg}")

    # Claves y tipos
    for key, expected in REQUIRED_KEYS.items():
        if key not in fm:
            err(f"falta la clave obligatoria '{key}'")
        elif not _type_ok(fm[key], expected):
            err(f"'{key}' tiene un tipo inválido")
    for key, expected in OPTIONAL_KEYS.items():
        if key in fm and not _type_ok(fm[key], expected):
            err(f"'{key}' tiene un tipo inválido")
    unknown = set(fm) - set(REQUIRED_KEYS) - set(OPTIONAL_KEYS)
    if unknown:
        err(f"claves desconocidas: {', '.join(sorted(unknown))}")
    if errors:
        return errors

    # Valores
    if fm["level"] not in LEVELS:
        err(f"nivel inválido '{fm['level']}' (use {', '.join(LEVELS)})")
    if fm["variety"] not in VARIETIES:
        err(f"variedad inválida '{fm['variety']}' (use {', '.join(VARIETIES)})")
    if fm["status"] not in STATUSES:
        err(f"estado inválido '{fm['status']}' (use {', '.join(STATUSES)})")
    if not SEMVER_RE.match(fm["version"]):
        err(f"versión inválida '{fm['version']}' (formato X.Y.Z)")
    if isinstance(fm["last_reviewed"], str):
        try:
            dt.date.fromisoformat(fm["last_reviewed"])
        except ValueError:
            err("'last_reviewed' debe ser una fecha ISO (AAAA-MM-DD)")
    if not fm["title"].strip():
        err("'title' está vacío")
    for key in ("authors", "can_do", "speaking_functions"):
        if not fm[key] or not _str_list(fm[key]):
            err(f"'{key}' debe ser una lista no vacía de textos")
    for key in ("grammar", "vocabulary"):
        if not _str_list(fm[key]):
            err(f"'{key}' debe ser una lista de textos")

    # Revisión por una segunda persona antes de publicar
    reviewers = fm.get("reviewers") or []
    if fm["status"] == "published":
        if not reviewers or not set(reviewers) - set(fm["authors"]):
            err("una lección 'published' requiere al menos un revisor distinto de los autores")
    if fm["status"] != "draft" and "TODO" in text:
        err(f"una lección en estado '{fm['status']}' no puede contener marcadores TODO")

    # Identificador, currículo y ruta
    m = ID_RE.match(fm["id"])
    if not m:
        err(f"id inválido '{fm['id']}' (formato TRK-NIVEL-Unn-Lnn, p. ej. GEN-A1-U01-L01)")
    else:
        expected = {
            "track": fm["track"],
            "level": fm["level"],
            "unit": f"{fm['unit']:02d}",
            "lesson": f"{fm['lesson']:02d}",
        }
        for part, value in expected.items():
            if m.group(part) != value:
                err(f"el id '{fm['id']}' no coincide con {part}={value}")

    track = repo.track(fm["track"])
    if not track:
        err(f"track '{fm['track']}' no existe en curriculum/syllabus.yml")
    elif not repo.unit(fm["track"], fm["level"], fm["unit"]):
        err(f"la unidad {fm['track']}-{fm['level']}-U{fm['unit']:02d} no existe en curriculum/syllabus.yml")

    parts = rel_path.parts
    if len(parts) != 4 or parts[-1] != "lesson.md":
        err("ruta inválida: use lessons/<track>/<nivel>/uNN-lNN-<slug>/lesson.md")
    else:
        track_dir, level_dir, folder, _ = parts
        if track and track_dir != track.get("slug"):
            err(f"carpeta de track '{track_dir}' debería ser '{track.get('slug')}'")
        if level_dir != fm["level"].lower():
            err(f"carpeta de nivel '{level_dir}' debería ser '{fm['level'].lower()}'")
        fm_folder = FOLDER_RE.match(folder)
        if not fm_folder:
            err(f"carpeta '{folder}' inválida (formato uNN-lNN-slug-en-minusculas)")
        elif (int(fm_folder["unit"]), int(fm_folder["lesson"])) != (fm["unit"], fm["lesson"]):
            err(f"carpeta '{folder}' no coincide con unit={fm['unit']} lesson={fm['lesson']}")

    # Foco L1
    codes = fm["l1_focus"]
    if not (MIN_L1_FOCUS <= len(codes) <= MAX_L1_FOCUS):
        err(f"'l1_focus' debe tener entre {MIN_L1_FOCUS} y {MAX_L1_FOCUS} códigos")
    if len(set(codes)) != len(codes):
        err("'l1_focus' tiene códigos repetidos")
    for c in codes:
        if not isinstance(c, str) or not CODE_RE.match(c):
            err(f"código L1 con formato inválido: {c!r}")
        elif c not in repo.catalog:
            err(f"código L1 '{c}' no existe en docs/01-interferencias-l1.md")
        elif c not in body:
            err(f"el código L1 '{c}' no se trabaja en el cuerpo de la lección")
    if not any(isinstance(c, str) and c.startswith("PRON-") for c in codes):
        err("'l1_focus' debe incluir al menos un código de pronunciación (PRON-)")

    # Etapas y tiempo de habla
    stages = fm["stages"]
    total = speaking = 0
    seen: list[str] = []
    for i, st in enumerate(stages, 1):
        if not isinstance(st, dict):
            err(f"etapa {i}: debe ser un mapa con type, minutes y learner_speaking")
            continue
        stype, mins, talk = st.get("type"), st.get("minutes"), st.get("learner_speaking")
        if set(st) - {"type", "minutes", "learner_speaking"}:
            err(f"etapa {i}: claves desconocidas {sorted(set(st) - {'type', 'minutes', 'learner_speaking'})}")
        if stype not in STAGE_TYPES:
            err(f"etapa {i}: tipo inválido '{stype}' (use {', '.join(STAGE_TYPES)})")
        elif stype in seen:
            err(f"etapa {i}: tipo repetido '{stype}'")
        else:
            seen.append(stype)
        if not _type_ok(mins, int) or mins <= 0:
            err(f"etapa {i}: 'minutes' debe ser entero positivo")
            continue
        if not _type_ok(talk, int) or not 0 <= talk <= mins:
            err(f"etapa {i}: 'learner_speaking' debe ser entero entre 0 y 'minutes'")
            continue
        total += mins
        speaking += talk
    missing = [s for s in STAGE_TYPES if s not in seen]
    if missing:
        err(f"faltan etapas obligatorias: {', '.join(missing)}")
    if "task_1" in seen and "task_2" in seen and seen.index("task_1") > seen.index("task_2"):
        err("'task_1' debe ir antes que 'task_2' (repetición de la tarea)")
    if total and total != fm["duration_min"]:
        err(f"la suma de minutos de las etapas ({total}) no coincide con duration_min ({fm['duration_min']})")
    if total:
        ratio = speaking / total
        if ratio < MIN_SPEAKING_RATIO:
            err(
                f"tiempo de habla del estudiante {ratio:.0%} < mínimo {MIN_SPEAKING_RATIO:.0%} "
                f"({speaking} de {total} min)"
            )

    # Los encabezados de etapa del cuerpo deben coincidir con los metadatos
    declared = [s.get("minutes") for s in stages if isinstance(s, dict)]
    in_body = stage_heading_minutes(body)
    if in_body != declared:
        err(
            "los encabezados '### N. Etapa (M min)' de 'Secuencia de la clase' no coinciden con 'stages' "
            f"(cuerpo: {in_body}, metadatos: {declared})"
        )

    # Secciones obligatorias, en orden
    found = h2_headings(body)
    positions = []
    for section in REQUIRED_SECTIONS:
        if section not in found:
            err(f"falta la sección obligatoria '## {section}'")
        else:
            positions.append(found.index(section))
    if positions != sorted(positions):
        err("las secciones obligatorias no están en el orden de la plantilla")

    return errors


def lesson_files(repo: Repo) -> list[Path]:
    return sorted(repo.lessons_dir.glob("**/lesson.md"))


def load_lessons(repo: Repo) -> list[tuple[Path, dict[str, Any]]]:
    out = []
    for path in lesson_files(repo):
        try:
            fm, _ = split_front_matter(read_text(path))
        except (ValueError, yaml.YAMLError):
            continue
        out.append((path, fm))
    return out


def validate_all(repo: Repo) -> tuple[list[str], int]:
    errors = validate_syllabus(repo)
    ids: dict[str, Path] = {}
    files = lesson_files(repo)
    for path in files:
        rel = path.relative_to(repo.lessons_dir)
        text = read_text(path)
        errors += validate_lesson(repo, rel, text)
        try:
            fm, _ = split_front_matter(text)
        except (ValueError, yaml.YAMLError):
            continue
        lid = fm.get("id")
        if lid in ids:
            errors.append(f"lessons/{rel.as_posix()}: id duplicado '{lid}' (también en {ids[lid]})")
        elif lid:
            ids[lid] = rel
    return errors, len(files)


# --- Índice ------------------------------------------------------------------------------------


def _speaking_ratio(fm: dict[str, Any]) -> str:
    try:
        total = sum(s["minutes"] for s in fm["stages"])
        talk = sum(s["learner_speaking"] for s in fm["stages"])
        return f"{talk / total:.0%}"
    except (KeyError, TypeError, ZeroDivisionError):
        return "—"


def build_index(repo: Repo) -> str:
    lessons = load_lessons(repo)
    by_unit: dict[tuple[str, str, int], list[tuple[Path, dict[str, Any]]]] = {}
    lessons = [(p, fm) for p, fm in lessons if isinstance(fm.get("lesson"), int) and isinstance(fm.get("title"), str)]
    for path, fm in lessons:
        by_unit.setdefault((fm.get("track"), fm.get("level"), fm.get("unit")), []).append((path, fm))

    counts = {s: 0 for s in STATUSES}
    for _, fm in lessons:
        if fm.get("status") in counts:
            counts[fm["status"]] += 1
    n_units = sum(
        len(lvl.get("units") or [])
        for t in repo.syllabus["tracks"].values()
        for lvl in (t.get("levels") or {}).values()
    )

    out = [
        "# Índice de lecciones",
        "",
        INDEX_HEADER,
        "",
        f"**{len(lessons)} lecciones** en {n_units} unidades planificadas · "
        f"{counts['published']} publicadas · {counts['review']} en revisión · {counts['draft']} borradores.",
        "",
        "Columna *Habla*: porcentaje planificado de tiempo de habla del estudiante (mínimo "
        f"{MIN_SPEAKING_RATIO:.0%}). Las unidades sin lecciones aparecen como pendientes.",
    ]
    for code, track in repo.syllabus["tracks"].items():
        out += ["", f"## {code} · {track['name']}"]
        for level, lvl in (track.get("levels") or {}).items():
            out += ["", f"### {code} {level}", ""]
            meta = []
            if lvl.get("focus"):
                meta.append(f"**Enfoque:** {lvl['focus']}")
            if lvl.get("guided_hours"):
                meta.append(f"**Horas de referencia:** {lvl['guided_hours']}")
            if meta:
                out += [" · ".join(meta), ""]
            out += [
                "| Unidad | Título | Meta de speaking | Lecciones | Habla |",
                "|---|---|---|---|---|",
            ]
            for u in lvl.get("units") or []:
                items = sorted(by_unit.get((code, level, u["unit"]), []), key=lambda x: x[1].get("lesson", 0))
                if items:
                    links = "<br>".join(
                        f"[L{fm['lesson']:02d} · {fm['title'].replace('|', '/')}]"
                        f"({p.relative_to(repo.lessons_dir).as_posix()}) "
                        f"({STATUS_LABELS.get(fm.get('status'), fm.get('status'))})"
                        for p, fm in items
                    )
                    ratios = "<br>".join(_speaking_ratio(fm) for _, fm in items)
                else:
                    links, ratios = "*pendiente*", "—"
                out.append(f"| U{u['unit']:02d} | {u['title']} | {u['speaking_goal']} | {links} | {ratios} |")
    return "\n".join(out) + "\n"


# --- Nueva lección -----------------------------------------------------------------------------


def render_new_lesson(
    repo: Repo,
    *,
    track: str,
    level: str,
    unit: int,
    lesson: int,
    title: str,
    author: str,
    ai_assisted: bool = False,
    today: dt.date | None = None,
) -> str:
    u = repo.unit(track, level, unit)
    if not u:
        raise ValueError(f"la unidad {track}-{level}-U{unit:02d} no existe en curriculum/syllabus.yml")
    codes = list(u.get("l1_focus") or [])[:MAX_L1_FOCUS]
    l1_list = "\n".join(f"  - {c}" for c in codes)
    l1_rows = "\n".join(
        f"| {c} | {repo.catalog.get(c, '')} | ✗ *TODO: error típico en contexto* | ✓ TODO: forma meta | TODO: actividad |"
        for c in codes
    )
    template = read_text(repo.root / "templates" / "lesson-template.md")
    values = {
        "id": f"{track}-{level}-U{unit:02d}-L{lesson:02d}",
        "title": title.replace('"', "'"),
        "track": track,
        "level": level,
        "unit": str(unit),
        "lesson": str(lesson),
        "date": (today or dt.date.today()).isoformat(),
        "author": author.replace('"', "'"),
        "ai_assisted": "true" if ai_assisted else "false",
        "can_do": u["speaking_goal"].replace('"', "'"),
        "unit_title": u["title"],
        "l1_focus": l1_list,
        "l1_rows": l1_rows,
    }
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    leftover = re.findall(r"\{\{[a-z_]+\}\}", template)
    if leftover:
        raise ValueError(f"marcadores sin reemplazar en la plantilla: {sorted(set(leftover))}")
    return template


def lesson_path(repo: Repo, track: str, level: str, unit: int, lesson: int, slug: str) -> Path:
    t = repo.track(track)
    if not t:
        raise ValueError(f"track '{track}' no existe")
    return repo.lessons_dir / t["slug"] / level.lower() / f"u{unit:02d}-l{lesson:02d}-{slug}" / "lesson.md"


# --- CLI ---------------------------------------------------------------------------------------


def cmd_validate(repo: Repo, load_errors: list[str]) -> int:
    errors, n = validate_all(repo)
    errors = load_errors + errors
    if errors:
        print(f"✗ {len(errors)} problema(s) encontrados:\n")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"✓ Currículo y {n} lección(es) válidos ({len(repo.catalog)} códigos L1 en el catálogo).")
    return 0


def cmd_index(repo: Repo, check: bool) -> int:
    content = build_index(repo)
    target = repo.lessons_dir / "INDEX.md"
    if check:
        current = read_text(target) if target.exists() else ""
        if current != content:
            print("✗ lessons/INDEX.md está desactualizado. Ejecuta: python tools/lessons.py index")
            return 1
        print("✓ lessons/INDEX.md está al día.")
        return 0
    target.write_text(content, encoding="utf-8")
    print(f"✓ Índice generado en {target.relative_to(repo.root)}")
    return 0


def cmd_new(repo: Repo, args: argparse.Namespace) -> int:
    if not SLUG_RE.match(args.slug):
        print("✗ --slug debe estar en minúsculas, con guiones y sin tildes (p. ej. my-family)")
        return 1
    try:
        path = lesson_path(repo, args.track, args.level, args.unit, args.lesson, args.slug)
        text = render_new_lesson(
            repo,
            track=args.track,
            level=args.level,
            unit=args.unit,
            lesson=args.lesson,
            title=args.title,
            author=args.author,
            ai_assisted=args.ai_assisted,
        )
    except ValueError as exc:
        print(f"✗ {exc}")
        return 1
    if path.exists():
        print(f"✗ Ya existe {path.relative_to(repo.root)}; no se sobrescribe.")
        return 1
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"✓ Lección creada: {path.relative_to(repo.root)}")
    print("  Siguiente paso: completar los TODO, ajustar 'stages' y ejecutar 'python tools/lessons.py validate'.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="valida currículo y lecciones")
    p_index = sub.add_parser("index", help="genera lessons/INDEX.md")
    p_index.add_argument("--check", action="store_true", help="falla si el índice no está actualizado")
    p_new = sub.add_parser("new", help="crea una lección desde la plantilla")
    p_new.add_argument("--track", required=True, help="código del track (p. ej. GEN, PHA)")
    p_new.add_argument("--level", required=True, choices=LEVELS)
    p_new.add_argument("--unit", required=True, type=int)
    p_new.add_argument("--lesson", required=True, type=int)
    p_new.add_argument("--slug", required=True, help="nombre corto de la carpeta, p. ej. my-family")
    p_new.add_argument("--title", required=True, help="título de la lección (en inglés)")
    p_new.add_argument("--author", required=True)
    p_new.add_argument("--ai-assisted", action="store_true", help="marca la lección como borrador asistido por IA")
    args = parser.parse_args(argv)

    repo, load_errors = load_repo()
    if args.command == "validate":
        return cmd_validate(repo, load_errors)
    if load_errors:
        for e in load_errors:
            print(f"✗ {e}")
        return 1
    if args.command == "index":
        return cmd_index(repo, args.check)
    return cmd_new(repo, args)


if __name__ == "__main__":
    sys.exit(main())
