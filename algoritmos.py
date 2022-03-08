def busquedaBinaria(lista, elem):
    """Busca un elemento en la lista ORDENADA y devuelve la posicion. En caso de que el
    elemento no este en la lista, devuelve None
    Notacion O-Grande = log(n)
    Argumentos: lista: Lista ORDENADA en la que se realiza la busqueda
                elem: Elemento a buscar en la lista"""
    menor = 0
    mayor = len(lista) - 1
    while menor <= mayor:
        medio = int((mayor + menor) / 2)
        estimado = lista[medio]
        if estimado == elem:
            return medio
        if estimado > elem:
            mayor = medio - 1
        else:
            menor = medio + 1
    return None

def quickSort(lista):
    """Ordena una lista utilizando la recursividad. Devuelve la lista ordenada, o
    la lista vacía en el caso base.
    Notacion O-Grande: nlog(n)
    Argumentos: lista: Lista que se desea ordenar"""
    if len(lista) < 2:
        return lista
    else:
        pivote = lista[0]
        menores = [i for i in lista[1:] if i <= pivote]
        mayores = [i for i in lista[1:] if i > pivote]
        return quickSort(menores) + [pivote] + quickSort(mayores)

