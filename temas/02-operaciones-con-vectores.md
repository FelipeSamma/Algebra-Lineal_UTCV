# 2. Suma y multiplicación por un escalar

[Índice](../README.md) · [Anterior](01-vectores.md) · [Siguiente](03-matrices.md)

## ¿Qué es?

Sumar vectores consiste en sumar sus componentes correspondientes. Multiplicar por un **escalar** significa multiplicar cada componente por un mismo número.

## Entendiendo la idea

Si un personaje camina dos unidades hacia la derecha y luego una más, en total avanzó tres en esa dirección. Si también cambia de altura, calculamos ese cambio por separado. La suma reúne ambos movimientos.

Un escalar funciona como un factor: `2` duplica un desplazamiento; `0.5` lo reduce a la mitad; `−1` invierte su sentido.

## ¿Cómo se representa?

$$u+v=(u_1+v_1,\ldots,u_n+v_n)$$

$$\lambda v=(\lambda v_1,\ldots,\lambda v_n)$$

El subíndice indica la posición de la componente. Los puntos significan «continúa de la misma manera». La letra griega λ, llamada lambda, representa el escalar. Para sumar, ambos vectores deben tener el mismo número de componentes.

## Ejemplo paso a paso

Con los valores de los apuntes, sean `u = (1, 2, −1)` y `v = (3, −1, 2)`:

| Componente | Operación | Resultado |
|---|---|---|
| Primera | 1 + 3 | 4 |
| Segunda | 2 + (−1) | 1 |
| Tercera | −1 + 2 | 1 |

Por tanto, `u + v = (4, 1, 1)`.

Ahora multiplicamos `u` por 2:

$$2u=(2\cdot1,2\cdot2,2\cdot(-1))=(2,4,-2)$$

El símbolo `·` significa multiplicación. Con `−1` obtendríamos `(−1, −2, 1)`; con `0`, el vector cero `(0, 0, 0)`.

## ¿Para qué sirve?

Permite combinar desplazamientos o cambiar su tamaño. Para un vector no nulo, un escalar positivo conserva su sentido y uno negativo lo invierte. Su longitud se multiplica por el valor absoluto del escalar. El vector cero no tiene una dirección definida.

Si multiplicas un vector de posición por 2, duplicas la distancia de ese punto al origen; eso no equivale automáticamente a duplicar el tamaño de un objeto alrededor de su propio centro.

## Relación con Inteligencia Artificial

Se pueden combinar vectores de características con distintos factores. Por ejemplo, `0.5u + 0.5v` es su promedio componente a componente, siempre que las componentes representen características compatibles.

## Comprueba tu comprensión

1. ¿Cuánto es `(2, 1) + (−1, 3)`?
2. ¿Cuánto es `3(1, −2)`?

<details>
<summary>Ver respuestas</summary>

1. `(1, 4)`.
2. `(3, −6)`; se multiplican ambas componentes.

</details>

## Lo que aprendí

> Propuesta para adaptar: «Para sumar, junto las componentes que ocupan el mismo lugar. Un escalar modifica todas las componentes, no solamente la primera».
