""" Grupo #3 "Los Yayos"
    Programa que calcule el residuo de una división
    exafinal05 2v.py
"""
import tkinter as tk
from tkinter import ttk

def calcular_residuo():
    dividendo = int(entry_dividendo.get())
    divisor = int(entry_divisor.get())

    if divisor == 0:
        label_residuo.config(text="Error: El divisor no puede ser cero.", foreground="red")
        return

    residuo = dividendo % divisor
    label_residuo.config(text=f"El residuo de la división es: {residuo}", foreground="green")

ventana = tk.Tk()
ventana.title("Calculadora de Residuos")
ventana.geometry("400x150")

frame_residuo = ttk.LabelFrame(ventana, text="Calculadora de Residuos")
frame_residuo.place(x=20, y=20, width=360, height=80)

label_dividendo = ttk.Label(frame_residuo, text="Dividendo:")
label_dividendo.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_dividendo = ttk.Entry(frame_residuo)
entry_dividendo.grid(row=0, column=1, padx=5, pady=5)

label_divisor = ttk.Label(frame_residuo, text="Divisor:")
label_divisor.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_divisor = ttk.Entry(frame_residuo)
entry_divisor.grid(row=1, column=1, padx=5, pady=5)

button_calcular_residuo = ttk.Button(frame_residuo, text="Calcular Residuo", command=calcular_residuo)
button_calcular_residuo.grid(row=2, columnspan=2, padx=5, pady=5)

label_residuo = ttk.Label(ventana, text="", foreground="green")
label_residuo.place(x=20, y=110)

ventana.mainloop()
