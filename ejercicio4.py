#4Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario. 

import os
print("Consulta si aprobo o no ")
nota = float(input("ingrese la calificacion del examen:"))
if nota >= 7:
    print ("Usted esta aprobado")
else:
    print("Usted no esta aprobado")

os.system ('pause')
