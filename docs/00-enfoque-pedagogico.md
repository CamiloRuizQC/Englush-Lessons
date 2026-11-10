# Enfoque pedagógico

Este documento explica **por qué** las lecciones están construidas como están. Cada principio se etiqueta según su origen:

- **[Marco de referencia]**: proviene de un estándar reconocido (principalmente el MCER / CEFR, Consejo de Europa).
- **[Buena práctica]**: práctica respaldada por investigación en adquisición de segundas lenguas o por la literatura de formación docente.
- **[Convención del repo]**: decisión de diseño de este repositorio, verificada automáticamente por `tools/lessons.py` cuando es posible.

## Para quién es

Adultos y jóvenes hispanohablantes de Latinoamérica que necesitan **hablar** inglés: en el trabajo, en viajes, en entrevistas o en reuniones con clientes y auditores internacionales. El perfil típico entiende más de lo que dice, tiene vocabulario pasivo gracias a los cognados y siente ansiedad al hablar.

## Principios

### 1. El speaking es el eje, no un complemento

**[Convención del repo]** Cada lección planifica **al menos 60 %** del tiempo de clase como habla del estudiante (meta recomendada: 65–75 %). El validador lo calcula a partir de las etapas de la lección y falla si no se cumple.

**[Buena práctica]** Producir lenguaje obliga a procesarlo de forma más profunda que solo comprenderlo: al hablar, el aprendiz nota lo que no sabe decir (*output hypothesis*, Swain). La interacción con negociación de significado ("Sorry? What do you mean?") acelera la adquisición (*interaction hypothesis*, Long).

### 2. Descriptores *can-do* alineados con el MCER

**[Marco de referencia]** Los objetivos se redactan como descriptores "Puedo..." alineados con las escalas de producción e interacción oral del MCER y su Volumen Complementario (Consejo de Europa, 2020), que incluye escalas de **control fonológico**.

**[Convención del repo]** Cada unidad del currículo tiene una meta de speaking y cada lección declara sus *can-do* en los metadatos.

### 3. Tareas comunicativas con repetición

**[Buena práctica]** La clase gira en torno a **tareas** con un resultado comunicativo concreto (presentarse, contar una historia, conducir una reunión), no en torno a la gramática (enfoque comunicativo y aprendizaje basado en tareas: Ellis, 2003; Willis, 1996).

**[Buena práctica]** **Repetir la tarea** con variaciones mejora la fluidez y la precisión: la técnica **4/3/2** (repetir el mismo contenido en menos tiempo y ante nuevos oyentes) es una de las actividades de fluidez mejor documentadas (Nation y Newton, 2009).

**[Convención del repo]** Toda lección tiene `task_1` y `task_2`; la segunda es una repetición con variación (menos tiempo, otro interlocutor o una complicación).

### 4. El ciclo de enseñanza del speaking

**[Buena práctica]** Las 7 etapas obligatorias adaptan el *teaching-speaking cycle* de Goh y Burns (2012):

| Etapa del repo | Propósito | Ciclo de Goh y Burns |
|---|---|---|
| `warm_up` | Hablar desde el minuto uno; activar el tema | Centrar la atención en el speaking |
| `input` | Modelo + tiempo de planificación | Dar input y guiar la planificación |
| `task_1` | Primer intento, foco en el significado | Realizar la tarea de speaking |
| `language_focus` | Trabajar lo que faltó o falló en la tarea | Foco en lenguaje, habilidades y estrategias |
| `pronunciation` | Percepción → producción → contexto | Foco en lenguaje (fonología) |
| `task_2` | Repetición con variación | Repetir la tarea |
| `feedback` | Retroalimentación + autoevaluación | Reflexión y retroalimentación |

Detalles y tiempos en [02-estructura-de-leccion.md](02-estructura-de-leccion.md).

### 5. Las cuatro líneas de Nation, con peso en la producción

**[Buena práctica]** Un curso equilibrado reparte el tiempo entre cuatro líneas: input centrado en el significado, **output centrado en el significado**, aprendizaje centrado en el lenguaje y **desarrollo de la fluidez** (Nation y Newton, 2009). Aquí las dos líneas en negrita reciben más peso dentro de la clase; el input extensivo (escuchar y leer mucho) se asigna sobre todo a la práctica autónoma.

### 6. Enseñanza informada por el español (contraste L1)

**[Buena práctica]** Anticipar las interferencias del español permite priorizar y explicar con eficiencia (Swan y Smith, 2001).

**[Convención del repo]** El [catálogo de interferencias L1](01-interferencias-l1.md) asigna un código a cada fenómeno. Cada lección declara entre 3 y 7 códigos en `l1_focus`, **al menos uno de pronunciación**, y debe trabajarlos en su cuerpo. La retroalimentación y la bitácora del aprendiz usan los mismos códigos.

