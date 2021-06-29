#Determinar si un número entero proporcionado por el usuario es primo. Un número primo es un entero que no tiene más divisores que él mismo y la unidad. Elaborar Pseudocódigo:

import os
numero_leido = int(input("inserta un numero: "))
numero = int(numero_leido)
contador = 0
for i in range(1,numero+1):
    if (numero% i)==0:
        contador = contador + 1

if contador==2:
    print ("el numero es primo")
else:
    print ("el numero no es primo")

os.system ('pause')