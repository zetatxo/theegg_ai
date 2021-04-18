""" Se define un conversor analógico digital. Para ello se define una funcion donde, se calcula el cociente de 2 y su resto, 
guardando el resultado del resto en una lista llamada resultado, y el cociente pasa a ser el nuevo numero a calcular. Esto se realiza mientras
el numero es mayor o igual a dos (en caso de que sea 0, devuelve 0). Si en este proceso el numero coge valor de tres o dos, se añaden a la 
lista tanto el resto como finalmente el cociente. La lista resultado final, será la inversa de resultado, que es el resultante en binario 
del numero introducido. Finalmente se devuelve en formato string."""

def conversorAD (num):
    cociente = 0
    resto = 0
    resultado = list()
    resultado_final = list()
    if num == 0:
        resultado.append(str(0))
    while num >= 2:
        cociente = num // 2 
        resto = num % 2
        if num == 2 or num == 3:
            resultado.append (str(num % 2))
            resultado.append (str(num // 2))
        else:
            resultado.append(str(resto))
        num = cociente
    resultado_final = resultado[::-1]
    return "".join(resultado_final)

num = int(input("Introduce el número que quieres convertir en binario: "))

conversion =conversorAD(num)
print(conversion)
