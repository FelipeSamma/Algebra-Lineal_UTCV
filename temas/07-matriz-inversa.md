# 7. Matriz inversa

[Índice](../README.md) · [Anterior](06-identidad-y-transpuesta.md) · [Siguiente](08-sistemas-de-ecuaciones.md)

## ¿Qué es?

La inversa de una matriz cuadrada A es otra matriz que cumple:

$$AA^{-1}=A^{-1}A=I$$

`A⁻¹` se lee «A inversa». No significa dividir 1 entre cada entrada. **No toda matriz cuadrada tiene inversa.**

## Entendiendo la idea

Si una operación duplica un número, dividir entre 2 deshace el cambio. Una matriz inversa hace algo semejante con una transformación de vectores. Pero si una transformación borra información, no podemos recuperar una única entrada original.

Por ejemplo, convertir cualquier `(x, y)` en `(x, 0)` pierde el valor de y. Varias entradas producen la misma salida: no hay una inversa que recupere cuál era la original.

## ¿Cómo se representa?

Para una matriz `2 × 2`:

$$A=\begin{bmatrix}a&b\\c&d\end{bmatrix},\quad A^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$$

Esto requiere `ad − bc ≠ 0`. El número `ad − bc` es el **determinante** de esta matriz. Aquí solo usamos el caso `2 × 2` presente en los apuntes; no aplicamos esta fórmula a matrices mayores.

## Ejemplo paso a paso

$$A=\begin{bmatrix}2&1\\1&1\end{bmatrix}$$

1. Calculamos `ad − bc = 2·1 − 1·1 = 1`.
2. Como no es cero, la inversa existe.
3. Intercambiamos a y d, y cambiamos los signos de b y c.
4. Multiplicamos todas las entradas por `1/1`.

$$A^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$$

Comprobamos con fila por columna:

$$AA^{-1}=\begin{bmatrix}2-1&-2+2\\1-1&-1+2\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$$

En cambio, para `[[1, 2], [2, 4]]`, el determinante es `1·4 − 2·2 = 0`: no existe inversa.

## Vocabulario y propiedades de los apuntes

- **Invertible, regular o no singular:** tiene inversa.
- **Singular:** no tiene inversa.
- Si existe, la inversa es única.
- Para A y B cuadradas e invertibles, `(AB)⁻¹ = B⁻¹A⁻¹`: se deshacen las operaciones en orden inverso.
- `(Aᵀ)⁻¹ = (A⁻¹)ᵀ` cuando A es invertible.
- En general, `(A + B)⁻¹` no es `A⁻¹ + B⁻¹`, aun cuando todas esas inversas existan.

## ¿Para qué sirve?

Permite recuperar un vector anterior a una transformación invertible y resolver ciertos sistemas de ecuaciones. Escalar una coordenada por cero pierde información; ese escalado no es invertible.

## Relación con Inteligencia Artificial

La inversa aparece en algunas formulaciones algebraicas para estimar parámetros. En cálculos reales no siempre se construye explícitamente: existen métodos para resolver el sistema directamente. Aquí estudiamos su significado matemático.

## Comprueba tu comprensión

1. ¿Toda matriz cuadrada tiene inversa?
2. ¿Cuál es la inversa de `[[2, 0], [0, 2]]`?

<details>
<summary>Ver respuestas</summary>

1. No. En el caso `2 × 2`, no la tiene si su determinante es cero.
2. `[[0.5, 0], [0, 0.5]]`; su producto da la identidad.

</details>

## Lo que aprendí

> Propuesta para adaptar: «La inversa permite deshacer una transformación cuando no se ha perdido información. Primero reviso si existe y luego verifico que el producto dé la identidad».
