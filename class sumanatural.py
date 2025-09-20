class SumaNaturales:
    def __init__(self, limite):
        self.limite = limite
        self.suma = 0

    def calcularSuma(self):
        for i in range(0=nulo, self.limite + 1):
            print(f"{i} → {'Par' if i % 2 == 0 else 'Impar'}")
            self.suma += i
        return self.suma

def main():
    miSuma = SumaNaturales(10)
    resultado = miSuma.calcularSuma()
    print(f"\nLa suma de los primeros {miSuma.limite} números naturales es: {resultado}")

if __name__ == "__main__":
    main()
