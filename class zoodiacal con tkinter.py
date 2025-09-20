import tkinter as tk
from tkinter import messagebox

# Función para obtener el signo zodiacal
def signo_zodiaco(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    else:
        return None

# Función para mostrar el resultado
def calcular_signo():
    try:
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        signo = signo_zodiaco(dia, mes)
        
        if signo:
            messagebox.showinfo("Resultado", f"Tu signo zodiacal es: {signo}")
        else:
            messagebox.showerror("Error", "Fecha inválida. Revisa los datos.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Signo Zodiacal")
ventana.geometry("300x200")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Día de nacimiento:").pack(pady=5)
entry_dia = tk.Entry(ventana)
entry_dia.pack()

tk.Label(ventana, text="Mes de nacimiento (1-12):").pack(pady=5)
entry_mes = tk.Entry(ventana)
entry_mes.pack()

# Botón para calcular
tk.Button(ventana, text="Calcular", command=calcular_signo).pack(pady=10)

ventana.mainloop()
