# Resultados comprobados — Descenso del gradiente

Fecha de verificación: 26 de noviembre de 2026. Ejecución local de `ejercicios_1_a_6.py` con NumPy y Matplotlib.

Criterio de parada: `||gradiente|| < 1e-6`.

| Ejercicio | Parámetros | Actualizaciones | Punto final aproximado | f(x) final | Norma del gradiente |
|---|---|---:|---|---:|---:|
| 1 | γ=0.15, x0=(0,0) | 24 | (-2,1) | -13 | 5.9605e-7 |
| 2 | γ=0.25, x0=(1,0,1) | 53 | (-3,2,-2) | -20.5 | 9.5567e-7 |
| 3 | γ=0.05, α=0.5, x0=1 | 46 | 2 | -4 | 1.0522e-7 |
| 4 | γ=0.03, x0=(0,0,0,0) | 36 | (1,1,1,1) | -30 | 6.5548e-7 |
| 5 sin momento | γ=0.001, α=0, x0=(-1.2,1) | 32076 | (1,1) | ≈0 | 9.9989e-7 |
| 5 con momento | γ=0.001, α=0.9, x0=(-1.2,1) | 3020 | (1,1) | ≈0 | 9.9850e-7 |
| 6 inicio (-3,-3) | γ=0.04 | 182 | (-2.059792,-2.059792) | -20.0606598 | 9.5073e-7 |
| 6 inicio (0,0) | γ=0.04 | 199 | (-2.059792,-2.059792) | -20.0606598 | 9.6599e-7 |
| 6 inicio (3,3) | γ=0.04 | 185 | (1.934298,1.934298) | -12.0645863 | 9.5270e-7 |

## Selección heurística (ejercicio 4)

Con x0=(0,0,0,0) y máximo de 150 actualizaciones: γ=0.01 alcanzó tolerancia en 123; γ=0.02 en 58; γ=0.03 en 36; γ=0.04 no alcanzó tolerancia dentro de ese límite (norma final ≈3.73424). Se adoptó γ=0.03 para la prueba principal.

## Comparación con/sin momento (ejercicio 5)

Con el mismo punto inicial y γ, el momento α=0.9 redujo las actualizaciones de 32076 a 3020 (≈90.6 % menos). No se debe interpretar como una ventaja universal: depende del problema y los parámetros. La curva con momento presenta oscilaciones iniciales.

## Diferentes mínimos (ejercicio 6)

Los puntos iniciales negativos y el origen convergieron al mínimo global aproximado (-2.059792,-2.059792), f≈-20.060660. El inicio positivo terminó en otro mínimo local (1.934298,1.934298), f≈-12.064586. La justificación analítica usa el hecho de que (x2-x1)^2≥0, con igualdad en x2=x1.

## Comparación de tablas a mano

- Ejercicio 1: x3=(-1.872,1.125), f(x3)=-12.889107.
- Ejercicio 2: x3=(-1.3125,1.96875,-2.046875), f(x3)=-19.069213867.
- Ejercicio 3: x3≈1.63811996, f(x3)≈-3.56666546.

La salida completa de la ejecución está en `comprobacion_consola.txt`. Las seis gráficas están en `../graficas`.
