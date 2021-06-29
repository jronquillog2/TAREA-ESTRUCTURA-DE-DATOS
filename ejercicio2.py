#2.Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.

import os
sueldo = 400
ventas = float (input ('Ingresa el valor del total de las 3 ventas: '))
if ventas>=1:
    comision=ventas*0.10
else:
    comision=0
sueldototal = sueldo + comision
print ('su sueldo mas comision es de: ',sueldototal )
print ()
os.system ('pause')