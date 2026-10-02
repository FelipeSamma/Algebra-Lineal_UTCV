# 3. Matrices y dimensiones

[Índice](../README.md) · [Anterior](02-operaciones-con-vectores.md) · [Siguiente](04-suma-y-resta-de-matrices.md)

## ¿Qué es?

Una matriz es un arreglo rectangular de números organizado en **filas y columnas**. Las filas son horizontales y las columnas verticales.

## Entendiendo la idea

Podemos guardar las coordenadas de dos objetos en una tabla. Cada fila representa un objeto; cada columna, una coordenada. Los títulos ayudan a interpretar los números, aunque no forman parte de la matriz numérica.

| Objeto | X | Y | Z |
|---|---|---|---|
| A | 2 | 4 | 1 |
| B | 5 | 0 | 3 |

## ¿Cómo se representa?

$$M=\begin{bmatrix}2&4&1\\5&0&3\end{bmatrix}\in\mathbb{R}^{2\times3}$$

El tamaño siempre se indica como **filas × columnas**. Esta matriz es de `2 × 3`, con seis entradas en total. En general, `aᵢⱼ` indica el número de la fila `i` y la columna `j`, contando desde 1 en esta notación.

## Ejemplo paso a paso

Para encontrar `m₂₃`:

1. El primer subíndice, 2, nos lleva a la segunda fila: `(5, 0, 3)`.
2. El segundo, 3, nos lleva al tercer número de esa fila.
3. Por tanto, `m₂₃ = 3`.

Una matriz de `1 × n` puede representar un vector fila; una de `m × 1`, un vector columna. Una matriz es **cuadrada** cuando tiene igual cantidad de filas y columnas, por ejemplo `2 × 2`.

## ¿Para qué sirve?

Organiza mediciones, coordenadas y coeficientes de ecuaciones. También permite representar transformaciones, aunque una tabla de posiciones y una matriz que transforma posiciones cumplen funciones distintas.

## Relación con Inteligencia Artificial

Un conjunto de datos puede representarse mediante una matriz: cada fila es una observación y cada columna una característica. Por ejemplo, cien objetos con tres mediciones forman una matriz de `100 × 3`.

## Comprueba tu comprensión

1. ¿Cuántas entradas tiene una matriz de `3 × 2`?
2. En la matriz del ejemplo, ¿cuánto vale `m₁₂`?

<details>
<summary>Ver respuestas</summary>

1. Seis: tres filas con dos números en cada una.
2. Vale 4: primera fila, segunda columna.

</details>

## Lo que aprendí

> Propuesta para adaptar: «Una matriz organiza números. Primero cuento filas y después columnas; los subíndices me dicen dónde encontrar cada entrada».
