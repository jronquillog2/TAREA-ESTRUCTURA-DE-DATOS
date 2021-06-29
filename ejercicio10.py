#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función:

import os

class ten:
 def __init__(self):
    pass


 def resultado(self):
    resultado = 0
    valor = 0
    n = int(input(
        "Ingrese el numero de la opercacion que desee realizar:\n 1) Multiplicacion \n 2) Potenciacion \n 3) Division \n "))

    if n == 1:
        valor = float(input("Ingrese el numero con el que desea realizar la multiplicacion: "))
        resultado = 100 * valor
    elif n == 2:
        while valor == 0:
            valor = float(input("Ingrese el numero con el que desea realizar la potenciacion: "))
        resultado = 100 ** valor
    elif n == 3:
        while valor == 0:
            valor = float(input("Ingrese el numero con el que desea realizar la division: "))
        resultado = 100 / valor
    else:
        resultado = 0

    print("Respuesta = ", resultado)


datos = ten()
datos.resultado()
