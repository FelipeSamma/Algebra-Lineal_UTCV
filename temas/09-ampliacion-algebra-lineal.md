# 09. Ampliación de álgebra lineal

[Volver al índice](../README.md) · [Continuar con cálculo](10-calculo-diferencial.md)

Este capítulo desarrolla el material del PDF *Apuntes completos: Matemáticas para IA*, páginas 3–9. Los números de ejercicio son los que aparecen en esa recopilación.

## Vectores, espacios y combinaciones lineales

Un vector es una lista ordenada de componentes. Un espacio vectorial es un conjunto de vectores con operaciones de suma y multiplicación por escalares que cumplen propiedades como asociatividad, distributividad, existencia del cero y de inversos aditivos. Son conceptos relacionados, pero distintos. Por ejemplo, en $\mathbb R^3$ la suma y el producto por un número real producen otro vector del mismo espacio:

$$
(1,2,-1)+(3,-1,2)=(4,1,1),\qquad 2(1,2,-1)=(2,4,-2).
$$

Una **combinación lineal** multiplica vectores por escalares y suma los resultados:

$$c_1v_1+c_2v_2+\cdots+c_nv_n.$$

Si $v_1=(2,1)$ y $v_2=(-1,3)$, entonces:

$$3v_1-2v_2=(6,3)-(-2,6)=(8,-3).$$

La multiplicación matricial también puede verse como una combinación de columnas:

$$
\begin{pmatrix}1&4\\2&-3\end{pmatrix}\begin{pmatrix}3\\1\end{pmatrix}
=3\begin{pmatrix}1\\2\end{pmatrix}+\begin{pmatrix}4\\-3\end{pmatrix}
=\begin{pmatrix}7\\3\end{pmatrix}.
$$

Así, resolver $Ax=b$ equivale a buscar los coeficientes que combinan las columnas de $A$ para obtener $b$.

## Espacio nulo y solución general

El **espacio nulo**, o núcleo, reúne todos los vectores que la matriz transforma en cero:

$$N(A)=\{x:Ax=0\}.$$

Para $B=\begin{pmatrix}1&2\\2&4\end{pmatrix}$, las ecuaciones de $Bx=0$ se reducen a $x_1+2x_2=0$. Tomando $x_2=t$:

$$x=t\begin{pmatrix}-2\\1\end{pmatrix},\qquad t\in\mathbb R.$$

No es solo un vector: todos sus múltiplos forman el núcleo. El vector cero siempre pertenece a él.

Cuando $Ax=b$ tiene solución, cualquier solución se escribe como:

$$x=x_p+x_h,\qquad Ax_p=b,\quad Ax_h=0.$$

La solución particular $x_p$ llega hasta $b$; sumar una solución homogénea no cambia ese resultado porque $A(x_p+x_h)=b+0$.

## Eliminación de Gauss

Gauss simplifica un sistema mediante operaciones que conservan sus soluciones:

1. Intercambiar dos filas.
2. Multiplicar una fila por un número distinto de cero.
3. Sumar a una fila un múltiplo de otra.

Se trabaja con la matriz aumentada $[A\mid b]$, aplicando cada operación también a la columna de resultados. Un **pivote** es el primer elemento no nulo de una fila en forma escalonada. Las variables sin pivote son libres.

Por ejemplo, en $x+2y=3$, $4x+5y=6$, restar la segunda ecuación a cuatro veces la primera da $3y=6$. Por tanto, $y=2$ y $x=-1$; ambos valores satisfacen las dos ecuaciones.

### Ejercicio 1. Sistema con infinitas soluciones

$$
\begin{cases}x_1+2x_2+x_3=1\\2x_1+4x_2+3x_3=4\end{cases}
$$

Aplicamos $F_2\leftarrow F_2-2F_1$:

$$
\left[\begin{array}{ccc|c}1&2&1&1\\2&4&3&4\end{array}\right]
\longrightarrow
\left[\begin{array}{ccc|c}1&2&1&1\\0&0&1&2\end{array}\right].
$$

La segunda fila indica $x_3=2$. La primera queda $x_1+2x_2=-1$. Como $x_2$ es libre, escribimos $x_2=t$:

$$
x=\begin{pmatrix}-1-2t\\t\\2\end{pmatrix}
=\underbrace{\begin{pmatrix}-1\\0\\2\end{pmatrix}}_{x_p}
+t\underbrace{\begin{pmatrix}-2\\1\\0\end{pmatrix}}_{\text{dirección del núcleo}},\quad t\in\mathbb R.
$$

**Comprobación:** la primera ecuación da $(-1-2t)+2t+2=1$; la segunda da $2(-1-2t)+4t+6=4$ para cualquier $t$.

Para distinguir resultados, una fila $[0\;0\;0\mid c]$ con $c\ne0$ significa que no hay solución. Si el sistema es compatible y tiene variables libres, hay infinitas soluciones. Si es compatible y todas las variables tienen pivote, la solución es única. En dos ecuaciones que representan rectas del plano, esto corresponde a rectas paralelas distintas, coincidentes o que se cruzan, respectivamente.

## Dependencia e independencia lineal

Los vectores son **linealmente dependientes** si existe una combinación igual a cero cuyos coeficientes no sean todos cero. Son independientes si la única forma de obtener cero usa todos los coeficientes iguales a cero.

