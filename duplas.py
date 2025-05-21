##Esto es una tupla
## index cuanta la primera aparcion del elemento
#elemento0 1  2  3  4, siempre los elementos se empiezan a contar desde 0
tup2 = (1, 2, 3, 4, 5)# estos elementos no se pueden cambiar redefiniendolos como variable solo desde la definicion de la tupla, mientras que en una lista si se puede cambiar el valor de la variable
print("Estos son los elemntos totales: ", tup2)
print("Este es el elmento en su parte 2 es: ", tup2[2])

texto = ("cien", "años", "de", "soledad")
if "años" in texto:
    print("La palabra años esta en la tupla", "esta en la posicion", texto.index("años"))
else:
    print("La palabra años no esta en la tupla")

if "cien" in texto:
    print("La palabra años esta en la tupla", "esta en la posicion", texto.index("cien")) 
else:
    print("La palabra años no esta en la tupla")
    
if "soledad" in texto:
    print("La palabra años esta en la tupla", "esta en la posicion", texto.index("soledad"))
else:
    print("La palabra años no esta en la tupla")
    
s = ("hola", "amigos", "mios")
for plabra in s: 
    print("La palabra es: ", plabra)
    
tupla = (1,-2, 3)
a, b, c = tupla
print("a =", a)
print("b =", b)
print("c =", c)
 
 
tupla= (11,9,-2,3,8,5)
var1, var2, var3 = (tupla[i] for i in (1, 3, 5))
print("var1=", var1, ",var2=", var2, ",var3=", var3)
var1, var2, var3 = (tupla[i] for i in range(0, 6, 2))
print("var1=", var1, ",var2=", var2, ",var3=", var3)

def minmax(a,b):
    if a < b:
        return a,b
    else:
        return b,a
x,y = minmax(5,13)
print("min=",x,",","max=",y)
x,y = minmax(12,-4)
print("min=",x,",","max=",y)
    
    
t = (4, 5,-1, 6, 7)
print(max(t))
print(min(t))
 
lista = [1, 2, 3, 4, 5]
lista[0] = 10
print(lista)

lista1 = [0,1,2,3]
lista2 = ["A","B","C"]
lista3 = [lista1,lista2]
print(lista3)
print(lista3[0])
print(lista3[1])
print(lista3[1][0])

d = 10
desplaza = [d + x for x in range(5)]
print(desplaza)
potencias = [3 ** x for x in range(2, 6)]
print(potencias)

lista=[4,5,-1,6,7]
lista.sort() #Demenoramayor
print(lista)
lista.sort(reverse=True) #Demayoramenor
print(lista)

def lee_arreglo_enteros():
    return (int(x) for x in input("Arreglo: ").split())
print(list(lee_arreglo_enteros()))

