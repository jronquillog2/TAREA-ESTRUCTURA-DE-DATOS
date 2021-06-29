#Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple.

import os

horas_de_trabajo = float (input ('Ingresa el valor de horas de trabajo: '))
pago_por_hora = float (input ('Ingresa el valor de pago por hora: '))
cantidad_de_dinero=horas_de_trabajo*pago_por_hora
if horas_de_trabajo>40:
    cantidad_de_dinero=cantidad_de_dinero+(horas_de_trabajo-40)*pago_por_hora
if horas_de_trabajo>48:
    cantidad_de_dinero=cantidad_de_dinero+(horas_de_trabajo-48)*pago_por_hora
print ('Valor de cantidad de dinero: ' + repr (cantidad_de_dinero))
print ()
os.system ('pause')