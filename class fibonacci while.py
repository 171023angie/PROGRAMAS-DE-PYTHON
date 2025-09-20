class Fibonacci:
    def __init__ (self,cantidad):
        self.cantidad = cantidad
        self.a = 0
        self.b = 1
        self.contador = 0
    def generarSerie(self):
        print ("contador")
        while self.contador < self.cantidad:
            print (self.a,end=" ")
            c=self.a + self.b
            
            self.contador+=1
            
def main():
    miFibonacci = Fibonacci(10)
    miFibonacci.generarSerie()
if __name__=="__main__":
    main()
