#Calcular el factorial de N números enteros leídos de teclado.

import os

factorial = 0
n = int (input ('Ingresa el valor de n: '))
for i in range (1, n + 1):
    print ('PROCESO ' + repr (i))
    if i==1:
        factorial=1
    else:
        factorial=factorial*i
    print ()
print ('Valor de factorial: ' + repr (factorial))
os.system ('pause')