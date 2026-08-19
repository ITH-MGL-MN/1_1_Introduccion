"""Genera grader_ofuscado.txt a partir de grader.py (misma carpeta).

Uso (en la PC del profesor, dentro de la carpeta de la tarea):
    python tools/ofuscar.py
"""
import base64
import pathlib
import zlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FUENTE = RAIZ / 'grader.py'
SALIDA = RAIZ / 'grader_ofuscado.txt'


def main():
    src = FUENTE.read_text(encoding='utf-8')
    # Comprime el TEXTO FUENTE (no bytecode) para ser compatible con
    # cualquier versión de Python que use Colab.
    blob = base64.b64encode(zlib.compress(src.encode('utf-8'))).decode()
    SALIDA.write_text(blob, encoding='utf-8')
    print(f'✅ Generado {SALIDA.name} ({len(blob)} caracteres) desde {FUENTE.name}')


if __name__ == '__main__':
    main()
