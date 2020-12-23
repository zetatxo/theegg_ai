"""Calcular numero de caracteres, numero de palabras y ranking de palabras por numero de uso"""
import re
import codecs
import operator

archivo = "texto.txt"

"""La funcion contaryListarPalabras devuelve el número de palabras y una lista con las palabras del
texto"""
def contaryListarPalabras(archivo):
    palabras = 0
    texto_completo = []
    with codecs.open(archivo, "r", "utf-8") as archivo_lectura:
        for line in archivo_lectura:
            texto = re.findall(r"\b\w+\b", line)
            for palabra in texto:
                palabra_mayus = palabra.upper()
                texto_completo.append(palabra_mayus)
            palabras += (len(texto))
    return palabras, texto_completo

"""La funcion contarCaracteres devuelve el numero de caracteres del texto"""
def contarCaracteres(archivo):
    caracteres = 0
    with codecs.open(archivo, "r", "utf-8") as archivo_lectura:
        for line in archivo_lectura:
            texto = re.findall(r"\w", line)
            caracteres += (len(texto))
    return caracteres

"""clasificarPalabras crea un diccionario con las diferentes palabras del texto y sus apariciones. A partir 
del diccionario crea una lista anidad ordenada de las palabras por numero de apariciones"""
def clasificarPalabras(lista):
    clasificacion = dict()
    for word in lista:
        if word in clasificacion.keys():
            clasificacion[word] += 1
        else:
            clasificacion[word] = 1
    clasificacion_ordenada = sorted(clasificacion.items(), key = operator.itemgetter(1), reverse = True)
    return clasificacion_ordenada

"""Se solicita al usuario que introduzca la direccion y nombre del archivo del que se quiere conocer el número 
de caracteres, de palabras y el ranking de palabras según su uso. Si no tiene un archivo en concreto, se le
proporciona el texto. En caso de que indique una direccion erronea, se indica y se sale del programa."""    
try:
    archivo_contaje = input("Introduzca ubicacion y nombre del archivo o pulse ENTER para utilizar el archivo por defecto: ")
    if archivo_contaje == "":
        archivo_contaje = archivo
    caracteres = contarCaracteres(archivo_contaje)
    palabras, texto = contaryListarPalabras(archivo_contaje)
    print ("El texto tiene " + str(caracteres)+ " caracteres y " + str(palabras) + " palabras.")

    clasif = clasificarPalabras(texto)

    print("El ranking por uso de las palabras es: ")
    for i in clasif:
        if i[1] >= 2:
            print("La palabra " + i[0] + " con " + str(i[1]) + " apariciones ")

    print ("Las demás palabras tienen una única aparición.")
        
except:
    print("La ubicacion del archivo no es correcta.")





        
        
        
