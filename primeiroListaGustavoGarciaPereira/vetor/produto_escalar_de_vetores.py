import ler_vetor


def produto_escalar(v):
    vetor_lido = []
    vator_resultado = []
    produto = 0
    print("Informe um vetor de 3 dimensões: ")

    x = float(input("X: "))
    y = float(input("Y: "))
    z = float(input("Z: "))

    vetor_lido.append(x)
    vetor_lido.append(y)
    vetor_lido.append(z)

    for i in range(len(vetor_lido)):
        vator_resultado.append(v[i]*vetor_lido[i])
        produto += v[i]*vetor_lido[i]

    return produto