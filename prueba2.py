import math 
import random 
resultado: int 


def suma_dos_valores(sumado1, sumado2):
    global resultado 
    resultado = sumado1 + sumado2
    return resultado

#suma_dos_valores(4,5)
#print ("primera suma")
#print (resultado)
#suma_dos_valores(1,2)
#print ("segunda suma")
#print (resultado)

def calculadora_dos_valores(numero1, numero2, operador):
    global resultado
    if operador ==1: #si el operador de 1 es suma
        resultado = numero1 + numero2
        return resultado
    elif operador == 2: # si el operador de 2 es resta
        resultado = numero1 - numero2
        return resultado
    elif operador == 3: # si el operador de 3 es multiplicación
        resultado = numero1 * numero2
        return resultado
    elif operador == 4: # si el operador de 4 es division
        resultado = numero1 / numero2
        return resultado
    else: # si el numero es diferente no se puede realizar operación
        print ("el valor insertado no es valido")

#calculadora_dos_valores(1,2,1)
#print ("suma", resultado)
#calculadora_dos_valores(1,2,2)
#print ("resta", resultado)
#calculadora_dos_valores (1,2,3)
#print("multiplicación", resultado)
#calculadora_dos_valores (1,2,4)
#print("division", resultado)


def calculadora_pitagoras(cateto1,cateto2):
    global resultado
    potencia1 = cateto1**2
    potencia2 = cateto2**2
    suma = potencia1 + potencia2
    resultado = math.sqrt(suma)
    return resultado

#calculadora_pitagoras (3,4)
#print (resultado)

def depejar_X ():
    global resultado 
    B = int(input("Ingrese el valor de B : "))
    C = int(input("Ingrese el valor de C : "))
    resta = C-B
    resultado = resta/2
    print("el valor de que x es igual a", resultado)
    return resultado

#depejar_X()

def And_tres_valores ():
    global resultado
    A = bool(input("inserte true o false "))
    B = bool(input("inserte true o false "))
    C = bool(input("inserte true o false "))
    resultado = A and B and C
    return resultado

#And_tres_valores()
#print("el resultado es", resultado)

def pitagoras_funcion_sumar():
    global resul_pitagoras
    a = int(input("inserte el valor de a "))
    b = int(input("inserte el valor de b "))
    a2 = a**2
    b2 = b**2
    suma = suma_dos_valores(a2,b2)
    resul_pitagoras = suma**0.5
    print("el valor de pitagoras es", resul_pitagoras)
    return resul_pitagoras

#pitagoras_funcion_sumar()


def piedra_papel_tijeras ():
    resultado_jugador1 = "gana el jugador 1"
    resultado_jugador2 = "gana el jugador 2"
    derrota_jugador1 = "pierde el jugador 1"
    derrota_jugador2 = "pierde el jugador 2"
    piedra = 1
    papel = 2
    tijeras = 3
    jugador1 = random.randint(1,3)
    jugador2 = random.randint(1,3)
    if jugador1 == piedra and jugador2 == papel :
        print(resultado_jugador2, "papel")
        print(derrota_jugador1, "piedra")
        return resultado_jugador2
    elif jugador1 == papel and jugador2 == tijeras :
        print(resultado_jugador2, "tijeras")
        print(derrota_jugador1, "papel")
        return resultado_jugador2
    elif jugador1 == tijeras and jugador2 == piedra :
        print(resultado_jugador2, "piedra")
        print(derrota_jugador1, "tijeras")
        return resultado_jugador2
    elif jugador1 == papel and jugador2 == piedra :
        print(resultado_jugador1, "papel")
        print(derrota_jugador2, "piedra")
        return resultado_jugador1
    elif jugador1 == piedra and jugador2 == tijeras :
        print(resultado_jugador1, "piedra" )
        print(derrota_jugador2, "tijeras")
        return resultado_jugador1
    elif jugador1 == tijeras and jugador2 == papel :
        print(resultado_jugador1, "tijeras")
        print(derrota_jugador2, "papel")
        return resultado_jugador1
    elif jugador1 == jugador2:
        print("empate")


piedra_papel_tijeras()