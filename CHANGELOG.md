# Registro de cambios

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/). Las versiones de cada lección se controlan en su propio campo `version`.

## [Sin publicar]

### Agregado

- Estructura inicial del repositorio con enfoque de speaking para hispanohablantes latinoamericanos.
- Documentación: enfoque pedagógico, catálogo de 86 interferencias L1, estructura de lección, guía de pronunciación, evaluación del speaking, guía de estilo y práctica con IA.
- Currículo `GEN` A1–B2 (24 unidades) y `PHA` B2 (6 unidades) en `curriculum/syllabus.yml`.
- Plantillas: lección, prompt de role-play con IA y bitácora de speaking.
- Lecciones de ejemplo (borradores asistidos por IA): `GEN-A1-U01-L01`, `GEN-A2-U03-L01`, `GEN-B1-U01-L01` y `PHA-B2-U01-L01`.
- `tools/lessons.py`: validación (metadatos, tiempo de habla ≥ 60 %, códigos L1, secciones, rutas), generación del índice y creación de lecciones.
- Pruebas automatizadas e integración continua con GitHub Actions y markdownlint.
