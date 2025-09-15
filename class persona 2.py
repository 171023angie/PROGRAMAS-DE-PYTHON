class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
nombre = input("Ingrese el nombre de la persona : ")
nombre = int(input("Ingrese la edad de la persona : "))

if persona.es_mayor_de_edad():
    print(f"{persona.nombre} es mayor de edad")
else:
    print(f"{persona.nombre} es menor de edad")
