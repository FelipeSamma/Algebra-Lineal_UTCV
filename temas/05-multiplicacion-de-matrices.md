# 5. Multiplicación de matrices

[Índice](../README.md) · [Anterior](04-suma-y-resta-de-matrices.md) · [Siguiente](06-identidad-y-transpuesta.md)

## ¿Qué es?

El producto matricial combina **una fila de la primera matriz con una columna de la segunda**. Multiplicamos los números correspondientes y sumamos esos productos para obtener una entrada.

## Entendiendo la idea

Una compra tiene cantidades y precios: si compras dos libretas a 10 pesos y tres lápices a 4 pesos, pagas `2·10 + 3·4 = 32`. Multiplicar una fila por una columna sigue esa misma lógica.

## ¿Cómo se representa?

$$A_{m\times n}B_{n\times p}=C_{m\times p}$$

Las columnas de A deben coincidir en cantidad con las filas de B. El resultado conserva las filas de A y las columnas de B. Por ejemplo, `(2 × 3)(3 × 4)` produce una matriz `2 × 4`.

La fórmula general es:

$$c_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj}$$

`Σ` significa sumar. `k` recorre las parejas de números de la fila `i` de A y la columna `j` de B. No necesitas memorizar ese símbolo para empezar: recuerda **multiplicar parejas y sumar resultados**.

## Ejemplo paso a paso

$$A=\begin{bmatrix}1&2\\3&4\end{bmatrix},\quad B=\begin{bmatrix}2&0\\1&2\end{bmatrix}$$

| Entrada | Fila de A por columna de B | Resultado |
|---|---|---|
| Primera fila, primera columna | 1·2 + 2·1 | 4 |
| Primera fila, segunda columna | 1·0 + 2·2 | 4 |
| Segunda fila, primera columna | 3·2 + 4·1 | 10 |
| Segunda fila, segunda columna | 3·0 + 4·2 | 8 |

$$AB=\begin{bmatrix}4&4\\10&8\end{bmatrix}$$

Si cambiamos el orden:

$$BA=\begin{bmatrix}2&4\\7&10\end{bmatrix}$$

Por tanto, `AB ≠ BA`. Se dice que el producto de matrices **no es conmutativo en general**. Algunas matrices sí conmutan, pero no debemos suponerlo. Incluso puede existir AB y no existir BA por sus dimensiones.

## ¿Para qué sirve?

En 3D sirve para componer transformaciones. Escalar y después girar no siempre produce el mismo resultado que girar y después escalar. Con vectores columna, en `ABv` se aplica primero B y luego A.

## Relación con Inteligencia Artificial

Una matriz puede combinar características con distintos pesos. Cada salida suma varias entradas multiplicadas por sus factores, como en el ejemplo de cantidades y precios.

## Comprueba tu comprensión

1. ¿Qué tamaño produce `(3 × 2)(2 × 1)`?
2. ¿Cuánto vale el producto de la fila `(2, 3)` por la columna `(4, 1)`?

<details>
<summary>Ver respuestas</summary>

1. `3 × 1`.
2. `2·4 + 3·1 = 11`.

</details>

## Lo que aprendí

> Propuesta para adaptar: «Antes de multiplicar reviso las dimensiones. Cada resultado sale de una fila por una columna, y cambiar el orden puede cambiar el resultado».
