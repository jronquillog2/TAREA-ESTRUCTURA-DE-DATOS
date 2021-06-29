#ejemplo de or

import os
print("Consulta si es aceptado o recazado ")
C1 = float(input("ingrese la calificacion del  primer examen:"))
C2 = float(input("ingrese la calificacion del segundo examen:"))

if (C1 >= 90) or (C2 >= 90):
    print ("ACEPTADO")
else:
    print("RECHAZAD0")

os.system ('pause')