#Sea un vector “Calificaciones” de 100 componentes: En forma de columna se representaría así:

class Diocho:
    def __init__(self):
        pass
    def vector(self):
        A = []
        for i in range(0,100):
            A.append("calificacion" + str(i+1))
            print("Calificacion " + str(i+1))
        print(A)
calificaciones = ocho()
calificaciones.vector()
