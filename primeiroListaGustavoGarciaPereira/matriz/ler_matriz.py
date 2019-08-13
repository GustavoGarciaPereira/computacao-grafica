

def ler_matriz():
    matriz = []
    linhas_matrix = []
    print("Informe a matriz: ")
    for i in range(3):
        print("\n{} ° - linha\n".format(i+1))

        x = float(input("x{}: ".format(i+1)))
        y = float(input("y{}: ".format(i+1)))
        z = float(input("z{}: ".format(i+1)))

        linhas_matrix.append(x)
        linhas_matrix.append(y)
        linhas_matrix.append(z)

        matriz.append(linhas_matrix)
        linhas_matrix = []
    
    return matriz
