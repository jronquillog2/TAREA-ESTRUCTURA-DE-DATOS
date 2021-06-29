#5.Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

import os
print("Consulta si obtiene un aumento")

sueldo = float(input("ingrese su sueldo:"))
aumento= sueldo*0.10
if sueldo < 600:
    print ("Si obtuvo aumento, su nuevo sueldo es:",sueldo+aumento)
else:
    print("No obtiene un aumento")

os.system ('pause')

