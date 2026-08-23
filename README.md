# Tarea 1 — Introducción

Plantilla de tarea para el curso de Métodos Numéricos.

## Archivos

- `Tarea1_Introduccion.ipynb` — notebook que recibe el alumno.
- `grader.py` — banco de preguntas + calificación + envío (fuente, **NO se sube**).
- `grader_ofuscado.txt` — versión ofuscada que **SÍ se sube** (generada con `tools/ofuscar.py`).
- `lib/robomat.py`, `lib/matlab_like.py` — sintaxis estilo MATLAB.
- `alumnos.csv` — lista oficial de alumnos (id, nombre, correo).
- `img/` — diagramas SVG vectoriales.

## Antes de publicar

1. Edita `grader.py`: pon tu `APPS_SCRIPT_URL`, tu `WEBHOOK_TOKEN` (el mismo que guardaste en las propiedades del Script de Apps Script) y las preguntas reales.
2. Genera el ofuscado:
   ```
   python tools/ofuscar.py
   ```
3. `alumnos.csv` es opcional (la identificación es automática con el correo institucional @tecnm.mx).
4. Cambia `REPO_URL` / `REPO_NOMBRE` en la celda de configuración del notebook.
5. Crea el repositorio en GitHub (uno por tarea) y súbelo.
6. Comparte el enlace de Colab del notebook.

## Nota de seguridad

La ofuscación (zlib + base64) es un **disuasivo**, no cifrado. El anticopia real
viene de que cada alumno tiene preguntas personalizadas (semilla = su ID) y de que
el envío es único. Las credenciales de Google Sheets NO se guardan en el notebook.