### 7. Pronunciación orientada a la inteligibilidad

**[Buena práctica]** La meta es ser **inteligible y cómodo de escuchar**, no sonar nativo (Levis, 2018; Derwing y Munro, 2015). Se priorizan los rasgos que más afectan la comprensión en contextos internacionales (Jenkins, 2000): contrastes vocálicos clave, consonantes finales, aspiración, acento de palabra y acento nuclear.

**[Convención del repo]** Pronunciación en **todas** las lecciones, integrada en la tarea y no como un bloque aislado. Ver [03-pronunciacion.md](03-pronunciacion.md).

### 8. Bloques de lenguaje (chunks)

**[Buena práctica]** Las secuencias prefabricadas (*Nice to meet you*, *How long have you...?*, *Let me get back to you*) se recuperan como una sola unidad y liberan atención para el contenido: son un motor de fluidez. Cada lección tiene una tabla de **frases útiles** con notas de pronunciación.

### 9. Retroalimentación: diferida en fluidez, inmediata en precisión

**[Buena práctica]** Interrumpir para corregir durante una tarea de fluidez rompe la comunicación y aumenta la ansiedad. Durante `task_1` y `task_2` el facilitador **anota** (con código L1) y corrige después. En `language_focus` y `pronunciation` la corrección es inmediata, prefiriendo las técnicas que hacen que el aprendiz se autocorrija (elicitación, petición de aclaración, pista metalingüística) sobre la simple reformulación (Lyster y Ranta, 1997). Ver [04-evaluacion-speaking.md](04-evaluacion-speaking.md).

### 10. Uso estratégico del español

**[Buena práctica]** El inglés es la lengua de la clase, pero el español se usa con propósito: explicaciones gramaticales breves en A1–A2, notas contrastivas, verificación de comprensión y reflexión.

**[Convención del repo]** Los metadatos, encabezados y notas para el facilitador van en español; los modelos, frases y prompts de práctica, en inglés. En A1–A2 las instrucciones pueden ir en ambos idiomas.

### 11. Factor afectivo: reducir la ansiedad

**[Buena práctica]** Muchos adultos latinoamericanos llegan con miedo a "hacer el ridículo" al hablar. Las lecciones lo reducen con: **tiempo de planificación** antes de hablar, **ensayo** antes de la tarea real, **repetición** que demuestra progreso en la misma clase, **corrección diferida** y **autoevaluación** basada en logros.

### 12. Práctica autónoma y medición del progreso

**[Buena práctica]** El progreso en speaking requiere práctica entre clases: *shadowing*, grabaciones, repaso espaciado y conversación con un compañero o con IA.

**[Convención del repo]** Cada lección incluye `Práctica autónoma` y `Práctica con IA (role-play)`. El aprendiz lleva una [bitácora de speaking](../templates/speaking-log.md) con grabaciones de referencia periódicas.

## Glosario breve

- **Can-do:** descriptor de lo que el aprendiz puede hacer con la lengua ("Puedo...").
- **Chunk:** bloque de palabras que se aprende y se usa como una unidad.
- **Elicitación:** técnica en la que el facilitador guía al aprendiz para que produzca o corrija él mismo la forma.
- **Inteligibilidad:** grado en que un oyente entiende lo que se dice.
- **Shadowing:** repetir un audio casi al mismo tiempo que se escucha, imitando ritmo y entonación.
- **STT (Student Talking Time):** tiempo de habla del estudiante.
- **4/3/2:** repetir el mismo contenido varias veces con tiempo decreciente para ganar fluidez.

## Referencias

- Consejo de Europa (2020). *Common European Framework of Reference for Languages: Learning, Teaching, Assessment — Companion Volume*. Council of Europe Publishing.
- Derwing, T. M. y Munro, M. J. (2015). *Pronunciation Fundamentals*. John Benjamins.
- Ellis, R. (2003). *Task-Based Language Learning and Teaching*. Oxford University Press.
- Goh, C. C. M. y Burns, A. (2012). *Teaching Speaking: A Holistic Approach*. Cambridge University Press.
- Jenkins, J. (2000). *The Phonology of English as an International Language*. Oxford University Press.
- Levis, J. (2018). *Intelligibility, Oral Communication, and the Teaching of Pronunciation*. Cambridge University Press.
- Lyster, R. y Ranta, L. (1997). Corrective feedback and learner uptake. *Studies in Second Language Acquisition*, 19(1), 37–66.
- Nation, I. S. P. y Newton, J. (2009). *Teaching ESL/EFL Listening and Speaking*. Routledge.
- Swan, M. y Smith, B. (Eds.) (2001). *Learner English* (2.ª ed.). Cambridge University Press.
- Thornbury, S. (2005). *How to Teach Speaking*. Pearson Longman.
- Willis, J. (1996). *A Framework for Task-Based Learning*. Longman.
