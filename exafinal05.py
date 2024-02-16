""" Grupo #3 "Los Yayos"
    Programa que calcule el residuo de una división
    exafinal05.py
"""
def calcular_residuo():
    dividendo = int(input("Ingresa el dividendo: "))
    divisor = int(input("Ingresa el divisor: "))

    if divisor == 0:
        print("Error: El divisor no puede ser cero.")
        return

    residuo = dividendo % divisor

    print("El residuo de la división es:", residuo)

def convertir_temp():
    try:
        temp_cel = float(caja_temp_cel.get())
        temp_kel = temp_cel + 273.15
        temp_far = temp_cel * 1.8 + 32
        etiqueta_temp_kel.config(text= f"Temperatura en °K: {temp_kel}")
        etiqueta_temp_far.config(text= f"Temperatura en °F: {temp_far}")
    except ValueError:
        etiqueta_temp_kel.config(text="Ingrese un valor numérico válido")
        etiqueta_temp_far.config(text="Ingrese un valor numérico válido")
    
import tkinter as tk
from tkinter import ttk

def main():
    ventana = tk.Tk()
    ventana.title("Conversor")
    ventana.geometry("400x300")

    etiqueta_temp_cel = ttk.Label(ventana, text="Temperatura en °C: ")
    etiqueta_temp_cel.place(x=20, y=20)
    caja_temp_cel = ttk.Entry(ventana)
    caja_temp_cel.place(x=140, y=20, width=30)

    boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir_temp)
    boton_convertir.place(x=20, y=60, width=60)

    etiqueta_temp_kel = ttk.Label(ventana, text="Temperatura en °K: ")
    etiqueta_temp_kel.place(x=20, y=120)

    etiqueta_temp_far = ttk.Label(ventana, text="Temperatura en °F: ")
    etiqueta_temp_far.place(x=20, y=160)

    ventana.mainloop()

if __name__ == "__main__":
    main()
