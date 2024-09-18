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

#edad()    

#años actual y año de nacimiento

def calcular_la_edad ():
    #año_actual = int(input("por favor ingrese el año actual"))
    año_nacimiento = int(input("por favor ingrese el año de nacimiento"))
    edad = año_actual - año_nacimiento
    for i in range(edad):
        time.sleep(1)
        print (i+1)

#calcular_la_edad()


def triangulo_de_numeros ():
    numero = int(input("Por favor ingrese un número"))
    for i in range(numero):
        for j in range(i+1):
            print("*", end=" ")
        print("-")

triangulo_de_numeros()        