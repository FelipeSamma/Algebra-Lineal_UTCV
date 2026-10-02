# 4. Suma y resta de matrices

[Índice](../README.md) · [Anterior](03-matrices.md) · [Siguiente](05-multiplicacion-de-matrices.md)

## ¿Qué es?

Sumar o restar matrices significa operar los números que ocupan la misma posición. **Ambas matrices deben tener exactamente las mismas dimensiones.**

## Entendiendo la idea

Si dos tablas registran las ventas de los mismos productos en las mismas tiendas, podemos sumar las ventas correspondientes. Para interpretar correctamente el resultado, también debemos respetar el significado y las unidades de cada posición.

## ¿Cómo se representa?

$$c_{ij}=a_{ij}+b_{ij}\qquad d_{ij}=a_{ij}-b_{ij}$$

Cada entrada del resultado se obtiene de las entradas ubicadas en la misma fila `i` y columna `j` de las matrices originales. El tamaño no cambia.

## Ejemplo paso a paso

Se retoma el ejemplo visible en las diapositivas:

$$A=\begin{bmatrix}2&0\\1&3\end{bmatrix},\quad B=\begin{bmatrix}1&4\\-2&1\end{bmatrix}$$

$$A+B=\begin{bmatrix}2+1&0+4\\1+(-2)&3+1\end{bmatrix}=\begin{bmatrix}3&4\\-1&4\end{bmatrix}$$

$$A-B=\begin{bmatrix}2-1&0-4\\1-(-2)&3-1\end{bmatrix}=\begin{bmatrix}1&-4\\3&2\end{bmatrix}$$

En la segunda fila y primera columna, restar `−2` equivale a sumar 2: `1 − (−2) = 3`.

## ¿Para qué sirve?

Permite reunir cantidades o comparar cambios entre dos registros. Matemáticamente, una matriz de `2 × 3` no se suma a otra de `3 × 2`, aunque ambas tengan seis números.

En los apuntes aparece `A − B = A + (−1)B`: multiplicar una matriz por `−1` cambia el signo de **cada entrada**, y después se suma.

## Relación con Inteligencia Artificial

Podemos calcular diferencias entre dos matrices de predicciones del mismo tamaño, siempre que sus entradas correspondan a los mismos casos y variables.

## Comprueba tu comprensión

1. ¿Se puede sumar una matriz `2 × 2` con una `2 × 3`?
2. Si dos entradas correspondientes son 5 y −3, ¿cuánto vale su diferencia `5 − (−3)`?

<details>
<summary>Ver respuestas</summary>

1. No: sus dimensiones son distintas.
2. Ocho.

</details>

## Lo que aprendí

> Propuesta para adaptar: «Sumo o resto entrada por entrada y reviso las dimensiones antes de empezar. Debo prestar atención al restar números negativos».
