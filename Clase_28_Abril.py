#hola mundo
##Se pueden hacer commits de visual a git y de git a visual, pero dice que se debe hace un pull
##para trabajar con la ultima version del repositorio que es la que esta en git, haciendo que se combinen los commits de visual y de git, esta operacion se llama merge)



##ESTRUCTURAS DE COCNTROL(if, else, elif)
## los condiconales son solo verdadero y falso(booleanos)

## VALOR ABSOLUTO
def Valor_abosoluto(r):
    if r < 0:
        return r * -1
    else:
        return r
r = int(input("Ingrese un numero real para conocer su valor absoluto: "))
print("el valor absoluto es: ",Valor_abosoluto(r))


## EL MAYOR DE DOS NUMEROS
def Mayor_de_2_numeros(a,b):
    if a > b:
        return a
    else:
        return b    
a = float(input("Ingrese un numero real: "))
b = float(input("Ingrese un numero real: "))
print("El mayor de los 2 muneros es: ", Mayor_de_2_numeros(a,b))


## OPERADOR CONDICIONAL TERNARIO



## EJECICIO DE LOS PRODUCTOS CON DESCUENTO
def precio_final(precio_inicial,n_productos,descuento):
    if n_productos < 5:
        return precio_inicial
    elif 5 < n_productos <= 10:
        return precio_inicial * descuento
    elif 10 < n_productos <= 15:
        return precio_inicial * descuento
    elif 15 < n_productos <= 20:
        return precio_inicial * descuento
    else:
        return precio_inicial * descuento
    
a = 0.95
b= 0.90
c = 0.85
d = 0.80

precio_inicial = float(input("Ingrese el precio del producto (COP): "))
n_productos = int(input("Ingrese la cantidad de productos: "))
descuento = (
    0 if n_productos < 5 else
    a if 5 <= n_productos <= 10 else
    b if 10 < n_productos <= 15 else
    c if 15 < n_productos <= 20 else
    d
) 
print("El precio final es: ", precio_final(precio_inicial,n_productos,descuento) * n_productos ,"Y el descuento es del :", 1 - descuento , "%")