# Descenso del gradiente — Matemáticas para Inteligencia Artificial

**Alumno:** Felipe de Jesús Sánchez Martínez  
**Universidad:** Universidad Tecnológica del Centro de Veracruz  
**Actividad:** Ejercicios 1 al 6 del documento «Ejercicios de descenso de gradiente»  
**Evaluación:** desempeño — repositorio GitHub.

## Contenido de la entrega

- `ejercicios/ejercicio_1.py` a `ejercicios/ejercicio_6.py`: seis programas independientes.
- `ejercicios_1_a_6.py`: programa para ejecutar los seis seguidos.
- `cuadernos/Ejercicios_1_a_6_Colab.ipynb`: cuaderno principal de Google Colab / Jupyter.
- `cuadernos/Ejercicio_1_Paso_a_Paso_Colab.ipynb`: cuaderno explicativo adicional del ejercicio 1.
- `graficas/`: seis gráficas generadas con Python, incluidas comparación con momento y diversos inicios.
- `resultados/resumen_resultados.md`: puntos mínimos, función, tolerancias, iteraciones y justificaciones de los parámetros probados.
- `resultados/comprobacion_consola.txt`: salida real de la ejecución de los seis ejercicios.
- `requirements.txt`: dependencias Python.

## Cómo ejecutar en Google Colab

1. Abrir https://colab.research.google.com/ .
2. Usar **Archivo → Subir cuaderno** y seleccionar `cuadernos/Ejercicios_1_a_6_Colab.ipynb`.
3. Seleccionar **Entorno de ejecución → Ejecutar todas**.
4. Examinar la tabla de las primeras iteraciones, el punto final y la norma del gradiente de cada ejercicio.

## Cómo ejecutar en terminal (Windows / Linux / Codespaces)

Situarse dentro de esta carpeta y ejecutar:

```bash
pip install -r requirements.txt
python ejercicios_1_a_6.py
```

Para un ejercicio individual, por ejemplo:

```bash
python ejercicios/ejercicio_2.py
```

## Qué se comprobó

Los seis ejercicios alcanzaron la tolerancia `||gradiente|| < 1e-6` usando las tasas seleccionadas. Los ejercicios 1, 2 y 3 verifican también el punto manual `x3`; los ejercicios 4 a 6 muestran elección de parámetros, comparaciones y convergencia. Consultar `resultados/resumen_resultados.md` y las gráficas.

## Aviso importante sobre la otra entrega

El documento indica **dos evaluaciones separadas**: para desempeño, entregar GitHub con los seis ejercicios; para producto, entregar **a mano** los ejercicios 1 a 3, con operaciones e iteraciones hasta x3. Este repositorio corresponde al desempeño; **no sustituye las hojas manuscritas**.
