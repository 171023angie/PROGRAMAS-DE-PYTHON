class Empleado:
    def _init_(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def aplicar_aumento(self):
        if self.cargo == "Gerente":
            self.salario *= 1.10  
        elif self.cargo == "Supervisor":
            self.salario *= 1.07  
        elif self.cargo == "Operario":
            self.salario *= 1.05 
        else:
            print("Cargo no reconocido, no se aplicará aumento.")


empleado1 = Empleado("Carlos", "Gerente", 2000)


print(f"Salario inicial de {empleado1.nombre}: ${empleado1.salario:.2f}")
empleado1.aplicar_aumento()
print(f"Salario con aumento: ${empleado1.salario:.2f}")
