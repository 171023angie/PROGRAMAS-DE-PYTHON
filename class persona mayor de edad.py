class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def clasificar(self):
        if self.edad < 18:
           return "Menor de edad"
        else :
            return "Mayor de edad"
ejemplos = [Persona("maria",25) , Persona("sadith",15) , Persona("nayelin",18)]

for persona in ejemplos:
    tipo = persona.clasificar()
    print(f"{persona.nombre} con {persona.edad} años es {tipo}")
