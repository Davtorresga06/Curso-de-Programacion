
numero = int(input("Ingrese un número (positivo): "))
if numero > 0:
    print("El cuadrado de el número ingresado es", numero ** 2)
else:  
    print("El numero ingresado es negativo o 0")

n = int(input("Ingrese un número entero positivo: "))
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
print(n)  # Para imprimir el 1 al final

año = 2022
poblacion_A = 25.0
poblacion_B = 18.9
while poblacion_B <= poblacion_A:
    poblacion_A *= 1.02
    poblacion_B *= 1.03
    año += 1
print("La población del país B superará a la del país A en el año", año,".")
