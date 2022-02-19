"""Realiza un programa que lea 2 números por teclado y determine:
Si los dos números son iguales
Si los dos números son diferentes
Si el primero es mayor que el segundo
Si el segundo es mayor o igual que el primero"""

n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

if n1 > n2:
    print("Los números son diferentes y " + str(n1) + " es mayor que " + str(n2))
elif n1 <= n2:
    print(str(n2) + " es mayor o igual que "+ str(n1))
    if n1 == n2:
        print(str(n1) + " y " + str(n2) + " son iguales")
    else:
        print(str(n1) + " y " + str(n2) + " son diferentes")
