


def algoritmo_de_Bresenham(p1,p2):
    difx = p2[0] - p1[0] #
    dify = p2[1] - p1[1]
    # print("xxxxxxxxxxxxxxxxxxxxxxxxxx",difx)
    # print("yyyyyyyyyyyyyyyyyyyyyyyyyyy",dify)
    
    #m = difx == 0 or dify/difx and 0
    

    respos = {}
    entre_ponto = []
    linha_rate = ()
    li = []
    #respos['r']
    

    # print("{}".format(difx))
    # print("{}".format(dify))
    # if difx == 0:
    #     print("reta vetical")
    #     y = p1[1]
    #     while (y<=p2[1]):
    #         print("@")
    #         y += 1
    # else:
    #     m = dify/difx    
    #     if m > 1:
    #         print("")
    #     print("algoritmo de Bresenham")
    if p2[0] == p1[0]:
        y=p1[1]
        while y<=p2[1]:
            print("({},{})".format(p1[0],y))
            y+=1
    else:
            
        m = dify/difx
        print(m)
        ajuste = 1
        offset = 0
        if m<=1:
            delta = dify*2
            limiar = difx
            limiarInc= difx*2
            y = p1[1]
            x= p1[0]
            while(x<=p2[0]):
                print("({},{})".format(x,y))
                li.append(x)
                li.append(y)
                entre_ponto.append(li)
                li = []
                offset+=delta
                if offset >= limiar:
                    y+=ajuste
                    limiar+=limiarInc
                x+=1
        elif m > 1:
            delta = difx*2
            limiar = dify
            limiarInc= dify*2
            x = p1[0]
            y=p1[1]
            while y<=p2[1]:
                print("({},{})".format(x,y))
                li.append(x)
                li.append(y)
                entre_ponto.append(li)
                li = []
                offset+=delta
                if offset >= limiar:
                    x+=ajuste
                    limiar+=limiarInc
                y+=1
        
        #respos['r'] = entre_ponto
    return entre_ponto
        
    