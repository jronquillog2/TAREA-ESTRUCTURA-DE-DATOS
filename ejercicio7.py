#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

import os

a = float (input ('Ingresa el valor de a: '))
b = float (input ('Ingresa el valor de b: '))
c = float (input ('Ingresa el valor de c: '))
mayor=a
if mayor<b:
    mayor=b
if mayor<c:
    mayor=c
print ('Valor de mayor: ' + repr (mayor))
print ()
os.system ('pause')