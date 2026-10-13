# 10. Cálculo diferencial: de la pendiente al gradiente

[Volver al índice](../README.md) · [Repasar álgebra lineal](09-ampliacion-algebra-lineal.md)

Este capítulo desarrolla las páginas 9–15 del PDF proporcionado. Conserva la numeración de ejercicios de la recopilación y explica los pasos intermedios.

## Derivada: cambio instantáneo

La derivada describe cómo cambia una función cuando cambia su entrada. Geométricamente, es la pendiente de la recta tangente. Se define por:

$$f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h.$$

El cociente mide el cambio promedio en un intervalo; el límite hace que ese intervalo se acerque a cero. Se simplifica con $h\ne0$ antes de tomar el límite.

### Ejercicio 11. Derivada por definición

Sea $f(x)=x^2+5x$. Primero sustituimos $a+h$:

$$f(a+h)=a^2+2ah+h^2+5a+5h.$$

Restamos $f(a)=a^2+5a$ y dividimos entre $h$:

$$\frac{f(a+h)-f(a)}h=\frac{2ah+h^2+5h}h=2a+h+5.$$

Al tomar el límite obtenemos $f'(a)=2a+5$, o bien $f'(x)=2x+5$. Sustituir directamente $h=0$ antes de simplificar produciría una división indefinida.

## Reglas básicas

| Función | Derivada |
|---|---|
| Constante $k$ | $0$ |
| $x^n$ | $nx^{n-1}$, donde la función y la regla sean aplicables |
| $e^x$ | $e^x$ |
| $\ln x$ | $1/x$, para $x>0$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |

Las reglas trigonométricas se expresan con el argumento en **radianes**. La derivada de una suma es la suma de las derivadas, y los factores constantes se conservan.

### Ejercicio 9a. Potencias negativas y raíz

$$f(x)=4x^5-3x^{-2}+2\sqrt{x}.$$

Escribimos $\sqrt{x}=x^{1/2}$ y derivamos término a término:

$$f'(x)=20x^4+6x^{-3}+x^{-1/2}=20x^4+\frac6{x^3}+\frac1{\sqrt{x}},\qquad x>0.$$

El signo del segundo término cambia porque $(-3)(-2)=6$. El exponente original es **$-2$**, no $2$. La función original exige $x>0$ por la raíz y la potencia negativa.

## Puntos críticos y extremos

Un número crítico pertenece al dominio de la función y cumple $f'(x)=0$ o tiene derivada inexistente. Los puntos donde $f'=0$ son estacionarios; no todos son máximos o mínimos. Para clasificarlos podemos observar el signo de la derivada a cada lado.

### Ejemplo de los apuntes

$$f(x)=\frac13x^3-2x^2+3x+1,$$
$$f'(x)=x^2-4x+3=(x-1)(x-3).$$

Los candidatos son $x=1$ y $x=3$:

| Intervalo | Signo de $f'$ | Comportamiento de $f$ |
|---|---|---|
| $x<1$ | Positivo | Crece |
| $1<x<3$ | Negativo | Decrece |
| $x>3$ | Positivo | Crece |

Por ello, $(1,7/3)$ es un máximo local y $(3,1)$ es un mínimo local. Son extremos **locales**, no absolutos en toda la recta real. Como contraste, $x^3$ tiene derivada cero en $x=0$, pero no tiene un extremo allí.

## Regla del producto

$$(uv)'=u'v+uv'.$$

Se deriva un factor a la vez y se suman los dos términos; no basta multiplicar las derivadas.

### Ejercicio 9b

Para $f(x)=x^2\cos x$, elegimos $u=x^2$ y $v=\cos x$:

$$u'=2x,\quad v'=-\sin x,\qquad f'(x)=2x\cos x-x^2\sin x.$$

## Regla del cociente

$$\left(\frac uv\right)'=\frac{u'v-uv'}{v^2},\qquad v\ne0.$$

### Ejercicio 9c

Si $f(x)=\frac{2x-1}{x+3}$, entonces $u'=2$ y $v'=1$:

$$f'(x)=\frac{2(x+3)-(2x-1)}{(x+3)^2}=\frac7{(x+3)^2},\qquad x\ne-3.$$

Los paréntesis evitan perder el signo negativo de todo el segundo producto.

## Regla de la cadena

Cuando una función está dentro de otra, se deriva la exterior conservando la interior y se multiplica por la derivada interior:

$$\frac d{dx}F(g(x))=F'(g(x))g'(x).$$

### Ejercicio 10a

$$f(x)=(x^3+2x)^4.$$

La exterior es elevar a la cuarta; la interior es $g=x^3+2x$, cuya derivada es $3x^2+2$:

$$f'(x)=4(x^3+2x)^3(3x^2+2).$$

### Ejercicio 10b

