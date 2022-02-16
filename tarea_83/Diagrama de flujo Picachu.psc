Algoritmo Picachu
	vidaPicachu <- 100
	ataquePicachu <- 50
	vidaJigglypuff <- 100
	ataqueJigglypuff <- 45
	turno <- 1
	Mientras vidaPichachu>=0 Y vidaJigglypuff>=0 Hacer
		Si turno==1 Entonces
			vidaJigglypuff <- vidaJigglypuff-ataquePicachu
			turno <- 0
		SiNo
			vidaPicachu <- vidaPicachu-ataqueJigglypuff
			turno <- 1
		FinSi
	FinMientras
	Si vidaPicachu>=0 Entonces
		Escribir 'Gana Picachu'
	SiNo
		Escribir 'Gana Jigglypuff'
	FinSi
FinAlgoritmo
