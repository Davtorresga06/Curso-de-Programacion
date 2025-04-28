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
def Valor_abosoluto(r):
    return r * -1 if r < 0 else r
r = int(input("Ingrese un numero real para conocer su valor absoluto: "))
print("el valor absoluto es: ",Valor_abosoluto(r))

def Mayor_de_2_numeros(a,b):
    return a if a > b else b
a = float(input("Ingrese un numero real: "))
b = float(input("Ingrese un numero real: "))
print("El mayor de los 2 muneros es: ", Mayor_de_2_numeros(a,b))

