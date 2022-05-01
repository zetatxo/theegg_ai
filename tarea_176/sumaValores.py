def sumaValores(listaValores):
    sumatorio = 0
    for i in lista:
        sumatorio += int(i)
    return sumatorio

numeros = input("Introduzca una lista de valores numeros separados por comas: ")

lista = numeros.split(sep = ",")

suma = sumaValores(lista)

print ("La suma es: " + str(suma))

