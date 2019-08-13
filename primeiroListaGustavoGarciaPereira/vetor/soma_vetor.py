

def somar(v):
    v_soma_re = []
    v_soma = []
    print("informe outro vetor para realizar a soma:")
    v_soma.append(float(input("X: ")))
    v_soma.append(float(input("Y: ")))
    v_soma.append(float(input("Z: ")))

    for i in range(len(v)):
        v_soma_re.append(v_soma[i]+v[i])
    return v_soma_re
        
