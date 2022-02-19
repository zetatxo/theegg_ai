"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""

vocales = ("a", "e", "i", "o", "u")

palabra = (input ("Introduzca una palabra: ")).lower()

print (palabra)

sumaVocales = [0, 0, 0, 0, 0]

for letra in palabra:
    for i in range(len(vocales)):
        if letra == vocales[i]:
            sumaVocales[i] += 1

for i in range(len(vocales)):
    print("La palabra tiene " + str(sumaVocales[i]) +" " + vocales[i] + " 's." )
