class Empleado:
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual
        print("Objeto Empleado creado")
        print(f"Empleado: {self.nombre}, Salario mensual: {self.salario_mensual}")

    def salario_anual(self):
        return self.salario_mensual * 12

    def mostrar_informacion(self):
        print("INFORMACIÓN DEL EMPLEADO")
        print(f"Nombre: {self.nombre}")
        print(f"Salario mensual: {self.salario_mensual}")
        print(f"Salario anual: {self.salario_anual()}")

    def __del__(self):
        print(f"Empleado {self.nombre} ha sido dado de baja")

def main():
    try:
        empleado1 = Empleado("Gleny", 1500)
        empleado1.mostrar_informacion()
        
    except NameError:
        print("Error al crear el empleado")

if __name__ == "__main__":
    main()
