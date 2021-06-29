#Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y calcular el resultado

import os
class quin:
    def __init__(self):
        pass
    def calcularSerie(self):
        t=1
        c1=1
        cont=1
        c2=2
        n=int(input("Ingrese un numero: "))
        while n < 2:
            print("El numero debe ser mayor a 1")
            n=int(input("Intente de nuevo: "))
        while cont < n :
            if c2%2==0 :
                t=t-(1/(c1+1))
            else:
                t=t+(1/(c1+1))
            c1=c1+1
            c2=c2+1
            cont=cont+1
        print(t)
numero = qin()
numero.calcularSerie()

os.system("pause")