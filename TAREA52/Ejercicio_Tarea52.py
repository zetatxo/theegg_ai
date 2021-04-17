def sumatorio (lista): #  Sumatorio de los numeros de la lista
    sumatorio = 0
    for numero in lista:
        sumatorio = sumatorio + numero
    return print (f"La suma de los números de la lista es {sumatorio}")

def listarNumerosMenores(lista, elemento): # Devuelve una lista de los numeros menores al elemento proporcionado
    numerosMenores = []
    for numero in lista:
        if numero < elemento:
            numerosMenores.append(numero)
    return numerosMenores

def tuplaOcurrencias(lista): #Devuelve una lista de tuplas con elemento y numero de ocurrencias
    ocurrencias = []
    for numero in lista:
        ocurrencias.append((numero, lista.count(numero)))
    return ocurrencias


# Pedir numeros y guardarlos en una lista. Una vez introducir el 0, parar y no introducir el 0

numeros = []
numero = int(input("Introduzca un número: "))

while numero != 0:
    numeros.append(numero)
    numero = int(input("Introduzca otro numero: "))

print(numeros)

# Solicitar un numero y eliminar su primera ocurrencia, si no enviar mensaje de que no está

eliminado = int(input("Introduzca el número que desea eliminar de la lista: "))

if eliminado in numeros:
    numeros.remove(eliminado)
else:
    print(f"El numero {eliminado} no está en la lista")

print(numeros)

# Suma de todos los elementos
sumatorio(numeros)

# Lista de numeros menores al proporcionado

limite = int(input("Introduzca el valor máximo para la lista de valores: "))

numMenores = listarNumerosMenores(numeros, limite)

for numero in numMenores:
    print(numero)

# Lista de tuplas con numero y ocurrencias

tupla = tuplaOcurrencias(numeros)

for numeros in tupla:
    print (f"El numero {numeros[0]} aparece {numeros[1]} veces.")