$$f(x)=e^{3x^2-1},\qquad f'(x)=e^{3x^2-1}(6x)=6xe^{3x^2-1}.$$

La exponencial se conserva y se multiplica por la derivada del exponente.

### Ejercicio 10c

$$f(x)=\ln(\sin x),\qquad f'(x)=\frac1{\sin x}\cos x=\frac{\cos x}{\sin x}.$$

Para trabajar con valores reales, el dominio original exige **$\sin x>0$**. Que la expresión de la derivada pueda evaluarse en otros puntos no amplía el dominio de la función original.

## Derivadas parciales

Si una función depende de varias variables, una derivada parcial cambia una variable y mantiene las demás constantes. Los símbolos $f_x$ y $\partial f/\partial x$ expresan la derivada parcial respecto de $x$.

### Ejercicio 12. Derivar respecto de cada variable

$$f(x,y)=2x^3y-4xy^2+y^3.$$

Respecto de $x$, tratamos $y$ como constante:

$$f_x=6x^2y-4y^2.$$

El término $y^3$ se vuelve cero porque no cambia al modificar $x$. Respecto de $y$, tratamos $x$ como constante:

$$f_y=2x^3-8xy+3y^2.$$

Aquí $2x^3y$ aporta $2x^3$: sí contiene la variable que estamos derivando.

## Gradiente

El gradiente reúne las derivadas parciales en un vector:

$$\nabla f(x,y)=\begin{pmatrix}f_x(x,y)\\f_y(x,y)\end{pmatrix}.$$

En un punto donde la función es diferenciable y el gradiente no es cero, este señala la dirección de mayor aumento local. Su opuesto señala la de mayor descenso local. Si el gradiente es cero, este criterio de primer orden no da una dirección única ni demuestra por sí solo que haya un mínimo.

### Ejercicio 12. Evaluar en $(1,-1)$

$$f_x(1,-1)=6(1)^2(-1)-4(-1)^2=-10,$$
$$f_y(1,-1)=2(1)^3-8(1)(-1)+3(-1)^2=13.$$

Por tanto:

$$\nabla f(1,-1)=\begin{pmatrix}-10\\13\end{pmatrix}.$$

### Ejercicio 13. Logaritmo de una función de dos variables

$$f(x,y)=\ln(x^2+4y),\qquad x^2+4y>0.$$

Aplicamos la cadena a cada variable:

$$f_x=\frac{2x}{x^2+4y},\qquad f_y=\frac4{x^2+4y},$$
$$\nabla f(x,y)=\begin{pmatrix}\frac{2x}{x^2+4y}\\[3pt]\frac4{x^2+4y}\end{pmatrix}.$$

## Relación con inteligencia artificial

Una función de pérdida mide el error de un modelo. Sus derivadas indican cómo cambia ese error al ajustar los parámetros; el gradiente reúne esos cambios. Esto ayuda a entender la idea del descenso de gradiente. Es una conexión conceptual: este repositorio no implementa ni entrena modelos.

## Formulario de repaso

| Idea | Fórmula o criterio |
|---|---|
| Derivada por definición | $\lim_{h\to0}[f(x+h)-f(x)]/h$ |
| Producto | $(uv)'=u'v+uv'$ |
| Cociente | $(u/v)'=(u'v-uv')/v^2$ |
| Cadena | $(F\circ g)'=F'(g)g'$ |
| Gradiente en dos variables | $\nabla f=(f_x,f_y)^T$ |
| Máximo local por cambio de signo | $f'$ cambia de positivo a negativo |
| Mínimo local por cambio de signo | $f'$ cambia de negativo a positivo |

## Comprueba tu comprensión

1. ¿Por qué no sustituimos $h=0$ al comenzar la definición?
2. ¿Qué pasa con $y^3$ al derivar respecto de $x$?
3. ¿Qué factor falta si se deriva $e^{3x^2-1}$ como solo $e^{3x^2-1}$?
4. ¿Todo punto con derivada cero es un extremo?
5. ¿Qué dominio real tiene $\ln(x^2+4y)$?
6. ¿Cuál es la diferencia entre una parcial y el gradiente?

<details><summary>Respuestas</summary>

1. Aparecería una división entre cero; primero simplificamos para $h\ne0$ y después tomamos el límite.
2. Su derivada parcial es cero, porque $y$ permanece constante.
3. La derivada interior $6x$.
4. No. Se necesita clasificarlo; $x^3$ en cero es un contraejemplo.
5. Los puntos donde $x^2+4y>0$.
6. Una parcial mide el cambio respecto de una variable; el gradiente reúne todas las parciales en un vector.

</details>

## Lo que aprendí — propuesta para adaptar

Entiendo la derivada como una medida de cambio. Puedo elegir entre las reglas básicas, producto, cociente y cadena, revisar el dominio y calcular parciales. El gradiente conecta estas ideas con funciones que dependen de varias variables.
