import tamanho_vetor

vn = []
#print(tamanho_vetor.calcula_vetor(v))


def normalizar(v):
    tamanho_Vetor = tamanho_vetor.calcula_vetor(v)
    for i in range(len(v)):
        print("",v[i])
        vn.append(v[i]/tamanho_Vetor)
    
    print("vetor normalizado", vn)
    return vn

