## EJERCICIO 17
suma_cuadrados = 0
a = 1  # Inicializar el contador
while a < 101:  # Del 1 al 100, incluyendo ambos
    suma_cuadrados += a ** 2  # Elevar al cuadrado y acumular
    a += 1  # Incrementar el contador
print("La suma de los cuadrados de los cien primeros números naturales es:", suma_cuadrados)

## EJERCICIO 18
numero = int(input("Ingresa un número entero: "))
contador = 1
suma = 0
actual = numero + 1
while contador <= 100:
    suma += actual
    actual += 1
    contador += 1
print("La suma de los 100 números siguientes a", numero, "es:", suma)

## EJERCICIO 19
a = float(input("Introduce la cantidad de euros que deseas convertir a dolares: "))
b = float(input("Introduce el valor actual del dolar con respecto al euro: "))
print("La cantidad de euros en dolares es: ", a * b)

## EJERCICIO 20
def area_rectangulo(l,a):
    area = l * a 
    return area
    
largo = float(input("Largo del ractangulo: "))
ancho = float(input("Ancho del rectangulo: "))
print("El area del rectangulo es:", end=" ")
print(area_rectangulo(largo, ancho))

## EJERCICIO 21
def Mayor_de_2_numeros(a,b):
    if a > b:
        print("El mayor de los 2 muneros es: ",a, "y el menor es: ",b)
        return a

    else:
        print("El mayor de los 2 muneros es: ",b, "y el menor es: ",a)
        return b    
a = float(input("Ingrese un numero real: "))
b = float(input("Ingrese otro numero real: "))
Mayor_de_2_numeros(a, b)

## EJERCICIO 22
a = int(input("Ingresa un número entero: "))
contador = 1
print("los numeros impares menores que", a," son :")
while contador < a:
    print(contador)
    contador += 2
    
## EJERCICIO 23
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
while b != 0:
    a, b = b, a % b
print("El máximo común divisor (GCD) es:", a)

## EJERCICIO 24
import math
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))
if a == 0:
    print("No es una ecuación de segundo grado.")
else:
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("La ecuación tiene dos soluciones reales distintas:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif discriminante == 0:
        x = -b / (2*a)
        print("La ecuación tiene una única solución real:")
        print("x =", x)
    else:
        print("La ecuación no tiene soluciones reales.")