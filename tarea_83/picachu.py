"""Se simula una pelea entre Picachu y Jigglypuff. Para ello se les asigna a 
ambos un valor de 100 puntos. En cambio cada ataque de Picachu será de 50 puntos
y de 45 puntos para Jigglypuff. Empieza atacando Picachu hasta que uno de los 
dos no tenga puntos de vida. Finalmente devolveremos el nombre del ganador."""

vidaPicachu = 100
ataquePicachu = 50

vidaJigglypuff = 100
ataqueJigglypuff = 45

turno = 1

while vidaPicachu >= 0 and vidaJigglypuff >= 0:
    if turno == 1:
        vidaJigglypuff = vidaJigglypuff - ataquePicachu
        turno = 0
    else:
        vidaPicachu = vidaPicachu - ataqueJigglypuff
        turno = 1

if vidaPicachu >= 0:
    print("Gana Picachu")
else:
    print("Gana Jigglypuff")