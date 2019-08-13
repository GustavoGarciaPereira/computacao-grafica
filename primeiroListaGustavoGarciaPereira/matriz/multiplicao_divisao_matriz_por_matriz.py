import ler_matriz


def multiplicacao(v):
    ma_lida = ler_matriz.ler_matriz()
    linha_re = []
    matriz_resposta = []
    num = 0
    for i in range(len(v)):
        vt = []
        vt2 = []
        vt = v[i]
        vt2 = ma_lida[i]
        for j in range(len(vt)):
            num += vt[i] * vt2[j]
            print("num", num)
        linha_re.append(num)
        num = 0
        
        matriz_resposta.append(linha_re)
        linha_re = []
    
    return matriz_resposta

def divisao(v):
    ma_lida = ler_matriz.ler_matriz()
    linha_re = []
    matriz_resposta = []
    num = 0
    for i in range(len(v)):
        vt = []
        vt2 = []
        vt = v[i]
        vt2 = ma_lida[i]
        for j in range(len(vt)):
            num += vt[i] / vt2[j]
            print("num", num)
        linha_re.append(num)
        num = 0
        
        matriz_resposta.append(linha_re)
        linha_re = []
    
    return matriz_resposta