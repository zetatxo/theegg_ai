"""Determina si una cadena de texto introducida por el usuario tiene 
una longitud mayor o igual a 5 y a su vez es menor que 10. """

texto = input("Introduzca un texto: ")

longitud = len(texto)

if longitud >= 5 and longitud < 10:
    print("El texto tiene una longitud mayor o igual a 5 y menor a 10")
else:
    print("El texto tiene una longitud menor que 5 o mayor o igual a 10 ")