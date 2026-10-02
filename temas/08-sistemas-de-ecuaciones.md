# 8. Sistemas de ecuaciones y Ax = b

[Índice](../README.md) · [Anterior](07-matriz-inversa.md)

## ¿Qué es?

Un sistema de ecuaciones lineales reúne varias condiciones sobre las mismas cantidades desconocidas, llamadas **incógnitas**. Una solución debe cumplir **todas las ecuaciones al mismo tiempo**.

## Entendiendo la idea

Compraste tres artículos entre libretas y lápices. Cada libreta cuesta 10 pesos y cada lápiz 4. Pagaste 18 pesos. Buscamos cuántos artículos compraste de cada tipo.

## ¿Cómo se representa?

Si `x₁` es la cantidad de libretas y `x₂` la cantidad de lápices:

$$\begin{cases}x_1+x_2=3\\10x_1+4x_2=18\end{cases}$$

Es lineal porque las incógnitas aparecen a la primera potencia y multiplicadas por coeficientes conocidos. No hay términos como `x₁²` ni `x₁x₂`.

Podemos reunir la información así:

$$\underbrace{\begin{bmatrix}1&1\\10&4\end{bmatrix}}_{A}\underbrace{\begin{bmatrix}x_1\\x_2\end{bmatrix}}_{x}=\underbrace{\begin{bmatrix}3\\18\end{bmatrix}}_{b}$$

Esto se abrevia **Ax = b**:

- A guarda los coeficientes: cuánto multiplica cada incógnita en cada ecuación.
- x guarda las incógnitas en un vector columna.
- b guarda los valores del lado derecho, llamados términos independientes.

En general, con `m` ecuaciones y `n` incógnitas: A es `m × n`, x es `n × 1` y b es `m × 1`.

## Ejemplo paso a paso

Para comprobar que `x₁ = 1` y `x₂ = 2` es una solución:

1. Cantidad de artículos: `1 + 2 = 3`.
2. Costo: `10·1 + 4·2 = 18`.
3. Ambas condiciones se cumplen: compraste una libreta y dos lápices.

La misma comprobación se escribe:

$$\begin{bmatrix}1&1\\10&4\end{bmatrix}\begin{bmatrix}1\\2\end{bmatrix}=\begin{bmatrix}3\\18\end{bmatrix}$$

El par `(2, 1)` cumple la primera ecuación, pero cuesta 24 pesos, así que **no es solución del sistema**.

## ¿Para qué sirve?

Permite describir varias restricciones simultáneas: cantidades, costos, mezclas o relaciones entre variables. Un sistema puede tener una solución, ninguna o infinitas; tener ecuaciones no garantiza una respuesta única.

Si A es cuadrada e invertible, se puede escribir `x = A⁻¹b`, multiplicando por la inversa a la izquierda. Si A no es invertible, esa fórmula no se puede usar. En esta guía nos concentramos en plantear y comprobar el sistema, como muestran las fotografías.

## Relación con Inteligencia Artificial

Las matrices permiten escribir relaciones entre características y resultados de manera compacta. Con datos reales puede no existir una igualdad exacta para todas las observaciones; entonces otros métodos buscan aproximaciones. Eso queda fuera del alcance de estos apuntes.

## Comprueba tu comprensión

1. ¿Es suficiente cumplir solo una ecuación?
2. Si hay cuatro ecuaciones y dos incógnitas, ¿qué tamaño tiene A?

<details>
<summary>Ver respuestas</summary>

1. No: la solución debe cumplirlas todas.
2. `4 × 2`: una fila por ecuación y una columna por incógnita.

</details>

## Lo que aprendí

> Propuesta para adaptar: «Ax = b es una manera ordenada de escribir varias ecuaciones. Una solución funciona en todas ellas; comprobar solo una no basta».
