"""
Universidad Jose Antonio Paéz
Estudiantes: Victor Marcano, Gustavo Paéz, Andres Chavéz
Profesora: Maria García - Calculo numérico
"""
#inicio del programa

import sys
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
                    if abs(A[i,j] * x[j]) < float('inf'):
                      s += A[i, j] * x[j]
                    else:
                        
                        break
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
                else:
                    break
                
            x[i] = (b[i] - s) / A[i, i]
            
        if np.linalg.norm(np.dot(A, x) - b) < tol:
            return x
    return x
def F_manual():
    try:
        N = int(input("Tamaño de matriz NxN: "))
        if N <= 0:
            raise ValueError("El tamaño de la matriz debe ser un entero positivo")

        A = np.zeros((N,N))
        A = A.astype(np.float64)
        for i in range(N):
            for j in range(N):
                A[i,j] = float(input(f"A[{i},{j}]: "))

        b = np.zeros(N)
        b = b.astype(np.float64)

        for i in range(N):
            b[i] = float(input(f"b[{i}]: "))

        x = np.linalg.solve(A, b)              
        print(x)
        x_exact = np.linalg.solve(A, b)           

        # Escalar los coeficientes y el término independiente
        scale = np.max(np.abs(A))
        A_scaled = A / scale
        b_scaled = b / scale

        x0 = np.zeros_like(b)
        x0 = x0.astype(np.float64) 

        tol = 1e-6
        max_iter = 1000

        x_jacobi = jacobi(A_scaled, b_scaled, x0, tol, max_iter)
        x_gauss_seidel = gauss_seidel(A, b, x0, tol, max_iter)

        print("Solución exacta:", x_exact)
        print("Solución Jacobi:", x_jacobi)
        print("Solución Gauss-Seidel:", x_gauss_seidel)

        finPro()

    except RuntimeWarning as er: 
        print(f"Error: {er}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado,intente de nuevo: {e}")

def F_automatica():
    try:
        N = int(input("Tamaño de matriz NxN: "))
        if N <= 0:
            raise ValueError("El tamaño de la matriz debe ser un entero positivo")
        A = np.random.randint(0, 10, size=(N, N))
        A = A.astype(np.float64)

        b= np.random.randint(0, 10, size=N)  
        b = b.astype(np.float64)

        x = np.linalg.solve(A, b)              
        print(x)
        x_exact = np.linalg.solve(A, b)           

        x0 = np.zeros_like(b)
        x0 = x0.astype(np.float64) 

        tol = 1e-6
        max_iter = 1000

        x_jacobi = jacobi(A, b, x0, tol, max_iter)
        x_gauss_seidel = gauss_seidel(A, b, x0, tol, max_iter)

        print("Solución exacta:", x_exact)
        print("Solución Jacobi:", x_jacobi)
        print("Solución Gauss-Seidel:", x_gauss_seidel)

        finPro()

    except RuntimeWarning as er: 
        print(f"Error: {er}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado,intente de nuevo: {e}")

def finPro():
    print("El programa ha finalizado correctamente")
    sys.exit()

print("――――――――――――――――――――――――――――――――――――")
print("⫸  MENU DE OPCIONES ⫷")
print("1 🡆 Crear matriz Manual")
print("2 🡆 Crear matriz Automatica")
print("――――――――――――――――――――――――――――――――――――")
opcion= int(input("Introduce la opcion ➜  "))
if opcion == 1:
    F_manual()
if opcion == 2:
    F_automatica()



