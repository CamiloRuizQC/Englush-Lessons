# Guía de estilo

Reglas para que todas las lecciones se vean y suenen igual, sin importar quién las escriba (una persona o una IA).

## Idiomas

| Elemento | Idioma |
|---|---|
| Documentación, metadatos de apoyo, encabezados, notas para el facilitador | Español (Colombia / Latinoamérica neutro) |
| Títulos de lecciones y unidades, modelos, frases útiles, tarjetas de rol, prompts de IA | Inglés |
| Instrucciones al aprendiz | A1–A2: español o bilingüe · B1+: inglés |
| Ejemplos de error | Inglés, marcados con ✗ |

- Español neutro latinoamericano: *tú* para dirigirse al aprendiz, sin *vosotros*; evitar regionalismos fuertes.
- Inglés: oraciones naturales, como las diría un hablante real en esa situación; nada de "inglés de libro" rígido.

## Variedad de inglés

- **Predeterminada: inglés americano general (`en-US`)**, por ser la más usada en el contexto laboral latinoamericano. Ortografía americana (*color, center, analyze*), vocabulario americano (*check* en el restaurante, *apartment*, *cell phone*).
- Si una lección usa inglés británico, declara `variety: en-GB` y es coherente en toda la lección.
- Las diferencias relevantes se mencionan en notas (*Z = /ziː/ in the US, /zed/ in the UK*).

## Transcripciones fonéticas

- IPA entre barras para fonemas (/ʃɪp/) y entre corchetes para detalle fonético ([pʰɪn]).
- Convención: la del **Cambridge Dictionary, pronunciación US**: /iː/, /ɪ/, /e/, /æ/, /ɑː/, /ʌ/, /ʊ/, /uː/, /ə/, /ɝː/, /ɚ/, /eɪ/, /aɪ/, /oʊ/, /aʊ/, /ɔɪ/.
- Verifica cada transcripción con el audio del diccionario antes de pasar una lección a `review`.
- Para el acento de palabra en materiales del aprendiz, usa MAYÚSCULAS en la sílaba tónica (*exPErience*, *LAB-ra-tor-y*); reserva el IPA para el facilitador y para los casos de duda.
- Entonación: ↗ (sube) y ↘ (baja). Enlace: ‿ (*an‿apple*).

## Notación de errores

- ✗ *ejemplo de error en cursiva* → ✓ forma meta en texto normal.
- Siempre con su código L1 cuando exista: ✗ *I have 34 years.* (GRAM-02).
- Los errores de ejemplo deben ser **reales y frecuentes** en hispanohablantes, no inventados para la ocasión.

## Contenido y representación

- Nombres y contextos diversos de toda Latinoamérica (no solo de un país) y del mundo angloparlante.
- Evitar estereotipos nacionales, de género o de profesión; alternar géneros en roles de autoridad y de servicio.
- Situaciones relevantes para adultos latinoamericanos: trabajo, trabajo remoto para empresas extranjeras, viajes, salud, trámites, familia.
- **Datos ficticios** en todos los modelos y role-plays, especialmente en el track profesional (empresas, productos, resultados, personas). Nunca información confidencial real.
- Temas sensibles (edad, religión, política, salud): tratarlos con opción de inventar la respuesta.

## Audio

- Archivos en `audio/` dentro de la carpeta de la lección: `model.mp3`, `shadowing-01.mp3`, etc.
- Toda pieza de audio tiene su **transcripción** en la lección (accesibilidad y shadowing).
- Formato recomendado: MP3 mono, 64–128 kbps. Los archivos de audio se versionan con Git LFS (ver `.gitattributes`).
- Si se usa síntesis de voz, indícalo en las notas para el facilitador.

## Markdown

- Un solo `#` por archivo; las secciones obligatorias en `##`; las etapas en `###`.
- Tablas para frases útiles, foco L1 y rúbricas; listas numeradas para procedimientos.
- Bloques de código con lenguaje declarado (`text` para diálogos y prompts, `yaml`, `bash`).
- Enlaces relativos entre archivos del repositorio.
- Fechas en ISO 8601 (`2026-11-10`).
- El estilo se verifica con `markdownlint` (configuración en `.markdownlint-cli2.jsonc`).

## Nombres de archivos y carpetas

- Minúsculas, guiones, sin tildes ni espacios: `u03-l01-how-was-your-weekend`.
- Documentación numerada para fijar el orden de lectura: `docs/00-...`, `docs/01-...`.

## Mensajes de commit

Formato *Conventional Commits* en español:

```text
feat(leccion): agrega GEN-A1-U02-L01 "This is my family"
fix(leccion): corrige transcripción IPA en GEN-A2-U03-L01
docs(catalogo): agrega VOC-34 "assume"
chore(ci): actualiza versión de markdownlint
```

Tipos: `feat` (lección o funcionalidad nueva), `fix` (corrección), `docs` (documentación o catálogo), `refactor`, `test`, `chore`.
