"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

word = input ("Introduzca una palabra: ")
letras = list(word)

if (letras[::1] == letras[::-1]):
    print( word, " es palindromo")
else:
    print(word, " no es palindromo")
