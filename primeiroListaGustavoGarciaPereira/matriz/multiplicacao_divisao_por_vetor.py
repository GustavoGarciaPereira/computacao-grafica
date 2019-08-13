




def muntiplicao(v):
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("z: "))
    vetor = []
    vetor.append(x)
    vetor.append(y)
    vetor.append(z)
    num = 0
    linha_re = []
    matriz_resposta = []

    for i in range(len(v)):
        vt = []
        vt = v[i]
        for i in range(len(vt)):
            num += vt[i] * vetor[i]
        linha_re.append(num)
        num = 0
        
        
        #matriz_resposta.append(linha_re)
        #linha_re = []
    
    return linha_re


def divisao(v):
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("z: "))
    vetor = []
    vetor.append(x)
    vetor.append(y)
    vetor.append(z)
    num = 0
    linha_re = []
    matriz_resposta = []

    for i in range(len(v)):
        vt = []
        vt = v[i]
        for i in range(len(vt)):
            num += vt[i] / vetor[i]
        linha_re.append(num)
        num = 0
        
        
        #matriz_resposta.append(linha_re)
        #linha_re = []
    
    return linha_re