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
            
            if entrada.isdigit():  # solo acepta enteros
                numero = int(entrada)
                self.total += numero

                # Verificar si es par o impar
                if numero % 2 == 0:
                    print(f"{numero} es PAR.")
                else:
                    print(f"{numero} es IMPAR.")
            else:
                print("Entrada inválida. Por favor, ingrese un número entero o escriba 'fin' para salir.")
                
        print(f"La suma total es: {self.total}")


def main():
    calculadora = CalculadoraSuma()
    calculadora.sumarNumeros()


if __name__ == "__main__":
    main()
