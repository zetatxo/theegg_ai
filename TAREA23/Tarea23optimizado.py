""" CIFRADO CON SOLITARIO: Para la resolución de este ejercicio, utilizo la opción descrita en la web,
en la que se utiliza una clave secreta en el último de los pasos. Defino en la parte inicial los datos necesarios
que serán la clave, la relación letra-número para la conversión, y la relación carta-número para generar la ristra.
No se necesita ningún módulo para su ejecución"""

# La clave para el paso 4 del cifrado/descifrado
clave = "EZEZDUTUTZIKOINORINIREBARNEANAGINTZENZUINORZARATAALAEREMENPERATZENDIDAZULASTOUSTELAIZANGONAIZBAKARRIKDAKITALANAIZELA"

# Diccionario para convertir letras en números y viceversa
letras = {" ": 0,"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,
"W":23,"X":24,"Y":25,"Z":26}

# Cartas de la baraja con su valor para generar la ristra de valor con solitario
solitario = {"T1":1,"T2":2,"T3":3,"T4":4,"T5":5,"T6":6,"T7":7,"T8":8,"T9":9,"T10":10,"TJ":11,"TQ":12,
"TK":13,"D1":14,"D2":15,"D3":16,"D4":17,"D5":18,"D6":19,"D7":20,"D8":21,"D9":22,"D10":23,"DJ":24,"DQ":25,
"DK":26,"C1":27,"C2":28,"C3":29,"C4":30,"C5":31,"C6":32,"C7":33,"C8":34,"C9":35,"C10":36,"CJ":37,"CQ":38,
"CK":39,"P1":40,"P2":41,"P3":42,"P4":43,"P5":44,"P6":45,"P7":46,"P8":47,"P9":48,"P10":49,"PJ":50,"PQ":51,
"PK":52,"jokA":53,"jokB":53} 

# devolverLetra convierte la lista de numeros en letras, la ultima conversión en cifrado/descifrado
def devolverLetra(numero):
    for i, num in letras.items():
        if num == numero:
            num = letras[i]
            return i

""" Creo la funcion crearRistra para poder utilizarla tanto en el cifrado como en el descifrado. Dentro de ella
se describen cada uno de los pasos necesarios para crear el listado de números de la ristra del solitario"""
def crearRistra(solitario, clave, frase_input):
    # Creo una lista con la clave, otra con las cartas y defino la lista que contendrá el resultado
    clave_list = list(clave)
    solitario_list = list(solitario.keys())
    resultado = list()
    for i in range (0, len(frase_input)): # Para cada letra de la frase introducida
        paso_1 = list()
        indice = solitario_list.index("jokA") #Se busca la posición del joker A
        # Se pone detras de la siguiente carta, y si es ultima se pone la primera de la lista
        if indice == 53:
            paso_1 = [solitario_list[0]] + [solitario_list[indice]] + solitario_list[1:-1]
        else:
            paso_1 = solitario_list[:indice] + [solitario_list[indice+1],solitario_list[indice]] + solitario_list[indice+2:]

        paso_2 = list()
        indice_2 = paso_1.index("jokB") #Se busca la posición del joker B 
        #Se situará dos posiciones detrás
        if indice_2 == 52: # Si es la anteultima letra, detrás de la primera
            paso_2 = [paso_1[0]] + [paso_1[indice_2]] + paso_1[1:52] + [paso_1[-1]]
        elif indice_2 == 53: # Si es la ultima, detrás de la segunda de la lista
            paso_2 = paso_1[:2] + [paso_1[indice_2]]+ paso_1[2:-1]
        else: #Si no, dos posiciones detrás
            paso_2 = paso_1[:indice_2] + paso_1[indice_2+1:indice_2+3]+ [paso_1[indice_2]] + paso_1[indice_2+3:]
        paso_3 = list()
        # La cartas delante de el primer joker se intercambian con las de detrás del segundo joker
        indice_A = paso_2.index("jokA") #Posición de joker A en lista
        indice_B = paso_2.index("jokB") #Posición de joker B en lista

        if indice_A < indice_B: # Si joker A está antes de joker B
            paso_3 = paso_2[indice_B+1:] + paso_2[indice_A:indice_B+1] + paso_2[:indice_A]
        else: # Si joker B está antes de joker A
            paso_3 = paso_2[indice_A+1:] + paso_2[indice_B:indice_A+1] + paso_2[:indice_B]
        paso_4 = list()
        """Corte, que corresponde al valor de la ultima carta, será el indice de corte de la baraja"""
        corte = paso_3[-1] 
        # Si la última carta corresponde a un comodín, no se hace nada
        if corte == "jokA" or corte == "jokB": 
            paso_4 = paso_3
        else: # Se situan las posteriores al corte, las anteriores al corte dejando la ultima en su posicion
            valor_corte = solitario[corte]
            paso_4 = paso_3[valor_corte:-1] + paso_3[:valor_corte] + [paso_3[-1]]
        cuenta = clave_list[i] #Extraemos la letra de la clave que corresponda
        valor_cuenta = letras[cuenta] #Buscamos su valor en número en el diccionario letras
        
        cuenta_final = paso_4[valor_cuenta-1] #Obtenemos la carta que corresponde a ese índice
        res = solitario[cuenta_final] #Obtenemos el valor que corresponde a la carta
        if res > 26: #Si el valor es mayor de 26, le restamos 26
            res = res - 26
        solitario_list = paso_4 # Establecemos la posición de las cartas como inicial para la sig letra
        resultado.append(res) #Lo incorporamos a la lista de resultado
    return resultado
