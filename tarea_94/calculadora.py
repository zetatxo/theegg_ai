"""Módulo que definirá suma, resta, producto y division"""

def sumar(a, b):
    try:
        n1 = float(a)
        n2 = float(b)
        print(n1 + n2)
    except ValueError:
        print("Debe introducir números para ejecutar la función")
    
def restar (a, b):
    try:
        n1 = float(a)
        n2 = float(b)
        print(n1 - n2)
    except ValueError:
        print("Debe introducir números para ejecutar la función")

def multiplicar (a, b):
    try:
        n1 = float(a)
        n2 = float(b)
        print(n1 * n2)
    except ValueError:
        print("Debe introducir números para ejecutar la función")

def dividir (a, b):
    try:
        n1 = float(a)
        n2 = float(b)
        print(n1 / n2)
    except ValueError:
        print("Debe introducir números para ejecutar la función")
    except ZeroDivisionError:
        print("No es posible dividir por 0")
