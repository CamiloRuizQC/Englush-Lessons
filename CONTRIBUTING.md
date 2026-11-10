# Cómo contribuir

¡Gracias por ayudar a mejorar estas lecciones! Este documento resume el flujo de trabajo. Las reglas pedagógicas están en [docs/](docs/).

## Flujo de trabajo

1. **Propón** la lección o el cambio con un *issue* (plantillas *Nueva lección* o *Error en contenido*).
2. **Crea una rama** desde `main`: `leccion/gen-a1-u02-l01`, `fix/ipa-gen-a2-u03-l01`, `docs/catalogo-voc-34`.
3. **Crea la lección** con la herramienta (no copies a mano otra lección):

    ```bash
    pip install -r requirements.txt
    python tools/lessons.py new --track GEN --level A1 --unit 2 --lesson 1 \
      --slug this-is-my-family --title "This is my family" --author "Tu nombre"
    ```

4. **Completa** todos los `TODO` siguiendo [la estructura](docs/02-estructura-de-leccion.md) y [la guía de estilo](docs/05-guia-de-estilo.md).
5. **Verifica localmente:**

    ```bash
    python tools/lessons.py validate
    python tools/lessons.py index
    python -m unittest discover -s tests
    npx markdownlint-cli2 "**/*.md"   # opcional; también corre en CI
    ```

6. **Abre un pull request** y completa la lista de verificación de la plantilla.
7. **Revisión:** al menos una persona distinta del autor revisa el contenido. Solo después puede pasar a `published`, agregando a esa persona en `reviewers`.

## Qué revisar en un pull request de contenido

- [ ] La tarea comunicativa es realista y relevante para adultos latinoamericanos.
- [ ] El tiempo de habla planificado es creíble (no solo pasa el validador).
- [ ] Los errores ✗ son reales y frecuentes; las formas ✓ son naturales.
- [ ] Las transcripciones IPA y las sílabas tónicas están verificadas con el diccionario.
- [ ] Los datos de modelos y role-plays son ficticios.
- [ ] El prompt de IA tiene corrección diferida y foco en los códigos L1 de la lección.

## Contenido asistido por IA

Se puede usar IA para redactar borradores (ver [CLAUDE.md](CLAUDE.md)). En ese caso:

- Marca `ai_assisted: true` y deja la lección en `draft`.
- Quien revise debe verificar con especial cuidado la IPA, la naturalidad del inglés y la exactitud de las notas contrastivas.

## Audio

Instala [Git LFS](https://git-lfs.com) antes de agregar audio (`git lfs install`). Los formatos de audio ya están configurados en `.gitattributes`.

## Privacidad

No subas grabaciones, bitácoras ni datos personales de aprendices a este repositorio. La [bitácora de speaking](templates/speaking-log.md) es una plantilla para copiar en un lugar privado.
