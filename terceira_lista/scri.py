



ma1 = [[1,2,3],
       [1,2,3],
       [1,2,3]]


ma2 = [[1,2,3],
       [1,2,3],
       [1,2,3]]

#1* 1 + 2 * 1 + 3 * 1

for i in range(len(ma1)):
    for j in range(len(ma2)):
        print("{} * {}".format(ma1[i][j],ma1[i][j]))
