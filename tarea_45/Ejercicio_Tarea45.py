vector = [3,56,21,33,874,123,66,1000,23,45,65,56]

def quickshort (lista): # Algoritmo de ordenacion. Devuelve lista ordenada
    if len(lista) < 2:
        return lista
    else:
        pivote = lista[0]
        menores = [i for i in lista[1:] if i <= pivote]
        mayores = [i for i in lista[1:] if i > pivote]
    return quickshort(menores) + [pivote] + quickshort(mayores)

vectorOrdenado = quickshort(vector)

print(vectorOrdenado)

def secuencial (elemento, lista): # Algoritmo de búsqueda secuencial. Devuelve valor y número de iteraciones realizadas
    iteracion = 0
    for i in range(len(lista)-1):
        iteracion +=1
        if lista[i] == elemento:
            return lista[i], iteracion
    return elemento, None
     
valor, iter = secuencial(874, vectorOrdenado)

if iter == None:
    print(f"El número {valor} no se encuentra en la lista")
else:
    print(f"El número {valor} necesita hacer {iter} iteraciones con búsqueda secuencial")

def binario(elemento, lista): #Algoritmo de búsqueda binaria. Devuelve valor y número de iteraciones
    limiteMenor = 0
    limiteMayor = len(lista) - 1
    iteracion = 0
    while limiteMenor <= limiteMayor:
        valorMedio = (limiteMenor + limiteMayor)//2
        valorEstimado = lista[valorMedio]
        if valorEstimado == elemento:
            iteracion += 1
            return lista[valorMedio], iteracion
        elif valorEstimado < elemento:
            limiteMenor = valorMedio + 1
            iteracion += 1
        else:
            limiteMayor = valorMedio - 1
            iteracion += 1
    return elemento, None

valor, iter = binario(874,vectorOrdenado)

if iter == None:
    print(f"El número {valor} no se encuentra en la lista")
else:
    print(f"El número {valor} necesita {iter} iteraciones para ser encontrado con la búsqueda binaria")




