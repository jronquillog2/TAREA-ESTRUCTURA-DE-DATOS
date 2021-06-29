#Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros y a continuación escribir en un vector A todos los números negativos y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores.

import os
class Dinueve:
    def __init__(self):
        pass
    def positivoNegativo(self):
        A = []
        P = []
        N = []
        for i in range(0,10):
            n=int(input("Ingrese un nùmero: "))
            A.append(n)
            if n > -1:
                P.append(n)
            else:
                N.append(n)
        print("Vector con numeros positivos: {}\nVecor con numeros negativos: {}".format(P,N))
numero = Dinueve()
numero.positivoNegativo()
os.system("pause")
