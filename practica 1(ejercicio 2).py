class Temperatura:
    def _init_(self, valor=0.0):
        self.__valor = float(valor)  # atributo privado

    # getter y setter
    def get_valor(self):
        return self.__valor

    def set_valor(self, nuevo_valor):
        self.__valor = float(nuevo_valor)

    # métodos de conversión
    def fahrenheit_a_celsius(self):
        return (self.__valor - 32) * 5 / 9

    def celsius_a_fahrenheit(self):
        return (self.__valor * 9 / 5) + 32


def main():
    print("=== Conversor de Temperaturas ===")
    print("1. Fahrenheit → Celsius")
    print("2. Celsius → Fahrenheit")

    opcion = input("Elige una opción (1 o 2): ")

    if opcion == "1":
        f = float(input("Ingrese la temperatura en °F: "))
        temp = Temperatura(f)
        print(f"{f} °F = {temp.fahrenheit_a_celsius():.2f} °C")

    elif opcion == "2":
        c = float(input("Ingrese la temperatura en °C: "))
        temp = Temperatura(c)
        print(f"{c} °C = {temp.celsius_a_fahrenheit():.2f} °F")

    else:
        print("Opción no válida.")


if _name_ == "_main_":
    main()
