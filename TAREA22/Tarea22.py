"""Basado en el capítulo de Programación dinámica del libro "Algoritmos" de Aditya Y.Bhargava. 
La programación dinámica se basa en solucionar subproblemas, y guardar dicha solución, con el fin de no tener que volver a calcularlo cuando
se vuelva a requerir dicha información.
Para ello, se diseña una matriz donde las columnas serán un rango entre el valor mínimo de la lista de objetos y el valor máximo del contenedor, 
en este caso, el peso de las vacas y el peso que soporta el camión. El paso entre dichos valores, nos dará mayor precisión pero también mayor
tiempo de ejecución.
Así, para llegar a la solución final, se irá rellenando la matriz con el valor de producción mayor para cada uno de los pasos del rango 
de pesos, incluyendo en cada fila los valores obtenidos por cada vaca y el posible hueco restante, y comparándolo con los resultados 
de la vaca anterior en el mismo rango de peso.
Utilizamos numpy para manipular arrays 
"""
import numpy as np
# Obtenemos los datos necesarios y los pasamos a int, para introducirlos en una lista
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
# Pasamos los datos a array y creamos un array para los valores de pesos que definirán nuestras columnas
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
                if peso_vacas[fila] == rango[columna]: # Si el peso de la vaca es igual al peso del rango
                    array[fila][columna] = max (produccion_vacas[fila], array[(fila-1), columna])
                    # Seleccionamos el valor max entre la produccion de la vaca y la produccion de la vaca anterior en el mismo rango 
                elif peso_vacas[fila] < rango[columna]: 
                    #Si el peso de la vaca es inferior al rango, puede haber una combinacion de suma de vacas que nos de más productividad
                    indice_array = np.where(rango==(rango[columna]-peso_vacas[fila]))
                    if len(indice_array[0]) > 0:
                        indice = indice_array[0]
                        array[fila][columna] = max(array[(fila-1),columna], 
                                               produccion_vacas[fila]+array[(fila-1),(indice)])
                    else:
                        #Si no hay combinacion posible, hay que comparar entre los valores de la vaca anterior para el mismo rango y éste
                        array[fila,columna] = max(array[(fila-1), columna],produccion_vacas[fila])
                else:
                    #Si el peso de la vaca en mayor al rango, se recoge el valor calculado para la vaca anterior
                    array[fila][columna] = array[(fila-1), columna]
                columna += 1
        columna = 0
        fila +=1
# Se imprime el ultimo valor del array
print(array[-1,-1])
