# Lecciones de inglés con énfasis en speaking para hispanohablantes latinoamericanos

[![CI](https://github.com/CamiloRuizQC/Englush-Lessons/actions/workflows/ci.yml/badge.svg)](https://github.com/CamiloRuizQC/Englush-Lessons/actions/workflows/ci.yml)

Repositorio de lecciones de inglés diseñadas para que hispanohablantes de Latinoamérica **hablen**: cada clase dedica la mayor parte del tiempo a la producción oral, trabaja la pronunciación en todas las sesiones y anticipa los errores típicos que produce el español.

## Qué lo hace diferente

- **Speaking primero, con regla verificable.** Cada lección planifica al menos **60 %** del tiempo como habla del estudiante; el validador lo calcula y falla si no se cumple.
- **Enseñanza informada por el español.** Un [catálogo de 86 interferencias](docs/01-interferencias-l1.md) (pronunciación, gramática, falsos amigos y pragmática) con códigos como `PRON-13` (terminación *-ed*) o `VOC-01` (*actually* ≠ actualmente). Las lecciones, la retroalimentación y la bitácora del aprendiz usan los mismos códigos.
- **Ciclo de enseñanza del speaking.** Siete etapas obligatorias con **repetición de la tarea** (4/3/2) para ganar fluidez ([estructura](docs/02-estructura-de-leccion.md)).
- **Pronunciación orientada a la inteligibilidad**, no al acento nativo ([guía](docs/03-pronunciacion.md)).
- **Alineado con el MCER (CEFR)**: objetivos *can-do* y rúbrica basada en los aspectos cualitativos del habla ([evaluación](docs/04-evaluacion-speaking.md)).
- **Práctica con IA lista para usar**: cada lección trae un prompt de role-play con corrección diferida ([guía y límites](docs/06-practica-con-ia.md)).
- **Control de calidad del contenido**: metadatos validados, revisión por una segunda persona antes de publicar, versionado e integración continua.

## Estructura

```text
.
├── curriculum/
│   ├── syllabus.yml          # Alcance y secuencia (fuente única de verdad)
│   └── README.md
├── docs/
│   ├── 00-enfoque-pedagogico.md
│   ├── 01-interferencias-l1.md   # Catálogo de códigos PRON/GRAM/VOC/PRAG
│   ├── 02-estructura-de-leccion.md
│   ├── 03-pronunciacion.md
│   ├── 04-evaluacion-speaking.md
│   ├── 05-guia-de-estilo.md
│   └── 06-practica-con-ia.md
├── lessons/
│   ├── INDEX.md              # Índice generado automáticamente
│   ├── general/<nivel>/uNN-lNN-<slug>/lesson.md
│   └── pharma/<nivel>/uNN-lNN-<slug>/lesson.md
├── templates/
│   ├── lesson-template.md
│   ├── ai-roleplay-prompt.md
│   └── speaking-log.md       # Bitácora del aprendiz
├── tools/lessons.py          # Validar, generar índice, crear lecciones
└── tests/
```

## Tracks y niveles

| Track | Niveles | Estado |
|---|---|---|
| `GEN` Inglés general comunicativo | A1 · A2 · B1 · B2 (24 unidades) | Currículo completo; lecciones de ejemplo en A1, A2 y B1 |
| `PHA` Inglés para la industria farmacéutica — Control de Calidad | B2 (6 unidades) | Currículo completo; lección de ejemplo de reunión de apertura de auditoría |

Consulta el avance en el [índice de lecciones](lessons/INDEX.md).

## Cómo usarlo

### Si eres aprendiz

1. Haz la grabación inicial con el texto de diagnóstico de [docs/03-pronunciacion.md](docs/03-pronunciacion.md).
2. Copia la [bitácora de speaking](templates/speaking-log.md) en un lugar privado.
3. Sigue las lecciones de tu nivel desde el [índice](lessons/INDEX.md); entre clases, haz la *Práctica autónoma* y la *Práctica con IA* de cada lección.

### Si eres facilitador

1. Lee [00-enfoque-pedagogico.md](docs/00-enfoque-pedagogico.md) y [04-evaluacion-speaking.md](docs/04-evaluacion-speaking.md).
2. Usa la sección *Notas para el facilitador* de cada lección (claves, adaptaciones para grupo o clase virtual).
3. Durante las tareas, anota errores con su código L1; corrige después.

### Si creas lecciones

Requisitos: Python 3.10+ y PyYAML.

```bash
pip install -r requirements.txt

# Crear una lección desde la plantilla (toma los focos L1 de la unidad)
python tools/lessons.py new --track GEN --level A1 --unit 2 --lesson 1 \
  --slug this-is-my-family --title "This is my family" --author "Nombre Apellido"

# Validar estructura, metadatos, tiempo de habla y códigos L1
python tools/lessons.py validate

# Regenerar el índice
python tools/lessons.py index

# Ejecutar las pruebas
python -m unittest discover -s tests -v
```

Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de abrir un *pull request*.

## Uso responsable de la IA

Las lecciones de ejemplo son **borradores asistidos por IA** (`ai_assisted: true`, `status: draft`). Antes de usarlas con aprendices deben pasar por revisión humana: verificar transcripciones IPA, naturalidad del inglés y pertinencia cultural. Una lección solo puede marcarse como `published` si tiene al menos un revisor distinto de sus autores.

## Licencia

- Contenido educativo (lecciones, documentación, plantillas y currículo): [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es).
- Código (`tools/`, `tests/`): MIT.

Detalles en [LICENSE](LICENSE).
