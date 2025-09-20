import tkinter as tk
from tkinter import messagebox

class TablaMultiplicar:
    def __init__(self, numero):
        self.numero = numero
        self.resultado = []

    def calcular(self):
        self.resultado.clear()
        for i in range(1, 11):
            self.resultado.append(f"{self.numero} x {i} = {self.numero * i}")
        return self.resultado

def generar_tabla():
    try:
        numero = int(entry_numero.get())
        if numero < 0:
            messagebox.showerror("Error", "Ingrese un número positivo")
            return
        
        miTabla = TablaMultiplicar(numero)
        resultado = miTabla.calcular()

        txt_resultado.delete("1.0", tk.END)  # Limpiar
        for linea in resultado:
            txt_resultado.insert(tk.END, linea + "\n")

    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

# Ventana principal
root = tk.Tk()
root.title("Tabla de Multiplicar")
root.geometry("400x350")

# Etiqueta
lbl_numero = tk.Label(root, text="Ingrese un número:")
lbl_numero.pack(pady=5)

# Entrada de texto
entry_numero = tk.Entry(root)
entry_numero.pack(pady=5)

# Botón
btn_generar = tk.Button(root, text="Generar Tabla", command=generar_tabla, bg="lightblue")
btn_generar.pack(pady=10)

# Caja de texto para mostrar la tabla
txt_resultado = tk.Text(root, height=12, width=30)
txt_resultado.pack(pady=10)

# Iniciar aplicación
root.mainloop()
