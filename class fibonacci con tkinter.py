import tkinter as tk
from tkinter import messagebox

class Fibonacci:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.serie = []

    def generarSerie(self):
        self.serie.clear()
        a, b = 0, 1
        for _ in range(self.cantidad):
            self.serie.append(a)
            a, b = b, a + b
        return self.serie

def generar():
    try:
        cantidad = int(entry_cantidad.get())
        if cantidad < 0:
            messagebox.showerror("Error", "Ingrese un número positivo")
            return
        
        miFibonacci = Fibonacci(cantidad)
        resultado = miFibonacci.generarSerie()
        txt_resultado.delete("1.0", tk.END)
        txt_resultado.insert(tk.END, ", ".join(map(str, resultado)))
    
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

# Ventana principal
root = tk.Tk()
root.title("Serie de Fibonacci")
root.geometry("400x300")

# Etiqueta
lbl_cantidad = tk.Label(root, text="Cantidad de términos:")
lbl_cantidad.pack(pady=5)

# Entrada
entry_cantidad = tk.Entry(root)
entry_cantidad.pack(pady=5)

# Botón
btn_generar = tk.Button(root, text="Generar Serie", command=generar)
btn_generar.pack(pady=10)

# Caja de texto para mostrar resultados
txt_resultado = tk.Text(root, height=8, width=40)
txt_resultado.pack(pady=10)

# Iniciar aplicación
root.mainloop()
