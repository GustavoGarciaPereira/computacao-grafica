'''
1. Desenvolva uma aplicação em que o usuário insere os pontos referentes aos vértices de um triângulo (P0, P1 e P2), 
e então calcule, de acordo com um dos algoritmos de rasterização de linhas, os pontos que fazem parte das arestas 
do triângulo especificado.

Obs: caso escolha o algoritmo de Bresenham para rasterização de linhas, será concedido + 0.5 a nota.'''


import algoritmo_de_Bresenham

x = 0 #int(input("X"))
y = 0 #int(input("Y"))


p1 = (int(input("p1 X: ")),int(input("p1 Y: ")))
p2 = (int(input("p2 X: ")),int(input("p2 Y: ")))
p3 = (int(input("p3 X: ")),int(input("p3 Y: ")))

# p1 = (2,1)
# p2 = (5,7)
# p3 = (0,0)

print("ponto 1",p1)
print("ponto 2",p2)
print("ponto 3",p3)


algoritmo_de_Bresenham.algoritmo_de_Bresenham(p1,p2)
algoritmo_de_Bresenham.algoritmo_de_Bresenham(p1,p3)
algoritmo_de_Bresenham.algoritmo_de_Bresenham(p2,p3)


