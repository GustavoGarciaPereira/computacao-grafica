
def calcula_vetor(v):
    soma = 0
    for i in range(len(v)):
        soma += v[i]**2
    
    
    print("soma do vetor",round((soma**(1/2)),2))
    return round((soma**(1/2)),2)


#print(calcula_vetor(v))