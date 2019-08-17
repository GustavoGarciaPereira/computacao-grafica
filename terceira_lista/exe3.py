'''
3. Implemente uma aplicação que 
leia pelo teclado o raio de um 
círculo (r) e um ponto (x,y), e 
apresente na tela se o ponto está 
dentro ou fora do círculo. Considere 
que o ponto central do círculo está 
na origem.
'''
def esta_dentro_circulo(px,py,x,y):
    if px >= x and py <= y:
        print("dentro")
        return True



r = int(input("Informe o raio do círculo: "))
px = int(input("px: "))
py = int(input("py: "))
flag = False
pontos_c = []
pon_t = ()

pon_t = (0,r)
pontos_c.append(pon_t)
x = 0
y = 0


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
    if (i[0] > px and i[1] > py) and (-i[0] < px and -i[1] < py):
        print("({},{})".format(i[0],i[1]))
        print("dentro")