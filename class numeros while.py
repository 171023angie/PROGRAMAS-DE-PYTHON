class Numeros:
    def _init_(self, cantidad):
        self.cantidad = cantidad
        self.contador = 0

    def generarNumeros(self):
        print("Imprime Numeros")
        while self.contador <= self.cantidad:
            print(self.contador)
            self.contador += 1

def main():
    miNumero = Numeros(10)
    miNumero.generarNumeros()

if __name__ == "__main__":
    main()
