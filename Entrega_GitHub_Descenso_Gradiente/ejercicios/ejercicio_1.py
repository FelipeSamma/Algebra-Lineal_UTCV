"""Matemáticas para IA — Ejercicios de descenso del gradiente (1 al 6).

Requiere numpy y matplotlib. Ejecutable en Colab/Jupyter o como script:
    python ejercicios/ejercicio_1.py

Mantiene las tasas iniciales sugeridas en ejercicios 1-3, y prueba parámetros
para 4-6. Registra la norma del gradiente y detiene en ||grad|| < 1e-6.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

TOL = 1e-6
OUTPUT = Path('graficas')
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


assert c1 and h1[-1]["norma"] < TOL

if __name__ == "__main__":
    print("Programa ejecutado correctamente.")
