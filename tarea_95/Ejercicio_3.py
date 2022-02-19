"""Realiza un programa que haga la tabla de multiplicación de un número introducido de valor entre 0 y 99:
            Guarda en una variable el número introducido por el usuario
            Añade un filtro que asegure que el número sea entre 0 y 99
            Escribe la tabla multiplicando el valor introducido por valores entre 1 y 10"""

n1 = int(input("Introduzca un número del 0-99: "))

if n1 < 0 or n1 > 99:
    print("Debe intrducir un número del 0-99")
else:
    for i in range(1, 11, 1):
        print(str(n1) + " x " + str(i) + " = " + str(n1 * i))

