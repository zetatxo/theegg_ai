
def maximo3Numeros(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n1 < n2 and n2 > n3:
        return n2
    else:
        return n3

print("Debes introducir 3 números enteros diferentes")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer y último número: "))

maximo = maximo3Numeros(num1, num2, num3)

print("El número máximo es el " + str(maximo))

