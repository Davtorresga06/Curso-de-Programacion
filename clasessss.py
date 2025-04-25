## defclarar funciones
    ##primero se escribe la palabra reservada "def" y luego se define el nombre de la funcion y luego los (aqui se escribe el argumento Variables o muchas cosas mas):
    ## luego el reurn la funcio que se quiere realizar 

import math ##importar librerias

def xCuadrado(x,y):
    z = x ** y 
    print(f"este es el resultado de la función {z}")
    return z
xCuadrado(2,3)

import math

def area_circulo(r):
    result = math.pi * r ** 2
    print("Esta es el area del circulo", result)
area_circulo(10)

def area_rectangulo(l,a):
    area = l * a 
    return area
    
largo = float(input("Largo del ractangulo: "))
ancho = float(input("Ancho del rectangulo: "))
print("El area del rectangulo es:", end=" ")
print(area_rectangulo(largo, ancho))




## EJERCICIOO LEY DE COULOMB
def ley_coulomb(q1, q2, r):
    k: float = 9e+9  # Constante de Coulomb en N m²/C²
    fuerza = k * (q1 * q2) / (r ** 2)
    return fuerza
carga1 = float(input("Carga 1: "))
carga2 = float(input("Carga 2: "))
distancia = float(input("Distancia entre cargas(en metros)): "))
print("El módulo de la fuerza es:", end= "")
print(ley_coulomb(carga1, carga2, distancia))



