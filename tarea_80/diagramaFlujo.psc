Algoritmo fraccionIrreductible
	Leer floatIrreductible
	numIrreductible <- floatIrreductible*1000
	denominador <- 1000
	Para i<-(numIrreductible-1) Hasta 2 Con Paso -1 Hacer
		Si numIrreductible MOD i=0 Y denominador MOD i=0 Entonces
			numIrreductible <- (numIrreductible/i)
			denominador <- (denominador/i)
		FinSi
	FinPara
	Escribir numIrreductible,'/',denominador
FinAlgoritmo
