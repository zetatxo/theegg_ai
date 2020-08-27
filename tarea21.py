# -*- coding: utf-8 -*-
""" OPCION 1: BUCLE FOR
Introducir un numero float de 4 decimales max y buscar la fraccion 
irreductible.
- Multiplicamos el numero introducido por 10000 para que sea int
- numerador: numero introducido
- denominador:  10000
"""

# Convierto el dato introducido a float
a = float(input())
# Utilizo round porque si utilizo int redondea al valor menor entero
num = round(a * 10000) 
den = 10000
# print (num)
# Creo un rango desde el numerador hasta 1 con paso -1 para que divida entre todas las posibilidades
""" Hago el rango de mayor a menor para reducir el numero de iteraciones y porque haciendo 
a la inversa si divido, por ejemplo entre dos, y siguen siendo múltiplos de dos, perdería esa división"""
for i in range(num, 1, -1):
# Si tanto el numerador como el denominador son divisibles entre i, se asignan nuevos denominador y numerador    
    if num % i == 0 and den % i == 0:
        #print(i)
        num = num // i
        #print (num)
        den = den // i
        #print(den)
# Imprimo resultado        
print (str(num) + "/" + str(den))

"""OPCION 2: ALGORITMO DE EUCLIDES 
(Referencias:
- Aditya Y. Bhargava "Algoritmos" Ed. Anaya Multimedia
- https://es.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)
    
El algoritmo de Euclides define que, siendo A mayor que B, si A/B = R, MCD (A, B) = MCD (B, R), 
siendo MCD el máximo comun divisor """

num1 = round(a * 10000)
den1 = 10000
"""Defino una funcion que, una vez calculado el resto, mientras que éste sea diferente a 0 
tome el valor menor (numerador) como el valor mayor, y el resto como el menor  """ 
def mcd (a, b):
    resto = a % b
    while resto != 0:
        a = b
        b = resto
        resto = a % b
    return b
# recojo el resultado de la función en la variable mcd
mcd = mcd(den1, num1)
# Calculo el numerador y denominador resultante de la división por mcd de cada uno
num2 = int(num1/mcd)
den2 = int(den1/mcd)
# Imprimo resultado
print (str(num2) + "/" + str(den2))





         
