#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.

import os
class ll:
    def __init__(self):
        pass

    def sumaCuadradaos(self):
        acu=0
        cont=1
        n=0

        while cont < 101 :
            n=(cont)**2
            acu+=n
            cont=cont+1
        print(acu)

entero = ll()
entero.sumaCuadradaos()

os.system("pause")
