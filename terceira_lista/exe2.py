'''
2. Escolha um dos algoritmos de rasterização de círculos. Está aplicação deverá:

    Pedir para o usuário informar o valor do raio do círculo (r)
    Pedir para o usuário informar o ponto central do círculo
    A partir do raio e do ponto central, gerar os pontos (x,y) 
    que formam o círculo e apresentar os mesmos na tela.
'''




r = int(input("Informe o raio do círculo: "))
ponto_centralx = int(input("Informe o ponto central do círculo: x"))
ponto_centraly = int(input("Informe o ponto central do círculo: y"))
x = 0
y = 0
pontos_c = []
pontos = []
pon_t = ()
print("({}, {})".format(ponto_centralx,r+ponto_centraly))
pon_t = (ponto_centralx,r+ponto_centraly)
pontos_c.append(pon_t)
pontos = []
p = 1 - r
y = r

while x < y:
    if p < 0:
        x += 1
        p = p + 2*x + 1
    elif p >= 0:
        x += 1
        y -= 1
        p = p + 2*x - 2*y + 1 
    pon_t = (x,y)
    pontos_c.append(pon_t)
    pon_t = (y,x)
    pontos_c.append(pon_t)
    pon_t = (y,-x)
    pontos_c.append(pon_t)
    pon_t = (y,-x)
    pontos_c.append(pon_t)
    pon_t = (x,-y)
    pontos_c.append(pon_t)
    pon_t = (-x,-y)
    pontos_c.append(pon_t)
    pon_t = (-y,-x)
    pontos_c.append(pon_t)
    pon_t = (-y,x)
    pontos_c.append(pon_t)
    pon_t = (-x,y)
    pontos_c.append(pon_t)

# print(pontos_c)
for i in pontos_c:
    print("({},{})".format(i[0]+ponto_centralx,i[1]+ponto_centraly))