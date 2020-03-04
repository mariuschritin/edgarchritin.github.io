
import time
import random
ttri = []
ttrii = []
ttriii = []
tttri = []
tttrii = []
tttriii = []
ttttri = []
ttttrii = []
ttttriii = []
maxVal = 2**14
#nVal = 5
valx = [2**i for i in range (1,10)]
#listeNombres = random.choices(range(maxVal),k=nVal)

def triSelection(l: list)-> list:
	n = len(l)
	for i in range(0,n-1):
		indiceMini = i
		for j in range (i,n):
			if l[j]<l[indiceMini]:
				#print (l)
				indiceMini = j
		temps = l[i]
		l[i]= l[indiceMini]
		l[indiceMini]= temps
		#print(l)

	return

def triInsertion(l: list)-> list:
	n = len(l)
	for i in range (1,n):
		vt = l[i]
		j=i-1
		while j>=0 and vt<l[j]:
			l[j+1]=l[j]
			j=j-1
		l[j+1]=vt
	return l
#listeNombresTriee = triSelection(listeNombres) # trie la liste

#print(listeNombresTriee)



from matplotlib.pyplot import*
for nVal in valx:
    listeNombres = random.choices(range(maxVal),k=nVal)

    t1 = time.time()

    triSelection(listeNombres)

    t2 = time.time()
    t3 = (t2-t1)
    ttri.append(t3)

    t11 = time.time()

    triInsertion(listeNombres)

    t22 = time.time()
    t33 = (t22-t11)
    ttrii.append(t33)

    t111 = time.time()

    sorted(listeNombres)

    t222 = time.time()
    t333 = (t222-t111)
    ttriii.append(t333)


    '''    '''
    listeNombres = sorted(listeNombres)

    tt1 = time.time()

    triSelection(listeNombres)

    tt2 = time.time()
    tt3 = (tt2-tt1)
    tttri.append(tt3)

    tt11 = time.time()

    triInsertion(listeNombres)

    tt22 = time.time()
    tt33 = (tt22-tt11)
    tttrii.append(tt33)

    tt111 = time.time()

    sorted(listeNombres)

    tt222 = time.time()
    tt333 = (tt222-tt111)
    tttriii.append(tt333)

    '''    '''
    listeNombres = sorted(listeNombres,reverse = True)

    ttt1 = time.time()

    triSelection(listeNombres)

    ttt2 = time.time()
    ttt3 = (ttt2-ttt1)
    ttttri.append(ttt3)

    ttt11 = time.time()

    triInsertion(listeNombres)

    ttt22 = time.time()
    ttt33 = (ttt22-ttt11)
    ttttrii.append(ttt33)

    ttt111 = time.time()

    sorted(listeNombres)

    ttt222 = time.time()
    ttt333 = (ttt222-ttt111)
    ttttriii.append(ttt333)

yyy1 = ttttri

yyy11 = ttttrii

yyy111 = ttttriii



yy1 = tttri

yy11 = tttrii

yy111 = tttriii


y1 = ttri
x = valx
y11 = ttrii

y111 = ttriii
'''
semilogy(x,y11,"x-b",x,y1,"x-g",x,y111,"x-r")
semilogy(x,yy1,"x--g",x,yy11,"x--b",x,yy111,"x--r")
semilogy(x,yyy1,":g",x,yyy11,":b",x,yyy111,":r")
'''
plot(x,y111,"x-r")
plot(x,yy111,"x--r")
plot(x,yyy111,":r")
show()


#liste2 = [10,3,7,5,6,1]
#print(triInsertion(liste2))
