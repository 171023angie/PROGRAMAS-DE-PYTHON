class Persona:
    def _init_(self, peso, altura):
        # atributos privados
        self.__peso = float(peso)
        self.__altura = float(altura)

    # getters y setters (encapsulamiento)
    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        self.__peso = float(nuevo_peso)

    def get_altura(self):
        return self.__altura

    def set_altura(self, nueva_altura):
        self.__altura = float(nueva_altura)

    # método para calcular IMC
    def calcular_imc(self):
        if self.__altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")
        return self._peso / (self._altura ** 2)

    # método para clasificar según OMS
    def clasificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc <= 24.9:
            return "Normal"
        elif 25.0 <= imc <= 29.9:
            return "Sobrepeso"
        elif 30.0 <= imc <= 34.9:
            return "Obesidad grado I"
        elif 35.0 <= imc <= 39.9:
            return "Obesidad grado II"
        else:  # imc >= 40.0
            return "Obesidad grado III (mórbida)"

    # método que devuelve rango de peso "normal" para su altura
    def rango_peso_normal(self):
        h2 = self.__altura ** 2
        peso_min = 18.5 * h2
        peso_max = 24.9 * h2
        return peso_min, peso_max

    # método para mostrar resumen
    def resumen(self):
        imc = self.calcular_imc()
        categoria = self.clasificar_imc()
        pmin, pmax = self.rango_peso_normal()
        return {
            "peso": self.__peso,
            "altura": self.__altura,
            "imc": imc,
            "categoria": categoria,
            "peso_normal_min": pmin,
            "peso_normal_max": pmax
        }


def pedir_numero(mensaje):
    while True:
        s = input(mensaje).strip()
        try:
            v = float(s)
            return v
        except ValueError:
            print("Entrada inválida. Ingresa un número (ej: 70, 1.75).")

def main():
    print("=== Calculadora IMC (con clases y encapsulamiento) ===")
    peso = pedir_numero("Ingrese su peso en kg (ej: 70.5): ")
    altura = pedir_numero("Ingrese su altura en metros (ej: 1.75): ")

    persona = Persona(peso, altura)
    datos = persona.resumen()

    print("\n--- Resultado ---")
    print(f"Peso: {datos['peso']:.2f} kg")
    print(f"Altura: {datos['altura']:.2f} m")
    print(f"IMC: {datos['imc']:.2f}")
    print(f"Categoría: {datos['categoria']}")
    print(f"Rango de peso 'normal' para esa altura: {datos['peso_normal_min']:.2f} kg - {datos['peso_normal_max']:.2f} kg")

if _name_ == "_main_":
    main()
