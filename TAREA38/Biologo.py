"""Se extrae la idea de la pagina web https://pythonforbiologists.com/sequence-similarity-search, donde se
explica como, utilizando programación dinámica, se crea una matriz con ambas secuencias. Se utiliza una de las
secuencias para definir las columnas y la otra para las filas. Cada base definirá una fila/columna, por lo que
se introducirán valores diferentes en las bases coincidentes y las no coincidentes.
En este caso, yo he definido a diferencia de la pagina previamente mencionada que, si no coinciden las bases de
una secuencia con la de la otra secuencia, la matriz en esa posicion cogerá valor de -1, y en caso de que sean
coincidentes incrementarán el valor en un punto respecto a la posicion anterior en ambas secuencias, si este
anterior no es negativo.
De este modo, obtendré la longitud de la secuencia mayor, buscando el valor maximo de la matriz y con su 
posicion y restando dicha longitud obtendré, de una de las secuencias, la secuencia buscada. """

import numpy as np
# Creo la matriz utilizando la funcion crearMatriz tomando como argumentos 2 listas de secuencias
def crearMatriz (secuencia1, secuencia2):
    col = np.array(secuencia1)
    row = np.array(secuencia2)
    matrix = np.zeros((len(row), len(col)), order = "F")
    fila = 0
    columna = 0
    for i in np.nditer(row, order = "F"):
        while fila < len(row):
            for j in np.nditer(col, order = "F"):
                while columna < len(col):
                    if row[fila] == col[columna]:
                        if matrix[fila-1][columna-1] == 0 or matrix[fila-1][columna-1] == -1:
                            matrix[fila][columna] = 1
                        else:
                            matrix[fila][columna] = matrix[fila-1][columna-1] + 1
                    else:
                        matrix[fila][columna] = -1
                    columna += 1
            columna = 0
            fila += 1
    return matrix

secuencia_uno = 'ATGTCTTCCTCGA'
secuencia_dos = 'TGCTTCCTATGAC'
#Genero las listas a partir del string introducido
sec1 = list(secuencia_uno)
sec2 = list(secuencia_dos)
#Creo la matriz para mis secuencias a comparar
matriz = crearMatriz(sec1, sec2)
#Busco el valor maximo obtenido en la matriz
maximo = int(np.amax(matriz))
print("La mayor secuencia de bases adyacentes es de "+ str(maximo) + " bases")
#Busco la posicion del valor maximo de la matriz
posicion_max = np.where(matriz == np.amax(matriz))
#Extraigo la fila en la que está dicho máximo
fila = posicion_max[0][0]
#Extraigo como resultado la subcadena de la secuencia con la posicion de la fila y longitud de la subsecuencia
resultado = sec2[((fila-maximo)+1):fila+1]
print("Y la secuencia es: " + "".join(resultado))












