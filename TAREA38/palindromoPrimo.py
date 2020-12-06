"""Un entero es un palindromo si es igual al numero que se obtiene al invertir en orden de sus cifras.En esta tarea
se le dará un entero N, donde 1 <= N <= 1000000. Hay que encontrar el menor entero M, tal que M >= N que es primo
y M es un palindromo de N. La salida debe ser el mas pequeño palindromo primo mayor que o igual a N"""

def esPrimo (numero):
    numeros = list(range(2,numero))
    resultado = 0
    for i in numeros:
        if numero % i == 0:
            resultado += 1
    return resultado

def buscarPalindromoMayor (numero):
    numeros = list(range(numero, 1200000))
    palindromo = []
    numero = list()

    for i in numeros:
        numero = str(i)
        numero.split()
        if numero[::1] == numero[::-1] and len(numero) >= 3:
            palindromo.append(numero)
    return palindromo

num = int(input("Introduzca un numero: "))

pal = buscarPalindromoMayor(num)
for i in pal:
    case = esPrimo(int(i))
    if case == 0:
        print("El palindromo primo mayor es: " + str(i))
        break
    








