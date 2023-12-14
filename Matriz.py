import numpy as np

def jacobi(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s += A[i, j] * x[j]
            x_new[i] = (b[i] - s) / A[i, i]
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s += A[i, j] * x[j]
            x[i] = (b[i] - s) / A[i, i]
        if np.linalg.norm(np.dot(A, x) - b) < tol:
            return x
    return x

# Ejemplo de uso
N = int(input("Tamaño de matriz NxN: "))
A = np.zeros((N,N))
# Se crea la matriz NxN (cuadratica) con todos sus coeficientes en 0
for i in range(N):
    for j in range(N):
        A[i,j] = float(input(f"A[{i},{j}]: "))
b = np.zeros(N)
# Se crea el vector de tamaño N con sus elementos en 0
for i in range(N):
    b[i] = float(input(f"b[{i}]: "))

x = np.linalg.solve(A, b)              
print(x)
x_exact = np.linalg.solve(A, b)           

"""
lo que hace np.linalg.solve() es:
Calcular la inversa de la matriz de coeficientes A
Multiplicar esa matriz inversa A^-1 por el vector b
De esta forma obtiene la solución x = A^-1 * b
"""
x0 = np.zeros_like(b)
tol = 1e-6
max_iter = 1000

x_jacobi = jacobi(A, b, x0, tol, max_iter)
x_gauss_seidel = gauss_seidel(A, b, x0, tol, max_iter)

print("Solución exacta:", x_exact)
print("Solución Jacobi:", x_jacobi)
print("Solución Gauss-Seidel:", x_gauss_seidel)









































































































