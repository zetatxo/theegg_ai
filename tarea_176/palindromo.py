palabra = input("Introduzca una palabra: ").upper()

palabraInvertida = palabra[::-1]

if palabra == palabraInvertida:
    print ("Es palindromo")
else:
    print("No es palindromo")
