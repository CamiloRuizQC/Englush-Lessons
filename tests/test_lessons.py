"""Pruebas de tools/lessons.py. Ejecutar con: python -m unittest discover -s tests -v"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import lessons as L  # noqa: E402

SAMPLE_REL = Path("general/a1/u01-l01-nice-to-meet-you/lesson.md")


class RepoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo, cls.load_errors = L.load_repo(ROOT)
        cls.sample = L.read_text(cls.repo.lessons_dir / SAMPLE_REL)

    def errors_for(self, text: str, rel: Path = SAMPLE_REL) -> list[str]:
        return L.validate_lesson(self.repo, rel, text)

    def assertHasError(self, errors: list[str], fragment: str) -> None:
        self.assertTrue(
            any(fragment in e for e in errors),
            f"Se esperaba un error que contenga {fragment!r}; errores: {errors}",
        )


class TestRepository(RepoTestCase):
    def test_catalog_loads_without_duplicates(self) -> None:
        self.assertEqual(self.load_errors, [])
        self.assertGreater(len(self.repo.catalog), 50)
        for prefix in ("PRON-", "GRAM-", "VOC-", "PRAG-"):
            self.assertTrue(any(c.startswith(prefix) for c in self.repo.catalog), prefix)

    def test_syllabus_is_valid(self) -> None:
        self.assertEqual(L.validate_syllabus(self.repo), [])

    def test_every_syllabus_unit_has_a_pronunciation_focus(self) -> None:
        for code, track in self.repo.syllabus["tracks"].items():
            for level, lvl in track["levels"].items():
                for unit in lvl["units"]:
                    with self.subTest(unit=f"{code}-{level}-U{unit['unit']:02d}"):
                        self.assertTrue(any(c.startswith("PRON-") for c in unit["l1_focus"]))

    def test_all_lessons_are_valid(self) -> None:
        errors, count = L.validate_all(self.repo)
        self.assertGreater(count, 0)
        self.assertEqual(errors, [])

    def test_index_is_up_to_date(self) -> None:
        index = self.repo.lessons_dir / "INDEX.md"
        self.assertTrue(index.exists(), "Falta lessons/INDEX.md")
        self.assertEqual(L.read_text(index), L.build_index(self.repo))


class TestLessonRules(RepoTestCase):
    def test_sample_lesson_is_valid(self) -> None:
        self.assertEqual(self.errors_for(self.sample), [])

    def test_low_speaking_ratio_fails(self) -> None:
        text = self.sample.replace(
            "{type: task_2, minutes: 10, learner_speaking: 8}",
            "{type: task_2, minutes: 10, learner_speaking: 0}",
        ).replace(
            "{type: task_1, minutes: 10, learner_speaking: 8}",
            "{type: task_1, minutes: 10, learner_speaking: 2}",
        )
        self.assertHasError(self.errors_for(text), "tiempo de habla del estudiante")

    def test_minutes_must_match_duration(self) -> None:
        text = self.sample.replace("duration_min: 60", "duration_min: 90")
        self.assertHasError(self.errors_for(text), "no coincide con duration_min")

    def test_missing_stage_fails(self) -> None:
        text = self.sample.replace("  - {type: pronunciation, minutes: 12, learner_speaking: 8}\n", "")
        self.assertHasError(self.errors_for(text), "faltan etapas obligatorias: pronunciation")

    def test_stage_headings_must_match_metadata(self) -> None:
        text = self.sample.replace("### 1. Warm-up (5 min)", "### 1. Warm-up (6 min)")
        self.assertHasError(self.errors_for(text), "no coinciden con 'stages'")

    def test_unknown_l1_code_fails(self) -> None:
        text = self.sample.replace("  - PRAG-05\n", "  - PRAG-99\n", 1)
        self.assertHasError(self.errors_for(text), "PRAG-99")

    def test_l1_code_must_appear_in_body(self) -> None:
        fm_end = self.sample.find("\n---\n", 4)
        front, body = self.sample[:fm_end], self.sample[fm_end:]
        text = front + body.replace("PRAG-05", "PRAG-XX")
        self.assertHasError(self.errors_for(text), "no se trabaja en el cuerpo")

    def test_pronunciation_code_is_required(self) -> None:
        text = re.sub(r"  - PRON-\d{2}\n", "", self.sample)
        text = text.replace("l1_focus:\n", "l1_focus:\n  - GRAM-01\n  - GRAM-03\n")
        self.assertHasError(self.errors_for(text), "al menos un código de pronunciación")

    def test_missing_section_fails(self) -> None:
        text = self.sample.replace("## Práctica con IA (role-play)", "## Práctica extra")
        self.assertHasError(self.errors_for(text), "Práctica con IA (role-play)")

    def test_published_requires_independent_reviewer(self) -> None:
        text = self.sample.replace("status: draft", "status: published")
        self.assertHasError(self.errors_for(text), "revisor distinto de los autores")
        text = text.replace("reviewers: []", 'reviewers:\n  - "Revisora Humana"')
        self.assertEqual(self.errors_for(text), [])

    def test_review_status_rejects_todo(self) -> None:
        text = self.sample.replace("status: draft", "status: review") + "\nTODO: pendiente\n"
        self.assertHasError(self.errors_for(text), "TODO")

    def test_id_must_match_path(self) -> None:
        rel = Path("general/a2/u01-l01-nice-to-meet-you/lesson.md")
        self.assertHasError(self.errors_for(self.sample, rel), "carpeta de nivel")

    def test_unknown_key_fails(self) -> None:
        text = self.sample.replace("variety: en-US", "variety: en-US\ncolor: blue")
        self.assertHasError(self.errors_for(text), "claves desconocidas")


class TestNewLesson(RepoTestCase):
    def test_rendered_lesson_is_valid_draft(self) -> None:
        text = L.render_new_lesson(
            self.repo,
            track="GEN",
            level="A1",
            unit=2,
            lesson=1,
            title="This is my family",
            author="Test Author",
        )
        rel = Path("general/a1/u02-l01-this-is-my-family/lesson.md")
        self.assertEqual(self.errors_for(text, rel), [])
        self.assertIn("id: GEN-A1-U02-L01", text)
        unit = self.repo.unit("GEN", "A1", 2)
        for code in unit["l1_focus"]:
            self.assertIn(f"| {code} |", text)

    def test_unknown_unit_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            L.render_new_lesson(
                self.repo, track="GEN", level="A1", unit=99, lesson=1, title="X", author="Y"
            )


if __name__ == "__main__":
    unittest.main()
