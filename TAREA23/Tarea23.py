
clave = "EZEZDUTUTZIKOINORINIREBARNEANAGINTZENZUINORZARATAALAEREMENPERATZENDIDAZU"

letras = {" ": 0,"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,
"W":23,"X":24,"Y":25,"Z":26}

solitario = {"T1":1,"T2":2,"T3":3,"T4":4,"T5":5,"T6":6,"T7":7,"T8":8,"T9":9,"T10":10,"TJ":11,"TQ":12,
"TK":13,"D1":14,"D2":15,"D3":16,"D4":17,"D5":18,"D6":19,"D7":20,"D8":21,"D9":22,"D10":23,"DJ":24,"DQ":25,
"DK":26,"C1":27,"C2":28,"C3":29,"C4":30,"C5":31,"C6":32,"C7":33,"C8":34,"C9":35,"C10":36,"CJ":37,"CQ":38,
"CK":39,"P1":40,"P2":41,"P3":42,"P4":43,"P5":44,"P6":45,"P7":46,"P8":47,"P9":48,"P10":49,"PJ":50,"PQ":51,
"PK":52,"jokA":53,"jokB":53} 

def devolverLetra(numero):
    for i, num in letras.items():
        if num == numero:
            num = letras[i]
            return i

def cifrarSolitario(frase, clave, solitario):
    frase_input = list(frase)
    clave_list = list(clave)
    solitario_list = list(solitario.keys())
    resultado = list()
    conversion_input = list()
    for i in frase_input:
        valor = letras[i]
        conversion_input.append(valor)
    
    for i in range (0, len(frase_input)):
        paso_1 = list()
        indice = solitario_list.index("jokA")

        if indice == 53:
            paso_1 = [solitario_list[0]] + [solitario_list[indice]] + solitario_list[1:-1]
        else:
            paso_1 = solitario_list[:indice] + [solitario_list[indice+1],solitario_list[indice]] + solitario_list[indice+2:]

        paso_2 = list()
        indice_2 = paso_1.index("jokB")

        if indice_2 == 52:
            paso_2 = [paso_1[0]] + [paso_1[indice_2]] + paso_1[1:52] + [paso_1[-1]]
        elif indice_2 == 53:
            paso_2 = paso_1[:2] + [paso_1[indice_2]]+ paso_1[2:-1]
        else:
            paso_2 = paso_1[:indice_2] + paso_1[indice_2+1:indice_2+3]+ [paso_1[indice_2]] + paso_1[indice_2+3:]
        paso_3 = list()
        
        indice_A = paso_2.index("jokA")
        indice_B = paso_2.index("jokB")

        if indice_A < indice_B:
            paso_3 = paso_2[indice_B+1:] + paso_2[indice_A:indice_B+1] + paso_2[:indice_A]
        else:
            paso_3 = paso_2[indice_A+1:] + paso_2[indice_B:indice_A+1] + paso_2[:indice_B]
        paso_4 = list()
        corte = paso_3[-1]

        if corte == "jokA" or corte == "jokB":
            paso_4 = paso_3
        else:
            valor_corte = solitario[corte]
            paso_4 = paso_3[valor_corte:-1] + paso_3[:valor_corte] + [paso_3[-1]]
        cuenta = clave_list[i]
        valor_cuenta = letras[cuenta]
    
        if valor_cuenta == 53:
            solitario_list = paso_4
        else:
            cuenta_final = paso_4[valor_cuenta-1]
            res = solitario[cuenta_final]
            if res > 26:
                res = res - 26
            solitario_list = paso_4
        resultado.append(res)
    
    resultado_final = list()

    for i in range(len(conversion_input)):
        if conversion_input[i] == 0:
            resultado_final.append(0)
        elif (conversion_input[i] + resultado[i]) > 26:
            resultado_final.append ((conversion_input[i] + resultado[i])-26)
        else:
            resultado_final.append ((conversion_input[i] + resultado[i])) 

    resultado_solitario = list()
    
    for i in resultado_final:
        letra = devolverLetra(i)
        resultado_solitario.append(letra)
    return resultado_solitario

def descifrarSolitario (cifrado, clave, solitario):
    cifrado_list = list()
    for i in cifrado:
        letra = letras[i]
        cifrado_list.append(letra)
    
    clave_list = list(clave)
    solitario_list = list(solitario.keys())
    resultado = list()
    
    for i in range (0, len(cifrado_list)):
        paso_1 = list()
        indice = solitario_list.index("jokA")

        if indice == 53:
            paso_1 = [solitario_list[0]] + [solitario_list[indice]] + solitario_list[1:-1]
        else:
            paso_1 = solitario_list[:indice] + [solitario_list[indice+1],solitario_list[indice]] + solitario_list[indice+2:]

        paso_2 = list()
        indice_2 = paso_1.index("jokB")

        if indice_2 == 52:
            paso_2 = [paso_1[0]] + [paso_1[indice_2]] + paso_1[1:52] + [paso_1[-1]]
        elif indice_2 == 53:
            paso_2 = paso_1[:2] + [paso_1[indice_2]]+ paso_1[2:-1]
        else:
            paso_2 = paso_1[:indice_2] + paso_1[indice_2+1:indice_2+3]+ [paso_1[indice_2]] + paso_1[indice_2+3:]
        paso_3 = list()

        indice_A = paso_2.index("jokA")
        indice_B = paso_2.index("jokB")

        if indice_A < indice_B:
            paso_3 = paso_2[indice_B+1:] + paso_2[indice_A:indice_B+1] + paso_2[:indice_A]
        else:
            paso_3 = paso_2[indice_A+1:] + paso_2[indice_B:indice_A+1] + paso_2[:indice_B]
        paso_4 = list()
        corte = paso_3[-1]

        if corte == "jokA" or corte == "jokB":
            paso_4 = paso_3
        else:
            valor_corte = solitario[corte]
            paso_4 = paso_3[valor_corte:-1] + paso_3[:valor_corte] + [paso_3[-1]]
        cuenta = clave_list[i]
        valor_cuenta = letras[cuenta]
    
        if valor_cuenta == 53:
            solitario_list = paso_4
        else:
            cuenta_final = paso_4[valor_cuenta-1]
            res = solitario[cuenta_final]
            if res > 26:
                res = res - 26
            solitario_list = paso_4
        resultado.append(res)
    resultado_final = list()
    for i in range(len(resultado)):
        if cifrado_list[i] == 0:
            valor = 0
            resultado_final.append(valor)
        elif cifrado_list[i] <= resultado[i]:
            valor = (cifrado_list[i] + 26) - resultado[i]
            resultado_final.append(valor)
        else:
            valor = cifrado_list[i] - resultado[i]
            resultado_final.append(valor)
    
    resultado_descifrado = list()
    for i in resultado_final:
        letra = devolverLetra(i)
        resultado_descifrado.append(letra)
    return resultado_descifrado

frase = input("Introduce una frase:").upper()
cifrado = cifrarSolitario(frase, clave, solitario)
print ("".join(cifrado))

respuesta = input("¿Deseas descifrarlo? (S/N)  "). upper()
if respuesta == "S":
    descifrado = descifrarSolitario(cifrado, clave, solitario)
    print("".join(descifrado))
else:
    print("OK, gracias!!")