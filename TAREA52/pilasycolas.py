"""La pilas se definen como LIFO (Last In First Out) y su manera mas sencilla de
representacion serían las listas"""

# Creamos una clase pila con atributo items de tipo lista
# Esta clase tendra como operaciones apilar, desapilar y verificar si está
# vacia

class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        return self.items == [] # Que devolvera True si está vacía

"""Las colas seran, en cambio FIFO (First In First Out)"""

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self,x):
        self.items.append(x)

    def desencolar(self):
        try:
            self.items.pop(0)
        except IndexError:
            raise ValueError("La lista está vacía")


