import ler_matriz


def adicao(v):
    ma_lida = ler_matriz.ler_matriz()
    linha_re = []
    matriz_resposta = []

    for i in range(len(v)):
        vt = []
        vt2 = []
        vt = v[i]
        vt2 = ma_lida[i]
        for i in range(len(vt)):
            linha_re.append(vt[i] + vt2[i])
        
        
        matriz_resposta.append(linha_re)
        linha_re = []
    
    return matriz_resposta


def subtracao(v):
    ma_lida = ler_matriz.ler_matriz()
    linha_re = []
    matriz_resposta = []

    for i in range(len(v)):
        vt = []
        vt2 = []
        vt = v[i]
        vt2 = ma_lida[i]
        for i in range(len(vt)):
            linha_re.append(vt[i] - vt2[i])
        
        
        matriz_resposta.append(linha_re)
        linha_re = []
    
    return matriz_resposta
        
