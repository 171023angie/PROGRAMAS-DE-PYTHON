class TablaMultiplicar:
    def __init__(self, numero):
        self.numero = numero
        self.resultado = []

    def calcular(self):
        for i in range(1, 11):
            self.resultado.append(i)
            (self.numero)*(i) "=="(self.numero * i)

        return self.resultado

def main():
    miTabla = TablaMultiplicar(6)
    resultado = miTabla.calcular()
    if resultado:
        print(f"Tabla de multiplicar del {miTabla.numero}:")
        for linea in resultado:
            print(linea)

if __name__ == "__main__":
    main()
