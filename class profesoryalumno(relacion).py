class Profesor:
    def __init__(self,nombre):
        self.nombre = nombre

class Curso:
    def __init__(self,nombre,profesor):
        self.nombre = nombre
        self.profesor = profesor

prof = Profesor("Dr.Morrillos")
curso = Curso("muestreo",prof)
print(curso.profesor.nombre)

