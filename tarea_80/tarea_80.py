'''FRACCION IRREDUCIBLE: Se busca que, dado un número de 4 decimales, es decir, desde 0.0001
hasta 0.9999, el algoritmo calcule la fracción irreductible. Dicha fraccion es la que numerador
y denominador son primos entre sí.
Para ello se seguirán dos estrategias:
1. Un bucle for con el que recorreremos todos los números desde el numerador hasta el 1, 
y probamos si tanto denominador como numerador devuelven un entero, y nos quedamos con
los resultados de las divisiones que devuelven entero.
2. Algoritmo de EUCLIDES
   (Referencias:
   - Aditya Y. Bhargava "Algoritmos" Ed. Anaya Multimedia
   - https://es.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)
    
   El algoritmo de Euclides define que, siendo A mayor que B, si A/B = R, MCD (A, B) = MCD (B, R), 
   siendo MCD el máximo comun divisor'''

# OPCION 1: BUCLE FOR

print("Cálculo con bucle FOR")
numero = float(input("Introduzca un numero del 0.001 al 0.999: "))

numerador = int(numero * 10000)
denominador = 10000

for i in range (numerador, 1, -1):
    if numerador % i == 0 and denominador % i == 0:
        numerador = numerador // i
        denominador = denominador // i
print ( str(numerador) + "/" + str(denominador))

#OPCION 2: Teorema de Euclides

print ("Cálculo con el Teorema de Euclides")
numero = float(input("Introduzca un numero del 0.001 al 0.999: "))

numerador = int(numero * 10000)
denominador = 10000

def mcd(a,b):
    resto = a % b
    while resto != 0:
        a = b
        b = resto
        resto = a % b
    return b

mcd = mcd(denominador,numerador)

print(str(numerador // mcd) + "/" + str(denominador // mcd))

