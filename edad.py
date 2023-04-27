import csv
import statistics

datos = []

with open('edad.csv', newline='') as archivo:
    lector = csv.reader(archivo)
    next(lector) # saltar la primera fila con los encabezados
    for fila in lector:
        datos.append(float(fila[0])) # suponiendo que el archivo solo tiene una columna de datos

promedio = statistics.mean(datos)
moda = statistics.mode(datos)
mediana = statistics.median(datos)
cuartiles = statistics.quantiles(datos, n=4)

print(f"Promedio: {promedio}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Cuartiles: {cuartiles}")