""" Definimos el cifrado de la frase"""    
def cifrarSolitario(frase):
    frase_input = list(frase) #Lista de las letras de la frase
    conversion_input = list() #Lista con los numeros correspondientes a la frase
    for i in frase_input: # Convertimos letras de la frase en números
        valor = letras[i]
        conversion_input.append(valor)
    resultado = crearRistra(solitario, clave, frase_input) # Creamos la ristra del solitario
    resultado_final = list() #Resultado de la suma de la frase y ristra de solitario

    for i in range(len(conversion_input)):
        if conversion_input[i] == 0: # Si el valor es un 0, correponde a un espacio, por lo que no sumamos ristra
            resultado_final.append(0)
        elif (conversion_input[i] + resultado[i]) > 26: # Si la suma es mayor a 26, restamos 26 a la suma
            resultado_final.append ((conversion_input[i] + resultado[i])-26)
        else:
            resultado_final.append ((conversion_input[i] + resultado[i])) 

    resultado_solitario = list()
    
    for i in resultado_final: # Para cada valor obtenido de la suma
        letra = devolverLetra(i) # Devolvemos letra
        resultado_solitario.append(letra) #Lo incluimos en el resultado
    return resultado_solitario

"""En descifrarSolitario, definimos como realizar la función inversa al cifrado"""
def descifrarSolitario (cifrado, clave, solitario):
    cifrado_list = list() #Lista obtenida del resultado de cifrarSolitario
    for i in cifrado: #Pasamos letras del cifrado a numeros
        numero = letras[i]
        cifrado_list.append(numero)
    
    resultado = list()
    resultado = crearRistra(solitario, clave, cifrado_list) #Creamos ristra
    resultado_final = list()
    for i in range(len(resultado)):
        if cifrado_list[i] == 0: #Si el numero es cero, corresponde a espacio, dejamos en 0
            valor = 0
            resultado_final.append(valor)
        elif cifrado_list[i] <= resultado[i]: # Si el valor del cifrado es menor que el de la ristra, suma 26
            valor = (cifrado_list[i] + 26) - resultado[i]
            resultado_final.append(valor)
        else:
            valor = cifrado_list[i] - resultado[i] #Si no, se realiza la resta
            resultado_final.append(valor)
    
    resultado_descifrado = list()
    for i in resultado_final: #Se traduce el resultado a letras
        letra = devolverLetra(i)
        resultado_descifrado.append(letra)
    return resultado_descifrado

"""Se ejecuta el programa: Para ello se solicita la frase a encriptar y se ejecuta la función de encriptado.
Se devuelve el texto encriptado. Finalmente se pregunta si se quiere desencriptar y se ejecuta en caso de 
respuesta afirmativa."""

frase = input("Introduce una frase:").upper()
cifrado = cifrarSolitario(frase)
print ("".join(cifrado))

respuesta = input("¿Deseas descifrarlo? (S/N)  "). upper()
if respuesta == "S":
    descifrado = descifrarSolitario(cifrado, clave, solitario)
    print("".join(descifrado))
else:
    print("OK, gracias!!")