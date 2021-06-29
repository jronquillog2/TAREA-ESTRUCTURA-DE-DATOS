#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por un centinela

import os
class DO:
    def __init__(self):
        pass

    def sumaProducto(self):
        centinela=0
        n=float(input("Ingrese un numero: "))
        suma=0
        producto=1
        while centinela != -1:
            suma=suma+n
            producto= producto*n
            print("suma: {} Producto: {} \n".format(suma,producto))
            n=int(input("Ingrese otro numero: "))
            centinela = n
        print("\nHaz finalizado la operación suma: {}  producto: {}".format(suma,producto))
numeros = DO()
numeros.sumaProducto()

os.system("pause")
