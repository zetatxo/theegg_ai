lista1 = input("Introduzca una lista de valores separados por comas: ")
lista2 = input("Ahora introduzca una segunda lista de valores también separado por comas: ")

valores1 = lista1.split(sep = ",")
valores2 = lista2.split(sep = ",")

for i in valores1:
    for j in valores2:
        if i == j:
            print( " El valor " + i + " está en ambas listas.")