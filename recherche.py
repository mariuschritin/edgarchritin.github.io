import random
import time
from matplotlib.pyplot import*

maxVal = 10**8
#nVal = (10**5)

valx = [10**i for i in range (1,9)]



#listeNombres = random.choices(range(maxVal),valx)
tdicho = []
tnaive = []


def rechercheNaive(L: list, elt: int)-> int:
    cnt = 0
    
    for i in L:
        
        if elt == i:
            cnt += 1
            return cnt
        else :
            cnt += 1
    return -1

def rechercheDicho(L: list, elt: int)-> int:
    tr = -1
    deb = 0
    fin = len(L)-1
    cnt = 0
    while tr == -1 and deb <= fin:
        
        cnt += 1
        mil = (deb + fin)//2 
        if L[mil] == elt:
            tr = True
        else:
            if elt > L[mil]:
                deb = mil+1
            else :
                fin = mil-1
        
    
    return tr,cnt


nbr_recherche = -1
for nVal in valx:
    listeNombres = random.choices(range(maxVal),k=nVal)
    l1 = sorted(listeNombres)
    t1 = time.time()

    rechercheDicho(l1,nbr_recherche)

    t2 = time.time()
    t3 = (t2-t1)
    tdicho.append(t3)
    
for nVal in valx:
    listeNombres = random.choices(range(maxVal),k=nVal)
    t1 = time.time()

    rechercheNaive(L1,nbr_recherche)

    t2 = time.time()
    t3 = (t2-t1)
    tnaive.append(t3)
print(tdicho)
print(tnaive)

x = valx
y1 = tdicho
y2 = tnaive
loglog(x,y1,x,y2)
show()
