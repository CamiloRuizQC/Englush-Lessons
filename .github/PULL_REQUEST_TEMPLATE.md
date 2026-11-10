<!-- markdownlint-disable-file MD041 -->

## Descripción

<!-- Qué cambia y por qué. Enlaza el issue relacionado (p. ej., Closes #12). -->

## Tipo de cambio

- [ ] Lección nueva
- [ ] Corrección de una lección existente
- [ ] Currículo o catálogo L1
- [ ] Documentación
- [ ] Herramientas o CI

## Lista de verificación

- [ ] `python tools/lessons.py validate` pasa.
- [ ] `python tools/lessons.py index` ejecutado (índice actualizado).
- [ ] `python -m unittest discover -s tests` pasa.
- [ ] El tiempo de habla planificado es realista (no solo supera el 60 %).
- [ ] Cada código de `l1_focus` tiene un error real y frecuente en la tabla de foco L1.
- [ ] Las transcripciones IPA y sílabas tónicas fueron verificadas con el diccionario.
- [ ] Los modelos y role-plays usan solo datos ficticios.
- [ ] Si el contenido fue asistido por IA, `ai_assisted: true` y el estado es `draft` o `review`.
- [ ] Se actualizaron `version` y `last_reviewed` de las lecciones modificadas.
- [ ] Se actualizó `CHANGELOG.md` si el cambio es relevante.

## Revisión

<!-- Para pasar una lección a `published`, una persona distinta del autor la revisa y se agrega en `reviewers`. -->
