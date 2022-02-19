"""Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, 
y muestre por pantalla el menor y el mayor de los precios."""

lista = (50, 75, 46, 22, 80, 65, 8)

def minMax(lista):
    minimo = lista[0]
    maximo = lista[0]
    for num in range(len(lista)):
        if minimo > lista[num]:
            minimo = lista[num]
        elif maximo < lista[num]:
            maximo = lista[num]
    return minimo, maximo

min, max = minMax(lista)

print("El valor minimo es ", min)
print("El valor maximo es ", max)

