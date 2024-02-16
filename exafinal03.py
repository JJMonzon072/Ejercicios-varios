""" Grupo #3 "Los Yayos"
    Programa que cacule el área de un trapecio
    exafinal03.py
"""
def calcular_area_trapecio(bma, bme, h):
    if bma <= 0 or bme <= 0 or h <= 0:
        raise ValueError("Las longitudes de las bases y la altura deben ser valores positivos.")
    
    area = ((bma + bme) * h) / 2
    return area

try:
    bma = float(input("Ingresa la longitud de la base mayor del trapecio: "))
    bme = float(input("Ingresa la longitud de la base menor del trapecio: "))
    h = float(input("Ingresa la altura del trapecio: "))
    
    area_trapecio = calcular_area_trapecio(bma, bme, h)

    print("El área del trapecio es:", area_trapecio)
except ValueError as e:
    print("Error:", e)
