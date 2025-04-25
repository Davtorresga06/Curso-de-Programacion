##Ejercicio de los numbers primos
dato = 0

##operation simplified
## dato %=2

while(dato <51):
    if( dato % 2 == 0) or ( dato % 3 == 0) or ( dato % 5 == 0) or ( dato % 7 == 0):
        print("el number se descartes como primo" , dato)
    else:
        print("number primo" , dato)
        
    dato +=1
    
##Capturar un dato desde consola 
## \n se usa para que pase a la sigueite linea en el print


dato = int(input ("ingrse un numero "))

result = 4 + dato

print(F"Este es el dato que usted ingreso sumado con 4, {result} felicidades")
print(type(dato))


dato = 2
if(dato == 2):
    print("se ejecuto el condicional")
else:
    print("no se ejecuto el condicional")
