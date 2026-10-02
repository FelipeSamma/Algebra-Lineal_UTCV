# 6. Matriz identidad y transpuesta

[Índice](../README.md) · [Anterior](05-multiplicacion-de-matrices.md) · [Siguiente](07-matriz-inversa.md)

## ¿Qué es?

La **identidad** es una matriz cuadrada que tiene unos en la diagonal principal y ceros en las demás posiciones. La **transpuesta** de una matriz se obtiene convirtiendo sus filas en columnas.

## Entendiendo la idea

La identidad cumple un papel parecido al número 1 al multiplicar: deja igual lo que recibe. La transposición reorganiza posiciones: la primera fila se vuelve primera columna, la segunda fila se vuelve segunda columna, y así sucesivamente.

## ¿Cómo se representa?

$$I_2=\begin{bmatrix}1&0\\0&1\end{bmatrix}$$

La diagonal principal va desde la esquina superior izquierda hasta la inferior derecha. El subíndice 2 indica que la identidad es de `2 × 2`.

`Aᵀ` se lee «A transpuesta». La T indica la operación; no es un exponente numérico. Si A tiene tamaño `m × n`, Aᵀ tiene tamaño `n × m`.

## Ejemplo paso a paso

Para `v = (3, 5)` escrito como columna:

$$I_2\begin{bmatrix}3\\5\end{bmatrix}=\begin{bmatrix}1\cdot3+0\cdot5\\0\cdot3+1\cdot5\end{bmatrix}=\begin{bmatrix}3\\5\end{bmatrix}$$

Ahora transpongamos otra matriz:

$$A=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix},\quad A^T=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}$$

La fila `(1, 2, 3)` se convirtió en la primera columna. Ningún número cambió de valor; cambió su ubicación. La matriz pasó de `2 × 3` a `3 × 2`.

## Propiedades de los apuntes, explicadas

Todas estas expresiones requieren dimensiones compatibles:

| Propiedad | Significado |
|---|---|
| IₘA = AIₙ = A, para A de m × n | La identidad conserva A; su tamaño depende del lado |
| (AB)C = A(BC) | Podemos cambiar la agrupación del producto, conservando el orden |
| A(B + C) = AB + AC | El producto se distribuye sobre la suma |
| (A + B)C = AC + BC | También se distribuye cuando la suma está a la izquierda |
| (Aᵀ)ᵀ = A | Transponer dos veces recupera la matriz original |
| (A + B)ᵀ = Aᵀ + Bᵀ | Podemos transponer una suma por separado |
| (AB)ᵀ = BᵀAᵀ | Al transponer un producto, se invierte el orden |
| (λA)ᵀ = λAᵀ | El escalar permanece igual |

No podemos cancelar matrices sin condiciones: `AB = AC` no garantiza `B = C`. Si A es la matriz cero, ambos productos son cero aunque B y C sean distintas.

## ¿Para qué sirve?

La identidad representa una transformación que conserva los vectores. La transpuesta permite cambiar la orientación de los datos para operaciones posteriores. **Transponer no equivale a invertir una matriz.**

## Relación con Inteligencia Artificial

Si una tabla tiene observaciones en filas, su transpuesta coloca esas observaciones en columnas. Es útil cuando una fórmula requiere esa orientación.

## Comprueba tu comprensión

1. ¿Qué tamaño tiene la transpuesta de una matriz `4 × 2`?
2. ¿Cuánto vale `I₂(7, −1)` con el vector escrito como columna?

<details>
<summary>Ver respuestas</summary>

1. `2 × 4`.
2. El mismo vector `(7, −1)`.

</details>

## Lo que aprendí

> Propuesta para adaptar: «La identidad conserva una matriz o vector al multiplicar. La transpuesta intercambia filas y columnas, y no sirve por sí sola para deshacer una transformación».
