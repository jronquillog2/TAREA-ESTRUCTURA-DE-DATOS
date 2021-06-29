#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado

import os
print("Consulta si es aceptado o recazado ")
C1 = float(input("ingrese la calificacion del  primer examen:"))
C2 = float(input("ingrese la calificacion del segundo examen:"))
notafinal = C1+C2
if notafinal >= 80:
    print ("ACEPTADO")
else:
    print("RECHAZAD0")

os.system ('pause')