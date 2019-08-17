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
        return "dentro"



r = int(input("Informe o raio do círculo: "))
px = int(input("px: "))
py = int(input("py: "))


x = 0
y = 0

print("(0, {})".format(r))

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
        
    print("({},{})\n".format(x,y))
    esta_dentro_circulo(px,py,x,y)

    print("({},{})\n".format(y, x))
    esta_dentro_circulo(px,py,y,x)

    print("({},{})\n".format(y, -x))
    esta_dentro_circulo(px,py,y,-x)

    print("({},{})\n".format(x, -y))
    esta_dentro_circulo(px,py,x,-y)
    
    print("({},{})\n".format(-x, -y))
    esta_dentro_circulo(px,py,-x,-y)

    print("({},{})\n".format(-y, -x))
    esta_dentro_circulo(px,py,-y,-x)

    print("({},{})\n".format(-y, x))
    esta_dentro_circulo(px,py,-y,x)

    print("({},{})\n".format(-x, y))
    esta_dentro_circulo(px,py,-x,y)