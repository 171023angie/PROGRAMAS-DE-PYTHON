import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def aplicar_aumento(self):
        if self.cargo.lower() == "gerente":
            porcentaje = 0.10
        elif self.cargo.lower() == "supervisor":
            porcentaje = 0.07
        elif self.cargo.lower() == "operario":
            porcentaje = 0.05
        else:
            porcentaje = 0.0
        return self.salario * (1 + porcentaje)

# Función para procesar empleados
def procesar_empleados():
    try:
        # Crear empleados desde la entrada del usuario
        empleado1 = Empleado(
            entry_nombre1.get(),
            entry_cargo1.get(),
            float(entry_salario1.get())
        )
        empleado2 = Empleado(
            entry_nombre2.get(),
            entry_cargo2.get(),
            float(entry_salario2.get())
        )
        # Empleados predefinidos
        empleado3 = Empleado("Ana", "Interna", 600)
        empleado4 = Empleado("Juan", "Supervisor", 1800)

        empleados = [empleado1, empleado2, empleado3, empleado4]

        # Mostrar resultados en cuadro de texto
        text_resultado.delete("1.0", tk.END)
        for emp in empleados:
            salario_anterior = emp.salario
            salario_nuevo = emp.aplicar_aumento()
            text_resultado.insert(tk.END,
                f"Salario anterior de {emp.nombre} ({emp.cargo}): ${salario_anterior:.2f}\n"
                f"Salario nuevo de {emp.nombre}: ${salario_nuevo:.2f}\n\n"
            )

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos en salario.")

# Interfaz gráfica
root = tk.Tk()
root.title("Cálculo de Aumento de Salario")

# Entrada para empleado 1
tk.Label(root, text="Empleado 1 - Nombre:").grid(row=0, column=0, sticky="w")
entry_nombre1 = tk.Entry(root)
entry_nombre1.grid(row=0, column=1)

tk.Label(root, text="Cargo:").grid(row=1, column=0, sticky="w")
entry_cargo1 = tk.Entry(root)
entry_cargo1.grid(row=1, column=1)

tk.Label(root, text="Salario:").grid(row=2, column=0, sticky="w")
entry_salario1 = tk.Entry(root)
entry_salario1.grid(row=2, column=1)

# Entrada para empleado 2
tk.Label(root, text="Empleado 2 - Nombre:").grid(row=3, column=0, sticky="w")
entry_nombre2 = tk.Entry(root)
entry_nombre2.grid(row=3, column=1)

tk.Label(root, text="Cargo:").grid(row=4, column=0, sticky="w")
entry_cargo2 = tk.Entry(root)
entry_cargo2.grid(row=4, column=1)

tk.Label(root, text="Salario:").grid(row=5, column=0, sticky="w")
entry_salario2 = tk.Entry(root)
entry_salario2.grid(row=5, column=1)

# Botón para calcular
btn_calcular = tk.Button(root, text="Calcular Aumentos", command=procesar_empleados)
btn_calcular.grid(row=6, column=0, columnspan=2, pady=10)

# Cuadro de texto para mostrar resultados
text_resultado = tk.Text(root, width=50, height=12)
text_resultado.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