### Ejercicio 3. Comprobar dependencia con Gauss

$$v_1=(1,2,1),\quad v_2=(2,1,0),\quad v_3=(0,3,2).$$

Colocamos los vectores como columnas y resolvemos $Ac=0$:

$$
A=\begin{pmatrix}1&2&0\\2&1&3\\1&0&2\end{pmatrix}
\longrightarrow
\begin{pmatrix}1&2&0\\0&-3&3\\0&-2&2\end{pmatrix}
\longrightarrow
\begin{pmatrix}1&2&0\\0&-3&3\\0&0&0\end{pmatrix}.
$$

Las primeras operaciones son $F_2\leftarrow F_2-2F_1$ y $F_3\leftarrow F_3-F_1$; la última es $F_3\leftarrow F_3-\frac23F_2$.

Resulta $c_2=c_3$ y $c_1=-2c_2$. Una elección no trivial es $(c_1,c_2,c_3)=(2,-1,-1)$:

$$2v_1-v_2-v_3=(0,0,0).$$

Por tanto, son dependientes. El criterio general es comprobar si hay pivote en cada **columna**. Una fila cero por sí sola no prueba dependencia de columnas en cualquier matriz rectangular.

## Ejercicio 5. Operaciones y transpuesta

Con $A=\begin{pmatrix}1&2\\0&-1\end{pmatrix}$ y $B=\begin{pmatrix}3&1\\2&4\end{pmatrix}$:

$$A+B=\begin{pmatrix}4&3\\2&3\end{pmatrix},\qquad AB=\begin{pmatrix}7&9\\-2&-4\end{pmatrix}.$$

Por ejemplo, la entrada superior derecha de $AB$ es $1(1)+2(4)=9$.

$$
(AB)^T=\begin{pmatrix}7&-2\\9&-4\end{pmatrix},\qquad
A^TB^T=\begin{pmatrix}3&2\\5&0\end{pmatrix}.
$$

Son diferentes: al transponer un producto se invierte el orden:

$$(AB)^T=B^TA^T.$$

Consulta también [identidad y transpuesta](06-identidad-y-transpuesta.md).

## Norma, producto punto y ángulo

La **norma euclidiana** mide la longitud de un vector:

$$\|u\|=\sqrt{u_1^2+\cdots+u_n^2}.$$

El **producto punto** multiplica componentes correspondientes y suma:

$$u\cdot v=u_1v_1+\cdots+u_nv_n.$$

Para dos vectores distintos de cero, el ángulo entre ellos satisface:

$$\cos\theta=\frac{u\cdot v}{\|u\|\|v\|}.$$

### Ejercicio 7a y 7b

Sean $u=(3,4,0)$ y $v=(1,0,0)$:

$$\|u\|=\sqrt{9+16}=5,\qquad\|v\|=1,$$
$$u\cdot v=3(1)+4(0)+0(0)=3,$$
$$\theta=\arccos\left(\frac35\right)\approx0.9273\text{ rad}\approx53.13^\circ.$$

La función $\arccos$ recupera el ángulo; no significa $1/\cos$. Revisa si tu calculadora muestra grados o radianes. El ángulo con el vector cero no está definido mediante esta fórmula.

## Matrices ortogonales

Una matriz real cuadrada es **ortogonal** si $R^TR=RR^T=I$. Por ello, $R^{-1}=R^T$: la transpuesta deshace la transformación. Sus columnas son ortonormales, es decir, tienen longitud uno y son perpendiculares entre sí. Estas matrices conservan longitudes y ángulos.

### Ejercicio 7c. Rotación de 30 grados

Con $c=\cos30^\circ=\sqrt3/2$ y $s=\sin30^\circ=1/2$:

$$R=\begin{pmatrix}c&-s\\s&c\end{pmatrix},\qquad R^T=\begin{pmatrix}c&s\\-s&c\end{pmatrix}.$$

$$
RR^T=\begin{pmatrix}c^2+s^2&cs-sc\\sc-cs&s^2+c^2\end{pmatrix}
=\begin{pmatrix}1&0\\0&1\end{pmatrix}.
$$

Los términos fuera de la diagonal se cancelan. **No se debe suponer que $\sin30^\circ=0$**: vale $1/2$.

## Relación con inteligencia artificial

Los vectores pueden representar características de datos; el producto punto y el ángulo ayudan a comparar sus direcciones. La dependencia indica que ciertos vectores pueden expresarse mediante otros. Estas conexiones son explicaciones didácticas, no prácticas de programación realizadas en clase.

## Comprueba tu comprensión

1. ¿Por qué sumar un vector del núcleo a una solución particular conserva $Ax=b$?
2. ¿Es suficiente usar todos los coeficientes cero para demostrar dependencia?
3. ¿Cuál es la transpuesta de $AB$?
4. ¿Qué condición necesitan los vectores para calcular el ángulo con la fórmula anterior?

<details><summary>Respuestas</summary>

1. Porque el vector añadido se transforma en cero.
2. No. Al menos un coeficiente debe ser distinto de cero.
3. $B^TA^T$.
4. Ambos deben ser distintos de cero.

</details>

## Lo que aprendí — propuesta para adaptar

Puedo interpretar un sistema como una combinación de columnas y usar Gauss para encontrar sus soluciones. También distingo entre longitud, producto punto y ángulo, y entiendo por qué una rotación conserva las longitudes.
