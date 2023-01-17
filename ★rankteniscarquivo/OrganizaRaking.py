def atualizaRanking(l1,l2):
    l=[]
    for el in l2:
        if int(el[1])>int(el[3]):
            v=el[0]
            p=el[2]
            posrankv=l1.index(el[0])
            posrankp=l1.index(el[2])
        else:
            v=el[2]
            p=el[0]
            posrankv=l1.index(el[2])
            posrankp=l1.index(el[0])
        if posrankv>posrankp:
            l1.remove(v)
            l1.insert(posrankp,v)
    print(l1,'VIROU ISSO')
    for i,el1 in enumerate(l1):
        print(i+1,el1)
    print('\n')
    return l1
      
def lerarqr(l):
    lista=[]
    arq=open(l, 'r')
    for linha in arq:
        linha=linha.strip()
        lista.append(linha)
    return lista

def lerarqp(l):
    lista=[]
    arq=open(l, 'r')
    for linha in arq:
        linha=linha.strip()
        jogo=linha.split(',')
        lista.append(jogo)
    return lista

l1= lerarqr('C:/Users/cance/OneDrive/PUC/Primeiro periodo/INF1025/rankteniscarquivo/ranking.txt')
print(l1)
l2= lerarqp('C:/Users/cance/OneDrive/PUC/Primeiro periodo/INF1025/rankteniscarquivo/partidas.txt')

print(atualizaRanking(l1,l2))