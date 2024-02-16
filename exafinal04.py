""" Grupo #3 "Los Yayos"
    Programa que calcule el capital final de un interés simple
    exafinal04.py
"""
def calcular_capital_final(ci, i, t):
    if ci <= 0 or i <= 0 or t <= 0:
        raise ValueError("El capital inicial, la tasa de interés y el tiempo deben ser valores positivos.")
    
    cf = ci + ci * (i / 100) * t
    return cf

try:
    capital_inicial = float(input("Ingrese el capital inicial: "))
    tasa_interes = float(input("Ingrese la tasa de interés (%): "))
    tiempo = float(input("Ingrese el tiempo (en años): "))
    
    capital_final = calcular_capital_final(capital_inicial, tasa_interes, tiempo)

    print("El capital final es:", capital_final)
except ValueError as e:
    print("Error:", e)
