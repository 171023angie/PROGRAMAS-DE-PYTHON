class CalculadoraSuma:
    def __init__(self):
        self.total = 0

    def sumarNumeros(self):
        print("Calcula la suma de números ingresados.")
        print("Escribe un número para sumar. Escribe 'fin' para terminar.")
        
        while True:
            entrada = input("Ingrese un número: ")
            
            if entrada.lower() == "fin":
                break
            
            try:
                numero = float(entrada)   # permite números decimales
                self.total += numero
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número o escriba 'fin' para salir.")
                
        print(f"La suma total es: {self.total}")


def main():
    calculadora = CalculadoraSuma()
    calculadora.sumarNumeros()


if __name__ == "__main__":
    main()
