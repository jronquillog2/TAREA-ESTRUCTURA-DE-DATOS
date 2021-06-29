#1.En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra

import os

costo_del_articulo_1 = float (input ('Ingresa el valor de costo del articulo 1: '))
costo_del_articulo_2 = float (input ('Ingresa el valor de costo del articulo 2: '))
costo_del_articulo_3 = float (input ('Ingresa el valor de costo del articulo 3: '))
total_de_la_compra=costo_del_articulo_1+costo_del_articulo_2+costo_del_articulo_3
if total_de_la_compra>1:
    descuento=total_de_la_compra*0.15
else:
    descuento=0
pago_final=total_de_la_compra-descuento
print ('Valor de descuento: ' + repr (descuento))
print ('Valor de pago final: ' + repr (pago_final))
print ('Valor de total de la compra: ' + repr (total_de_la_compra))
print ()
os.system ('pause')
