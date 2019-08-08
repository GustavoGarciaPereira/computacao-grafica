import tamanho_vetor
import normalizar_vetor
import soma_vetor
import subtrair_vetor
import multiplicar_escalar

vator_lido = []
print("Informe um vetor de 3 dimensões: ")
x = float(input("X: "))
y = float(input("Y: "))
z = float(input("Z: "))

vator_lido.append(x)
vator_lido.append(y)
vator_lido.append(z)

print(soma_vetor.somar(vator_lido))
print(subtrair_vetor.subtrair(vator_lido))
#print(normalizar_vetor.normalizar(vator_lido))
#print(tamanho_vetor.calcula_vetor(vator_lido))
#print(tamanho_vetor.calcula_vetor(normalizar_vetor.normalizar(vator_lido)))
