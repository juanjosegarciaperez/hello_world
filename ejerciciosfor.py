import time
def ejercicio1 ():
    palabra = str(input("por favor ingrese una palabra"))
    cantidad = int(input("por favor ingrese la cantidad"))
    for i in range(cantidad):
        print("valor de la variable i: ", i+1)
        time.sleep(2)
        print(palabra)
    return 

#ejercicio1()  

#programa en donde se ingrese la edad y muestre la cantidad hasta llegar a la edad

def edad ():
    edad = int(input("porfavor ingrese una edad"))
    for i in range(edad):
        time.sleep(1)
        print (i+1)

edad()    