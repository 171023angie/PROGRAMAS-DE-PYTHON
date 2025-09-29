import matplotlib.pyplot as plt
import numpy as np

def graficar_funciones():
    print("=== Graficador de funciones lineales ===")
    n = int(input("¿Cuántas funciones lineales deseas graficar? (mínimo 2): "))

    if n < 2:
        print("Debes ingresar al menos 2 funciones.")
        return

    x = np.linspace(-10, 10, 400)  # valores de x de -10 a 10
    
    plt.figure(figsize=(7, 5))   # nueva figura
    plt.axhline(0, color='black', linewidth=1)  # eje X
    plt.axvline(0, color='black', linewidth=1)  # eje Y

    for i in range(n):
        print(f"\nFunción {i+1}: y = m*x + b")
        m = float(input("Ingrese la pendiente m: "))
        b = float(input("Ingrese la ordenada al origen b: "))

        y = m * x + b
        plt.plot(x, y, label=f"y = {m}x + {b}")

    plt.title("Funciones Lineales")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    
    plt.show()

# Ejecutar
graficar_funciones()
