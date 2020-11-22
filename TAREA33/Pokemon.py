"""Creo la clase Pokemon donde defino los atributos que deberá tener cada 
instancia de la clase. Genero tambien un método que imprimirá la instancia 
que gane la lucha entre los Pokemon""" 
class Pokemon:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def win(self):
        print (f"Ha ganado {self.nombre}!!")

#Creo las instancias de Pokemon que lucharán con sus atributos
luchador1 = Pokemon("Pikachu", 100, 50)
luchador2 = Pokemon("Jiglypuzz", 100, 45)
#Defino la variable turno, que es la que definirá quien ataca
turno = 1
#Creo el bucle while para que la lucha no finalice hasta que no le quede vida
#a alguno de los dos pokemon
while (luchador1.vida > 0 and luchador2.vida > 0):
    if turno == 1:
        #Resto el ataque del primero a la vida del segundo
        luchador2.vida = luchador2.vida - luchador1.ataque
        #Paso turno al otro pokemon
        turno = 0
    else:
        #Lo mismo que en la parte superior de la condicional pero esta
        #vez con el otro pokemon
        luchador1.vida = luchador1.vida - luchador2.ataque
        turno = 1
#A alguno de los dos pokemon se le ha tenido que acabar la vida, porque si no
#no hubiera salido del bucle
#Si al primer pokemon no le queda vida, gana el segundo
if luchador1.vida <= 0:
    luchador2.win()
else:
#Si no, ha ganado el segundo
    luchador1.win()

