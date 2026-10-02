# 1. Vectores y sus representaciones

[Índice](../README.md) · [Siguiente: operaciones](02-operaciones-con-vectores.md)

## ¿Qué es?

En los ejemplos de esta guía, un vector es una **lista ordenada de números**. Cada número es una componente y ocupa un lugar con significado. Cambiar el orden puede cambiar lo que estamos describiendo.

## Entendiendo la idea

Imagina un objeto en un escenario 3D. Para ubicarlo respecto a un origen necesitas tres coordenadas: X, Y y Z. La lista `(2, 4, 1)` reúne esas tres cantidades.

Una posición y un desplazamiento no significan lo mismo: la posición indica dónde está algo respecto al origen; el desplazamiento indica cuánto cambia su posición. Ambos pueden describirse mediante tres componentes. Una flecha desde el origen hasta un punto representa su vector de posición.

## ¿Cómo se representa?

$$v=\begin{bmatrix}2\\4\\1\end{bmatrix}\in\mathbb{R}^3$$

- `v` es el nombre del vector.
- Los números `2`, `4` y `1` son sus componentes.
- `∈` se lee «pertenece a».
- `ℝ` representa los números reales, como enteros, fracciones y decimales.
- `ℝ³` indica que el vector tiene tres componentes reales; el 3 no pide elevar cada componente al cubo.

En los apuntes se utiliza principalmente la forma **columna**. La forma fila coloca los mismos números horizontalmente. Al multiplicar matrices, esa orientación sí importa.

## Ejemplo paso a paso

Supongamos que las unidades del escenario son metros y que Z representa altura:

1. X = 2: dos metros en la dirección positiva del eje X.
2. Y = 4: cuatro metros en la dirección positiva del eje Y.
3. Z = 1: un metro de altura respecto al origen.

El vector `(4, 2, 1)` describe otra posición: se intercambiaron X e Y.

## ¿Para qué sirve?

Un vector también puede guardar muestras de audio o características de un objeto. Un vector con cien componentes no requiere imaginar cien direcciones físicas: puede ser simplemente una lista de cien mediciones.

## Relación con Inteligencia Artificial

Una observación puede representarse como `(ancho, alto, peso)`. Un modelo recibe esos valores para trabajar con las características del objeto. El orden y las unidades deben mantenerse consistentes. Un *embedding* también es un vector, pero sus componentes son una representación aprendida y no necesariamente tienen nombres intuitivos.

## Comprueba tu comprensión

1. ¿Cuántas componentes tiene un vector de ℝ²?
2. ¿Representan lo mismo `(1, 3)` y `(3, 1)`?

<details>
<summary>Ver respuestas</summary>

1. Dos componentes reales.
2. No: el orden cambió. Si son coordenadas, corresponden a puntos distintos.

</details>

## Lo que aprendí

> Propuesta para adaptar: «Puedo reunir varias cantidades en un vector. Para interpretarlo necesito saber qué significa cada componente y respetar su orden».
