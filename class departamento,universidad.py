class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def mostrar_departamentos(self):
        print(f"Universidad: {self.nombre}")
        print("Departamentos:")
        for dep in self.departamentos:
            print(f"- {dep.nombre}")

# Crear departamentos
dep1 = Departamento("Ingeniería Estadística")
dep2 = Departamento("Informática")

# Crear universidad y agregar departamentos
uni = Universidad("Universidad Nacional del Altiplano")
uni.agregar_departamento(dep1)
uni.agregar_departamento(dep2)

# Mostrar información
uni.mostrar_departamentos()

