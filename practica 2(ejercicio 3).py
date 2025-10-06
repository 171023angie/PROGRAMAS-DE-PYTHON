class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
        print(f"Objeto Temperatura creado con {self.celsius}°C")

    def a_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def mostrar(self):
        print("=== Conversión de Temperatura ===")
        print(f"Temperatura en Celsius: {self.celsius}°C")
        print(f"Temperatura en Fahrenheit: {self.a_fahrenheit()}°F")

    def __del__(self):
        print("Objeto Temperatura destruido")


# Programa principal
temp = Temperatura(25)   # ejemplo con 25°C
temp.mostrar()

# eliminar objeto
del temp
