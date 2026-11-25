# Matemáticas para Inteligencia Artificial — Descenso del gradiente

Ejercicios 1 a 6 del documento «Ejercicios de descenso de gradiente».

## Contenido
- `cuadernos/Ejercicio_1_Paso_a_Paso_Colab.ipynb`: ejercicio 1 explicado con operaciones, tabla y gráfica.
- `cuadernos/Ejercicios_1_a_6_Gradiente.ipynb`: los seis ejercicios programados.
- `ejercicios_1_a_6.py`: versión ejecutable desde terminal.
- `graficas/e1.png` a `graficas/e6_inicios.png`: resultados de convergencia.

## Ejecutar en Google Colab
1. Abrir https://colab.research.google.com/
2. Menú Archivo → Subir cuaderno.
3. Seleccionar un archivo `.ipynb` de la carpeta `cuadernos`.
4. Ejecutar las celdas en orden.

## Ejecutar desde terminal
Instalar dependencias con `pip install numpy pandas matplotlib` y después `python ejercicios_1_a_6.py`.

## Nota
Los ejercicios 1–3 se comparan con sus tres iteraciones manuales y continúan hasta ||gradiente|| < 1e-6. Los ejercicios 4–6 usan parámetros seleccionados heurísticamente. Los ejercicios 3 y 5 implementan momento según el enunciado del PDF.
