""" En esta opcion se recurre a la recursividad. Para ello se realiza el calculo de cociente y resto. En caso de que el cociente sea mayor que
1, se añade el resultado del resto a la lista resultado y se llama a la funcion conversor AD para el cociente. En cado de que no sea mayor que 1,
se añaden a resultado, primero el resto y luego el cociente. Finalmente se crea la lista inversa de resultado y lo devuelve en formato string."""
resultado = list()
resultado_final = list()
def conversorAD (num):
    cociente = num // 2
    resto = num % 2
    if cociente > 1:
        resultado.append(str(resto))
        conversorAD(cociente)
    else:
        resultado.append(str(resto))
        resultado.append(str(cociente))
    resultado_final = resultado[::-1]
    return "".join(resultado_final)

num = int(input("Introduce el número que quieres convertir en binario: "))

conversion =conversorAD(num)
print(conversion)