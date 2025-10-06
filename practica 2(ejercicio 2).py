class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        print(f"Cuenta creada a nombre de {self.titular} con saldo inicial de {self.saldo}.")

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de {monto}. Nuevo saldo: {self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto}. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes para el retiro.")

    def __del__(self):
        print(f"Cuenta de {self.titular} cerrada.")


# Programa principal
cuenta1 = CuentaBancaria("Gleny", 1000)

cuenta1.depositar(500)   # Depositar dinero
cuenta1.retirar(300)     # Retirar dinero
cuenta1.retirar(1500)    # Intento de retiro mayor al saldo

# Eliminar el objeto para ejecutar el destructor
del cuenta1
