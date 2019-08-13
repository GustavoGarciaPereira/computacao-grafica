



def muntiplicao(v):
    escalar = float(input("Informe o escalar: "))
    linha_re = []
    matriz_resposta = []

    for i in range(len(v)):
        vt = []
        vt = v[i]
        for i in range(len(vt)):
            linha_re.append(vt[i] * escalar)
        
        
        matriz_resposta.append(linha_re)
        linha_re = []
    
    return matriz_resposta


def divisao(v):
    escalar = float(input("Informe o escalar: "))
    linha_re = []
    matriz_resposta = []

    for i in range(len(v)):
        vt = []
        vt = v[i]
        for i in range(len(vt)):
            linha_re.append(vt[i] / escalar)
        
        
        matriz_resposta.append(linha_re)
        linha_re = []
    
    return matriz_resposta