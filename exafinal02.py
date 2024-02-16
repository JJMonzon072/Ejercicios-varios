""" Grupo #3 "Los Yayos"
    Programa que calcule el precio de 5 productos comprados en línea
    exafinal02.py
"""
def calcular_precio_total(productos, ubicacion):
    precio_total = sum(productos)
    
    if ubicacion == "capital":
        precio_total += 25
    else:
        precio_total += 45
    
    return precio_total

productos = []

for i in range(5):
    while True:
        try:
            precio_producto = float(input("Ingrese el precio del producto {}: ".format(i + 1)))
            if precio_producto < 0:
                raise ValueError("El precio no puede ser negativo.")
            productos.append(precio_producto)
            break
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico válido.")

while True:
    ubicacion_entrega = input("Ingrese la ubicación de entrega (capital/otro lugar): ").lower()
    if ubicacion_entrega in ["capital", "otro lugar"]:
        break
    else:
        print("Error: Por favor, ingrese 'capital' o 'otro lugar'.")

precio_total = calcular_precio_total(productos, ubicacion_entrega)
print("El precio total de los productos es: {}".format(precio_total))

