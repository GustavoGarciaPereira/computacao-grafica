


def algoritmo_de_Bresenham(p1,p2):
    difx = p2[0] - p1[0]
    dify = p2[1] - p1[1]
    m = dify/difx

    print("{}".format(difx))
    print("{}".format(dify))
    if defx == 0:
        print("reta vetical")
        y = p1[1]
        while (y<=p2[1]):
            print("@")
            y += 1
    
    if m > 1:
        print("")
    print("algoritmo de Bresenham")