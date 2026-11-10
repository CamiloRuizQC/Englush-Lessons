# Currículo

El alcance y la secuencia viven en [`syllabus.yml`](syllabus.yml), la fuente única de verdad del currículo. El [índice de lecciones](../lessons/INDEX.md) se genera a partir de este archivo y muestra qué unidades ya tienen lecciones y cuáles están pendientes.

## Tracks

| Código | Carpeta | Nombre | Niveles |
|---|---|---|---|
| `GEN` | `lessons/general/` | Inglés general comunicativo | A1–B2 (6 unidades por nivel) |
| `PHA` | `lessons/pharma/` | Inglés para la industria farmacéutica (ESP) — Control de Calidad | B2 (requiere B1 consolidado) |

Para agregar un track (por ejemplo, inglés para tecnología o para atención al cliente), añade una entrada en `tracks` con un código de 3 letras, un `slug` para la carpeta y sus niveles y unidades.

## Cómo se diseñó

- **Unidad = una meta de speaking.** Cada unidad tiene un descriptor *can-do* alineado con las escalas orales del MCER, funciones comunicativas, gramática de apoyo y focos L1 del [catálogo](../docs/01-interferencias-l1.md).
- **Currículo en espiral.** Los focos L1 de prioridad alta reaparecen en varios niveles (por ejemplo, PRON-18 en A2, B1, B2 y PHA), cada vez en tareas más exigentes.
- **Pronunciación en todas las unidades.** Cada unidad incluye al menos un foco `PRON-`.
- **Funciones antes que gramática.** La gramática aparece porque la tarea la necesita (*How long have you...?* para hablar de experiencia laboral), no al revés.

## Lecciones por unidad y horas

Recomendación: **3–4 lecciones de 60 minutos por unidad** más **15–30 minutos diarios de práctica autónoma** (shadowing, grabaciones, role-plays con IA).

Las horas de referencia por nivel (`guided_hours`) son **orientativas** y corresponden al aprendizaje guiado acumulado en **todas** las destrezas. Este repositorio cubre el componente de **speaking e interacción**; complementa con exposición abundante a audio y lectura en inglés.

## Reglas de mantenimiento

1. No renumeres unidades que ya tienen lecciones: agrega unidades nuevas al final del nivel.
2. Toda unidad necesita `title` (en inglés), `speaking_goal` (en español, "Puedo...") y `l1_focus`.
3. Después de editar el currículo, ejecuta:

```bash
python tools/lessons.py validate
python tools/lessons.py index
```
