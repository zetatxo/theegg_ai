"""Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un
número impar el proceso debe repetirse hasta que lo introduzca correctamente."""

numImpar = int(input("Introduzca un numero impar: "))

while numImpar % 2 == 0:
    numImpar = int(input("Debe introducir un numero impar: "))

print(numImpar, "es impar")
