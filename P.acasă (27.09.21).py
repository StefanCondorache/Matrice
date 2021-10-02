matrice=[[],[],[],[],[]]
for i in matrice:
    print('randul',matrice.index(i)+1)
    for j in range(5):
        element=int(input('element: '))
        matrice[matrice.index(i)].append(element)
for i in matrice:
    print('suma randului',matrice.index(i)+1,':',sum(i))
print()
sum2=0
for i in range(5):
    for j in matrice:
        sum2+=j[i]
    print('suma coloanei',i+1,':',sum2)
    sum2=0
print()
dpr=[]
for i in range(5):
    dpr.append(matrice[i][i])
print('diagonala principala: ',*dpr)
dsec,j=[],0
for i in matrice[::-1]:
    dsec.append(i[j])
    j+=1
print('diagonala secundara: ',*dsec)  