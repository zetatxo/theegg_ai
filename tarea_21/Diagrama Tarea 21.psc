Algoritmo Tarea21
	Leer a
	num <- a*10000
	den <- 10000
	Para i<-num Hasta 1 Con Paso -1 Hacer
		Si num MOD i==0 Y den MOD i==0 Entonces
			num <- num/i
			den <- den/i
		FinSi
	FinPara
	Escribir num,'/',den
FinAlgoritmo
