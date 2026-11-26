"""Matemáticas para IA — Ejercicios de descenso del gradiente (1 al 6).

Requiere numpy y matplotlib. Ejecutable en Colab/Jupyter o como script:
    python ejercicios_1_a_6.py

Mantiene las tasas iniciales sugeridas en ejercicios 1-3, y prueba parámetros
para 4-6. Registra la norma del gradiente y detiene en ||grad|| < 1e-6.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

TOL = 1e-6
OUTPUT = Path(__file__).resolve().parent / 'graficas'
OUTPUT.mkdir(exist_ok=True)


def descenso(f, grad, x0, gamma, alpha=0.0, tol=TOL, max_iter=100000):
    """Descenso clásico (alpha=0) o con momento clásico (alpha>0).
    Cada registro (i, x, grad, f, norma) describe el estado ANTES de actualizar.
    """
    x = np.asarray(x0, dtype=float).reshape(-1)
    anterior = x.copy()
    historia = []
    convergio = False
    for i in range(max_iter + 1):
        g = np.asarray(grad(x), dtype=float).reshape(-1)
        fx = float(f(x))
        norma = float(np.linalg.norm(g))
        if not (np.all(np.isfinite(g)) and np.isfinite(fx) and np.all(np.isfinite(x))):
            break
        historia.append({'i': i, 'x': x.copy(), 'grad': g.copy(), 'f': fx, 'norma': norma,
                         'delta': x-anterior if i else np.zeros_like(x)})
        if norma < tol:
            convergio = True
            break
        if i == max_iter:
            break
        nuevo = x - gamma*g + alpha*(x-anterior)
        anterior, x = x, nuevo
        if np.max(np.abs(x)) > 1e50:
            break
    return historia, convergio


def informe(titulo, historia, convergio, gamma, alpha=0.0, filas=4):
    print('\n' + '='*65)
    print(titulo)
    print(f'gamma={gamma}, alpha={alpha}, convergencia={convergio}')
    print('Iteración | x | gradiente | f(x) | norma')
    for r in historia[:filas]:
        print(r['i'], np.round(r['x'], 8), np.round(r['grad'], 8),
              round(r['f'], 9), f"{r['norma']:.4e}")
    if historia:
        r = historia[-1]
        print(f"FINAL: i={r['i']}, x={r['x']}, f={r['f']:.12g}, "+
              f"grad={r['grad']}, ||grad||={r['norma']:.4e}")


def grafica(historia, nombre, titulo, log=False, otras=None):
    plt.figure(figsize=(8, 4.5))
    series=[('Descenso',historia)]
    if otras:
        series += otras
    for etiqueta, h in series:
        # Submuestreo para archivos ligeros y gráficas legibles
        saltar = max(1, len(h)//1500)
        registros = h[::saltar]
        if registros[-1] is not h[-1]: registros = registros + [h[-1]]
        yy = np.asarray([r['f'] for r in registros])
        if log:
            yy=np.maximum(yy,1e-18)
        plt.plot([r['i'] for r in registros], yy, label=etiqueta)
    plt.xlabel('Iteración i')
    plt.ylabel('f(x_i)')
    plt.title(titulo)
    if log: plt.yscale('log')
    if len(series)>1: plt.legend()
    plt.grid(True, alpha=.25)
    plt.tight_layout()
    plt.savefig(OUTPUT / nombre, dpi=160)
    plt.close()


# EJERCICIO 1
A1=np.array([[4.,0.],[0.,10.]])
b1=np.array([-8.,10.])
f1=lambda x: .5*float(x@A1@x)-float(b1@x)
g1=lambda x: A1@x-b1
h1,c1=descenso(f1,g1,[0,0],.15)
informe('Ejercicio 1',h1,c1,.15)
assert np.allclose(h1[3]['x'],[-1.872,1.125])
grafica(h1,'e1.png','Ejercicio 1: descenso del gradiente')

# EJERCICIO 2
A2=np.diag([1.,3.,5.])
b2=np.array([-3.,6.,-10.])
f2=lambda x: .5*float(x@A2@x)-float(b2@x)
g2=lambda x: A2@x-b2
h2,c2=descenso(f2,g2,[1,0,1],.25)
informe('Ejercicio 2',h2,c2,.25)
assert np.allclose(h2[3]['x'],[-1.3125,1.96875,-2.046875])
grafica(h2,'e2.png','Ejercicio 2: tres variables')

# EJERCICIO 3 (CON MOMENTO)
f3=lambda x: .25*x[0]**4-2*x[0]**2
g3=lambda x: np.array([x[0]**3-4*x[0]])
h3,c3=descenso(f3,g3,[1],.05,alpha=.5)
informe('Ejercicio 3: momento',h3,c3,.05,alpha=.5)
assert np.allclose(h3[3]['x'],[1.638119957173],atol=1e-10)
grafica(h3,'e3.png','Ejercicio 3: descenso con momento')

# EJERCICIO 4 (4 VARIABLES)
pesos=np.arange(1.,5.)

def f4(x):
    return float(np.sum(pesos*x**4-4*pesos*x)+np.sum(np.diff(x)**2))

def g4(x):
    g=4*pesos*x**3-4*pesos
    d=np.diff(x)
    g[:-1]-=2*d
    g[1:]+=2*d
    return g

print('\nPruebas de tasas ejercicio 4, x0=(0,0,0,0):')
for gamma in (.01,.02,.03,.04):
    h,c=descenso(f4,g4,np.zeros(4),gamma,max_iter=150)
    print(f'gamma={gamma:.3f}, converge antes de 150: {c}, '
          f'iteraciones realizadas: {h[-1]["i"]}, norma final: {h[-1]["norma"]:.6g}')
h4,c4=descenso(f4,g4,[0,0,0,0],.03)
informe('Ejercicio 4: cuatro variables',h4,c4,.03)
grafica(h4,'e4.png','Ejercicio 4: convergencia')

# EJERCICIO 5 (ROSENBROCK, CON / SIN MOMENTO)
def f5(x):
    return float((1-x[0])**2+100*(x[1]-x[0]**2)**2)

def g5(x):
    e=x[1]-x[0]**2
    return np.array([2*(x[0]-1)-400*x[0]*e,200*e])

h5_sin,c5_sin=descenso(f5,g5,[-1.2,1],.001,alpha=0,max_iter=100000)
h5_con,c5_con=descenso(f5,g5,[-1.2,1],.001,alpha=.9,max_iter=100000)
informe('Ejercicio 5: sin momento',h5_sin,c5_sin,.001)
informe('Ejercicio 5: con momento',h5_con,c5_con,.001,alpha=.9)
grafica(h5_con,'e5_comparacion.png','Ejercicio 5: con y sin momento',log=True,
        otras=[('Sin momento',h5_sin)])

# EJERCICIO 6 (NO CONVEXO, MULTIPLES PUNTOS INICIALES)
def f6(x):
    return float(x[0]**4-8*x[0]**2+2*x[0]+(x[1]-x[0])**2)

def g6(x):
    return np.array([4*x[0]**3-16*x[0]+2+2*(x[0]-x[1]),
                     2*(x[1]-x[0])])

all6=[]
for init in [(-3.,-3.),(0.,0.),(3.,3.)]:
    h,c=descenso(f6,g6,init,.04,max_iter=300000)
    informe(f'Ejercicio 6: punto inicial {init}',h,c,.04,filas=2)
    all6.append((f'Inicio {init}',h))
grafica(all6[0][1],'e6_inicios.png','Ejercicio 6: diferentes puntos iniciales',
        otras=all6[1:])

# Prueba de consistencia
for idx,h,c in [(1,h1,c1),(2,h2,c2),(3,h3,c3),(4,h4,c4),
                (5,h5_sin,c5_sin),(5,h5_con,c5_con)]+[(6,h,c) for _,h in all6]:
    assert c, f'Ejercicio {idx}: no alcanzo tolerancia'
    assert h[-1]['norma']<TOL
print('\nTodos los ejercicios alcanzaron ||gradiente|| < 1e-6 en las tasas elegidas.')
print('Gráficas:', OUTPUT)
