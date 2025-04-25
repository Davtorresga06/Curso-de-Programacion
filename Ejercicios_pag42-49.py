
## EJERCICIOO PAGINA 42 VOLUMEN DE LA ESFERA Y EL CONO

import math


#Codigo esfera
def volumen_esfera(R1):
    return (4/3) * math.pi *R1**3
R1 = float(input("Radio de la esfera (en cm): "))
print("El volumen de la esfera es: ", end="")
print(volumen_esfera(R1),"cm³")

#Codigo cono
def volumen_cono(R2,h):
    return (1/3) * math.pi *R2**2 * h
R2 = float(input("Radio de la base del cono(en cm): "))
h = float(input("Altura del cono (en cm): "))
print("El volumen del cono es: ", end="")
print(volumen_cono(R2,h),"cm³")

## EJERCICIO PAGINA 45  AREA RECTANNGULO Y CIRCUNFERENCIA

#Codigo rectangulo
def area_rectangulo(a,b):
    return a * b
a = float(input("Largo del rectangulo (en cm): "))
b = float(input("Ancho del rectangulo (en cm): "))
print("El area del rectangulo es: ", end="")
print(area_rectangulo(a,b),"cm²")

#Codigo circunferencia
def area_circunferencia(r):
    return math.pi * r**2
r = float(input("Radio de la circunferencia (en cm): "))
print("El area de la circunferencia es: ", end="")
print(area_circunferencia(r),"cm²")

#Area lateral total de la circunferencia y el rectangulo(vagón)
print(" el area total de la circunferencia y el rectangulo es: ", end="")
print(area_circunferencia(r) + area_rectangulo(a,b),"cm²")

##EJERCICIO PAGINA 47 RECTANGULOS Y CIRCUNFERENCIAS

#Codigo rectangulo 1
def area_rectangulo_1(c,d):
    return c *d
c = float(input("Largo del rectangulo 1 (en cm): "))
d = float(input("Ancho del rectangulo 1 (en cm): "))
print("El area del rectangulo 1 es: ", end="")
print(area_rectangulo_1(c,d),"cm²")

#Codigo rectangulo 2
def area_rectangulo_2(e,f):
    return e * f
e= float(input("Largo del rectangulo 2 (en cm): "))
f = float(input("Ancho del rectangulo 2 (en cm): "))
print("El area del rectangulo es: ", end="")
print(area_rectangulo_2(e,f),"cm²")

#Codigo circunferencia 1
def area_circunferencia_1(r1):
    return math.pi * r1**2
r1 = float(input("Radio de la circunferencia 1 (en cm): "))
print("El area de la circunferencia es: ", end="")
print(area_circunferencia_1(r1),"cm²")

#Codigo circunferencia 2
def area_circunferencia_2(r2):
    return math.pi * R2**2
r2 = float(input("Radio de la circunferencia 2 (en cm): "))
print("El area de la circunferencia es: ", end="")
print(area_circunferencia_2(r2),"cm²")

#Area lateral total de  los rectangulos y las circunferencias(carro)
print("El area total de los rectangulos y circunferencias es: ", end="")
print(area_rectangulo_1(c,d) + area_rectangulo_2(e,f) + area_circunferencia_1(r1) + area_circunferencia_2(r2),"cm²")

