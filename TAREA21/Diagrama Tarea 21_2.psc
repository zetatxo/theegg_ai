Funcion b <- mcd (a,b)
	resto <- a MOD b
	Mientras resto<>0 Hacer
		a <- b
		b <- resto
		resto <- a MOD b
	FinMientras
FinFuncion

Algoritmo Tarea21
	Leer a
	num <- a*10000
	den <- 10000
	max <- mcd(den,num)
	num <- num/max
	den <- den/max
	Escribir num,'/',den
FinAlgoritmo
