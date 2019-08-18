



ma1 = [[1,2,3],
       [1,2,3],
       [1,2,3]]


ma2 = [[1,2,3],
       [1,2,3],
       [1,2,3]]

re = []

for linha in range(len(ma1)):
       re.append([])
       for colula in range(len(ma2[0])):
              re[linha].append(0)
              for k in range(len(ma1[0])):
                     re[linha][colula] += ma1[linha][k] * ma1[k][colula]

print(re)