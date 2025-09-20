class Persona:
    def __init__(self, nombre, edad):  # doble guion bajo
        self.nombre = nombre
        self.edad = edad

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

# Crear el objeto
persona = Persona("María", 25)

# Verificar si es mayor de edad
if persona.es_mayor_de_edad():
    print(f"{persona.nombre} es mayor de edad")
else:
    print(f"{persona.nombre} es menor de edad")
