# Instrucciones para asistentes de IA

Este repositorio contiene lecciones de inglés con énfasis en speaking para hispanohablantes latinoamericanos. Estas instrucciones aplican a cualquier asistente de IA que cree o edite contenido aquí.

## Antes de escribir

1. Lee `docs/02-estructura-de-leccion.md` (reglas de la lección) y `docs/05-guia-de-estilo.md` (idiomas, IPA, notación).
2. Ubica la unidad en `curriculum/syllabus.yml`. Si no existe, agrégala primero (al final del nivel; nunca renumeres).
3. Usa solo códigos L1 que existan en `docs/01-interferencias-l1.md`. Si necesitas uno nuevo, agrégalo con el siguiente número libre de su categoría, con ejemplo ✗, forma ✓, prioridad y técnica.

## Crear una lección

```bash
python tools/lessons.py new --track GEN --level A1 --unit 2 --lesson 1 \
  --slug this-is-my-family --title "This is my family" \
  --author "Claude (borrador asistido por IA)" --ai-assisted
```

Luego completa todos los `TODO`. Toma como referencia de calidad las lecciones existentes en `lessons/`.

## Reglas no negociables

- **Speaking primero:** tiempo de habla del estudiante ≥ 60 % (meta 65–75 %); `task_2` repite `task_1` con variación.
- **Pronunciación en cada lección:** al menos un código `PRON-` en `l1_focus`, trabajado con percepción → producción → contexto.
- **Cada código de `l1_focus`** aparece en la tabla *Foco L1 para hispanohablantes* con un error real y frecuente.
- **Idiomas:** documentación y notas en español (Latinoamérica neutro); modelos, frases y prompts en inglés americano.
- **IPA:** convención del Cambridge Dictionary (US). Si no estás seguro de una transcripción, márcala con `TODO: verificar IPA` en lugar de inventarla.
- **Datos ficticios** en modelos y role-plays; nunca información real de empresas, clientes, productos o personas.
- **Estado:** una IA deja las lecciones en `draft` (o `review` si no quedan `TODO`), con `ai_assisted: true`. **Nunca** marques una lección como `published` ni te agregues como revisor: la aprobación es humana.

## Antes de terminar

```bash
python tools/lessons.py validate
python tools/lessons.py index
python -m unittest discover -s tests
```

Los tres deben pasar. Usa mensajes de commit en formato *Conventional Commits* en español (ver la guía de estilo).
