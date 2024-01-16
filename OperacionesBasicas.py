#inicio del programa

import numpy as np

# Funciones con Numpy
def suma_numpy(a, b):
    return np.add(a, b)

def resta_numpy(a, b):
    return np.subtract(a, b)

def multiplicacion_numpy(a, b):
    return np.multiply(a, b)

def division_numpy(a, b):
    return np.divide(a, b)

# Obtener los valores de a y b del usuario
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))

# Realizar las operaciones
suma_estandar = a + b
resta_estandar = a - b
multiplicacion_estandar = a * b
division_estandar = a / b

# Comparación de resultados y discusión de posibles errores
print("Suma con Numpy:", suma_numpy(a, b))
if abs(suma_numpy(a, b) - suma_estandar) < 1e-10:
    print("La suma es correcta.")
else:
    print("Posible error en la suma,por favor intentelo de nuevo")

print("Resta con Numpy:", resta_numpy(a, b))
if abs(resta_numpy(a, b) - resta_estandar) < 1e-10:
    print("La resta es correcta.")
else:
    print("Posible error en la resta,por favor intentelo de nuevo.")

print("Multiplicación con Numpy:", multiplicacion_numpy(a, b))
if abs(multiplicacion_numpy(a, b) - multiplicacion_estandar) < 1e-10:
    print("La multiplicación es correcta.")
else:
    print("Posible error en la multiplicación,por favor intentelo de nuevo.")

print("División con Numpy:", division_numpy(a, b))
if abs(division_numpy(a, b) - division_estandar) < 1e-10:
    print("La división es correcta.")
else:
    print("Posible error en la división,por favor intentelo de nuevo.")


# fin del programa