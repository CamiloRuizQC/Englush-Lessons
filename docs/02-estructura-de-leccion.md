# Estructura de una lección

Toda lección es un archivo `lesson.md` creado desde la [plantilla](../templates/lesson-template.md) con `python tools/lessons.py new`. Este documento describe sus partes y las reglas que verifica el validador.

## Ubicación y nombre

```text
lessons/<track>/<nivel>/u<NN>-l<NN>-<slug>/lesson.md
lessons/<track>/<nivel>/u<NN>-l<NN>-<slug>/audio/      (opcional)
```

- `<track>`: el `slug` del track en `curriculum/syllabus.yml` (`general`, `pharma`).
- `<nivel>`: el nivel MCER en minúsculas (`a1`, `a2`, `b1`, `b2`, `c1`).
- `<slug>`: nombre corto en inglés, en minúsculas, con guiones y sin tildes (`nice-to-meet-you`).
- **Identificador:** `TRK-NIVEL-Unn-Lnn`, por ejemplo `GEN-A1-U01-L01`. Debe coincidir con la ruta y con los metadatos.

## Metadatos (front matter)

| Clave | Obligatoria | Descripción |
|---|---|---|
| `id` | Sí | Identificador único (`GEN-A1-U01-L01`). |
| `title` | Sí | Título en inglés, tal como lo ve el aprendiz. |
| `track`, `level`, `unit`, `lesson` | Sí | Deben existir en el currículo y coincidir con el `id` y la ruta. |
| `duration_min` | Sí | Duración total; debe ser igual a la suma de minutos de `stages`. |
| `variety` | Sí | `en-US` (predeterminada) o `en-GB`. |
| `status` | Sí | `draft`, `review` o `published` (ver ciclo de vida). |
| `version` | Sí | Versión semántica `X.Y.Z`. |
| `last_reviewed` | Sí | Fecha ISO `AAAA-MM-DD`. |
| `authors` | Sí | Lista de autores. |
| `reviewers` | No* | Lista de revisores. *Obligatoria para `published`. |
| `ai_assisted` | No | `true` si el borrador fue generado o asistido por IA. |
| `can_do` | Sí | Objetivos "Puedo..." (el primero suele ser la meta de la unidad). |
| `speaking_functions` | Sí | Funciones comunicativas (*greeting, narrating...*). |
| `grammar`, `vocabulary` | Sí | Listas (pueden estar vacías si la lección no lo requiere). |
| `l1_focus` | Sí | 3–7 códigos del [catálogo L1](01-interferencias-l1.md), al menos uno `PRON-`. |
| `stages` | Sí | Las 7 etapas con `type`, `minutes` y `learner_speaking`. |
| `tags`, `prerequisites`, `materials` | No | Listas libres. |

## Etapas y tiempo de habla

Las 7 etapas son obligatorias; `task_1` va antes que `task_2`. Cada etapa declara cuántos minutos dura y cuántos de ellos **habla el estudiante** (estimación de planificación).

| Etapa (`type`) | Encabezado en el cuerpo | Min. típicos | Habla típica |
|---|---|---|---|
| `warm_up` | `### 1. Warm-up (5 min)` | 5 | 4 |
| `input` | `### 2. Input y preparación (8 min)` | 8 | 3 |
| `task_1` | `### 3. Tarea de habla 1 (10 min)` | 10 | 8 |
| `language_focus` | `### 4. Foco en la forma (8 min)` | 8 | 4 |
| `pronunciation` | `### 5. Pronunciación (10 min)` | 10 | 7 |
| `task_2` | `### 6. Tarea de habla 2 (12 min)` | 12 | 10 |
| `feedback` | `### 7. Retroalimentación y reflexión (7 min)` | 7 | 4 |
| **Total** | | **60** | **40 (67 %)** |

**Reglas que verifica el validador:**

1. La suma de `minutes` es igual a `duration_min`.
2. `learner_speaking` está entre 0 y `minutes` en cada etapa.
3. Tiempo de habla del estudiante = Σ `learner_speaking` / Σ `minutes` **≥ 60 %**.
4. Los encabezados `### N. Etapa (M min)` de la sección *Secuencia de la clase* coinciden, en orden, con los minutos de `stages`.

Cómo estimar `learner_speaking`: cuenta solo el tiempo en que el aprendiz produce lenguaje en voz alta (responder, preguntar, repetir, narrar, hacer *shadowing*). Leer en silencio, escuchar explicaciones o escribir notas no cuenta. En grupo, estima el tiempo de habla **por aprendiz**.

## Secciones obligatorias (en este orden)

1. `## Objetivos (can-do)`
2. `## Lenguaje clave` (frases útiles, gramática en contexto, vocabulario)
3. `## Foco L1 para hispanohablantes` (tabla con cada código de `l1_focus`)
4. `## Secuencia de la clase` (las 7 etapas como `###`)
5. `## Evaluación del speaking` (cómo se ve "Logrado (3)" en esta lección)
6. `## Práctica autónoma`
7. `## Práctica con IA (role-play)` (prompt listo para copiar)
8. `## Notas para el facilitador` (claves, adaptaciones, notas culturales)

Se pueden agregar otras secciones (por ejemplo, anexos) siempre que las obligatorias mantengan su orden.

## Buenas prácticas de redacción por etapa

- **Warm-up:** sin corrección; el aprendiz habla en el primer minuto.
- **Input:** el modelo es breve (1–2 min de audio), natural y muestra exactamente el lenguaje que la tarea necesitará. Siempre con transcripción. Incluye **tiempo de planificación** con palabras clave, no con oraciones completas (para no leer).
- **Tarea 1:** instrucciones claras, tarjetas de rol cuando aplique y un resultado observable. El facilitador anota errores con su código L1, sin interrumpir.
- **Foco en la forma:** parte de los errores reales de la tarea 1 más los focos planificados; la práctica es **oral**.
- **Pronunciación:** percepción (¿lo oigo?) → producción controlada (¿lo digo aislado?) → producción en contexto (¿lo digo en la tarea?).
- **Tarea 2:** misma tarea con variación: menos tiempo (4/3/2), otro interlocutor o una complicación realista.
- **Retroalimentación:** 2 fortalezas y máximo 3 errores prioritarios; autoevaluación con *can-do*; actualización de la bitácora.

## Ciclo de vida y control de cambios

```text
draft ──► review ──► published
  ▲          │            │
  └──────────┴────────────┘  (cambios mayores vuelven a review)
```

| Estado | Significado | Requisitos |
|---|---|---|
| `draft` | En construcción. Puede contener `TODO`. | Estructura válida. |
| `review` | Lista para revisión por otra persona. | Sin `TODO`. |
| `published` | Aprobada para usar con aprendices. | Sin `TODO` y al menos un revisor **distinto** de los autores. |

- **Revisión por pares:** ninguna lección pasa a `published` sin revisión de una segunda persona. Si `ai_assisted: true`, el revisor verifica especialmente las transcripciones IPA, los ejemplos de error y la naturalidad del inglés.
- **Versionado semántico:** `MAJOR` si cambian objetivos o la estructura de la tarea; `MINOR` si se agregan o reemplazan actividades; `PATCH` para erratas. Actualiza `last_reviewed` en cada cambio.
- **Trazabilidad:** todo cambio entra por *pull request* con la lista de verificación de la plantilla de PR; el historial de Git es el registro de cambios de cada lección.
