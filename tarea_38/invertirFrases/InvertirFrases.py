"""Se debe solicitar el numero de frases que se van a introducir. Invertir las palabras de cada una de las
 frases. La salida debe ser Case# + nºfrase + : + " " y las palabras de la frase invertidas"""

"""Creo la funcion invertirFrases que toma como argumento una de las frases y la invierte. Para ello, creo una
lista definiendo cada dato usando como separador el espacio, y los añado en la lista resultado en orden inverso."""
def invertirFrases(sentence):
    frase = sentence.split(sep= " ")
    resultado = []
    for i in range(len(frase)-1, -1, -1):
        resultado.append(frase[i]+ " ")
    return resultado

#Solicito la entrada de los datos
numeroDeCasos = int(input("Introduzca el número de frases que desea introducir: "))
frases = list()
for i in range(1,numeroDeCasos + 1, 1):
    fraseInput = input("Introduzca la frase "+ str(i) + ": ")
    frases.append(fraseInput)

#Llamo a la funcion para cada una de las frases e imprimo el resultado
for i in range(len(frases)):
    invertido = invertirFrases(frases[i])
    print("Case# " + str(i + 1) +": " + "".join(invertido))







