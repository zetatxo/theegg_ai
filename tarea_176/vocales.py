letra = input("Introduzca una letra: ").capitalize()

vocales = ["A", "E", "I", "O", "U"]
cont = 0
for i in vocales:
    if letra == i:
        cont = 1

if cont == 1:        
    print( "La letra " + letra + " es vocal.")
else:
    print (" La letra " + letra + " no es vocal.")

