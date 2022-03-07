def busquedaBinaria(lista, elem):
    """Busca un elemento en la lista y devuelve la posicion. En caso de que el
    elemento no este en la lista, devuelve None
    Argumentos: lista: lista en la que se realiza la busqueda
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

print(busquedaBinaria([1, 3, 5, 7, 9], 4))
help(busquedaBinaria)
