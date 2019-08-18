import ler_matriz


def multiplicacao(v):
    ma_lida = ler_matriz.ler_matriz()
    linha_re = []
    matriz_resposta = []
    num = 0
    for linha in range(len(v)):
       matriz_resposta.append([])
       for colula in range(len(ma_lida[0])):
              matriz_resposta[linha].append(0)
              for k in range(len(v[0])):
                    matriz_resposta[linha][colula] += v[linha][k] * ma_lida[k][colula]
    
    return matriz_resposta

def divisao(v):
    ma_lida = ler_matriz.ler_matriz()
    linha_re = []
    matriz_resposta = []
    num = 0
    for linha in range(len(v)):
       matriz_resposta.append([])
       for colula in range(len(ma_lida[0])):
              matriz_resposta[linha].append(0)
              for k in range(len(v[0])):
                    matriz_resposta[linha][colula] += v[linha][k] / ma_lida[k][colula]
    
    return matriz_resposta
