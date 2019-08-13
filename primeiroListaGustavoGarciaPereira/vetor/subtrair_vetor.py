

def subtrair(v):
    v_subtrair_re = []
    v_subtrair = []
    print("informe outro vetor para realizar a subitracao:")
    v_subtrair.append(float(input("X: ")))
    v_subtrair.append(float(input("Y: ")))
    v_subtrair.append(float(input("Z: ")))

    for i in range(len(v)):
        v_subtrair_re.append(v_subtrair[i]-v[i])
    return v_subtrair_re