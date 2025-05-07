##Ejercicio #1
suma_total = 0  # crear una variable para almacenar la suma total de los números positivos y pares

# Leer los números uno por uno
a = int(input("Ingrese un número (positivo par): "))#ingresar los numeros desde la consola
if a > 0 and a % 2 == 0:#condiciones de que si es par y positivo
    suma_total += a# agregar el dato a la suma ya que el condicional se cumplio

b = int(input("Ingrese un número (positivo par): "))#ingresar los numeros desde la consola
if b > 0 and b % 2 == 0:#condiciones de que si es par y positivo
    suma_total += b# agregar el dato a la suma ya que el condicional se cumplio

c = int(input("Ingrese un número (positivo par): "))#ingresar los numeros desde la consola
if c > 0 and c % 2 == 0:#condiciones de que si es par y positivo
    suma_total += c# agregar el dato a la suma ya que el condicional se cumplio

d = int(input("Ingrese un número (positivo par): "))#ingresar los numeros desde la consola
if d > 0 and d % 2 == 0:#condiciones de que si es par y positivo
    suma_total += d# agregar el dato a la suma ya que el condicional se cumplio

e = int(input("Ingrese un número (positivo par): "))#ingresar los numeros desde la consola
if e > 0 and e % 2 == 0:#condiciones de que si es par y positivo
    suma_total += e# agregar el dato a la suma ya que el condicional se cumplio

print("La suma total de los números positivos y pares es:", suma_total)# Mostrar la suma total de los números positivos y pares


## Ejercicio 2
Edad = int(input("Ingrese su edad: "))#ingresar desde la consola la edad de la persona
if 0 < Edad < 13:#condiciones de edad
    print("Es un niño")#impresion segun la edad
elif 13 <= Edad <= 17:#condiciones de edad
    print("Es un adolescente")#impresion segun la edad
elif 18 <= Edad <= 59:#condiciones de edad
    print("Es un adulto")#impresion segun la edad
elif Edad >= 60:#condiciones de edad
    print("Es un adulto mayor")#impresion segun la edad
else:#condiciones de edad
    print("Edad no válida")#impresion si la edad no es valida
    

## Ejercicio 3

# Crear las variables de contadores para cada vocal
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0
palabra = ""  # Inicializar la variable palabra como una cadena vacía

# Verificar manualmente cada posición de la palabra para saber si tiene alguna vocal
while palabra == "":
    palabra = str(input("Ingrese una palabra (de 8 caracteres): "))  # Solicitar la palabra desde la consola
    if palabra[0] == 'a' or palabra[0] == 'A':
        contador_a += 1
    elif palabra[0] == 'e' or palabra[0] == 'E':
        contador_e += 1
    elif palabra[0] == 'i' or palabra[0] == 'I':
        contador_i += 1
    elif palabra[0] == 'o' or palabra[0] == 'O':
        contador_o += 1
    elif palabra[0] == 'u' or palabra[0] == 'U':
        contador_u += 1

    if palabra[1] == 'a' or palabra[1] == 'A':
        contador_a += 1
    elif palabra[1] == 'e' or palabra[1] == 'E':
        contador_e += 1
    elif palabra[1] == 'i' or palabra[1] == 'I':
        contador_i += 1
    elif palabra[1] == 'o' or palabra[1] == 'O':
        contador_o += 1
    elif palabra[1] == 'u' or palabra[1] == 'U':
        contador_u += 1

    if palabra[2] == 'a' or palabra[2] == 'A':
        contador_a += 1
    elif palabra[2] == 'e' or palabra[2] == 'E':
        contador_e += 1
    elif palabra[2] == 'i' or palabra[2] == 'I':
        contador_i += 1
    elif palabra[2] == 'o' or palabra[2] == 'O':
        contador_o += 1
    elif palabra[2] == 'u' or palabra[2] == 'U':
        contador_u += 1

    if palabra[3] == 'a' or palabra[3] == 'A':
        contador_a += 1
    elif palabra[3] == 'e' or palabra[3] == 'E':
        contador_e += 1
    elif palabra[3] == 'i' or palabra[3] == 'I':
        contador_i += 1
    elif palabra[3] == 'o' or palabra[3] == 'O':
        contador_o += 1
    elif palabra[3] == 'u' or palabra[3] == 'U':
        contador_u += 1

    if palabra[4] == 'a' or palabra[4] == 'A':
        contador_a += 1
    elif palabra[4] == 'e' or palabra[4] == 'E':
        contador_e += 1
    elif palabra[4] == 'i' or palabra[4] == 'I':
        contador_i += 1
    elif palabra[4] == 'o' or palabra[4] == 'O':
        contador_o += 1
    elif palabra[4] == 'u' or palabra[4] == 'U':
        contador_u += 1

    if palabra[5] == 'a' or palabra[5] == 'A':
        contador_a += 1
    elif palabra[5] == 'e' or palabra[5] == 'E':
        contador_e += 1
    elif palabra[5] == 'i' or palabra[5] == 'I':
        contador_i += 1
    elif palabra[5] == 'o' or palabra[5] == 'O':
        contador_o += 1
    elif palabra[5] == 'u' or palabra[5] == 'U':
        contador_u += 1

    if palabra[6] == 'a' or palabra[6] == 'A':
        contador_a += 1
    elif palabra[6] == 'e' or palabra[6] == 'E':
        contador_e += 1
    elif palabra[6] == 'i' or palabra[6] == 'I':
        contador_i += 1
    elif palabra[6] == 'o' or palabra[6] == 'O':
        contador_o += 1
    elif palabra[6] == 'u' or palabra[6] == 'U':
        contador_u += 1

    if palabra[7] == 'a' or palabra[7] == 'A':
        contador_a += 1
    elif palabra[7] == 'e' or palabra[7] == 'E':
        contador_e += 1
    elif palabra[7] == 'i' or palabra[7] == 'I':
        contador_i += 1
    elif palabra[7] == 'o' or palabra[7] == 'O':
        contador_o += 1
    elif palabra[7] == 'u' or palabra[7] == 'U':
        contador_u += 1


# Imprimir los resultados
print(f"La palabra {palabra} tiene:")
print(f"{contador_a} vocal(es) 'a' o 'A'")
print(f"{contador_e} vocal(es) 'e' o 'E'")
print(f"{contador_i} vocal(es) 'i' o 'I'")
print(f"{contador_o} vocal(es) 'o' o 'O'")
print(f"{contador_u} vocal(es) 'u' o 'U'")