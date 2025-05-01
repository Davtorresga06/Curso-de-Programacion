## Estructura para realizar ciclos while en python

x = 0
y = 10

while (x < 5 and y > 5):
    print("hola ", x)
    print("adios ", y)
    y -= 1
    
print("fin del ciclo")
#siempre dar condiciones con fin al ciclo, si no se queda en un bucle infinito
## Esta es la estructura para realizar ciclos en python 

## Estructura para realizar ciclos for en python
##            0        1         2        3
Frutas = ["manzana", "pera", "naranja", "uva"]

print("Frutas: ", Frutas[2])

for i in Frutas:
    print("Esta frutas es: ", i)

##operaciones de conversion
#convierte el valor 65 a su respectivo caracter ascci
a = int(input("ingrese un numero para conocer su equivalente en ASCCI: "))
print("este es el quivalente a: ", chr(a)) 

