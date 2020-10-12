import numpy as np

numero_vacas = int(input("Numero de vacas a la venta: "))
peso_camion = int (input("Peso que puede llevar el camión: "))
peso = input("Peso separado por comas de las vacas: ")
pesos =peso.split(",")
input_peso_vacas = []
for i in pesos:
    peso_vaca = int(i)
    input_peso_vacas.append(peso_vaca)

produccion = input("Produccion de leche al día de cada vaca separado por comas: ")
producciones = produccion.split(",")
input_produccion_vacas =[]
for i in producciones:
    produccion_vaca = int(i)
    input_produccion_vacas.append(produccion_vaca)

peso_vacas = np.array(input_peso_vacas)
produccion_vacas = np.array(input_produccion_vacas)
rango = np.arange(peso_vacas.min(), peso_camion + 1, 1)
filas = numero_vacas
columnas = len(rango)
array = np.zeros((filas, columnas))
fila = 0
columna = 0
indice = 0

for i in np.nditer(peso_vacas, order = "F"):
    while fila < len(peso_vacas):
        for j in np.nditer(rango, order = "F"):
            while columna < len(rango):
                if peso_vacas[fila] == rango[columna]:
                    array[fila][columna] = max (produccion_vacas[fila], array[(fila-1), columna])
                elif peso_vacas[fila] < rango[columna]:
                    indice_array = np.where(rango==(rango[columna]-peso_vacas[fila]))
                    if len(indice_array[0]) > 0:
                        indice = indice_array[0]
                        array[fila][columna] = max(array[(fila-1),columna], 
                                               produccion_vacas[fila]+array[(fila-1),(indice)])
                    else:
                        array[fila,columna] = max(array[(fila-1), columna],produccion_vacas[fila])
                else:
                    array[fila][columna] = array[(fila-1), columna]
                columna += 1
        columna = 0
        fila +=1

print(array[-1,-1])
