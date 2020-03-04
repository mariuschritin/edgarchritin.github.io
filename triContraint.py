
import random
import time
from matplotlib.pyplot import*

valx = [2**i for i in range (1,13)]
triC =[]

def creerListe(nVal : int)-> list:
    # Génère une liste de nVal éléments
    # A adapter pour obtenir des couleurs.
    return random.choices((1 , 0),k=nVal)

def creerListe3(nVal : int)-> list:
    # Génère une liste de nVal éléments
    # A adapter pour obtenir des couleurs.
    return random.choices((1 , 0, -1),k=nVal)
def couleurs2(l:list)->list:
	N = len(l)
	lo = 0
	hi = N-1
	print (l)
	while lo <= hi :
		if l[lo] == 1:
			lo +=1
			print(l,"lo:",lo)
		else : 
			l[hi],l[lo] = l[lo],l[hi]
			hi -= 1
			print(l,"hi:",hi)
    #return 

def couleurs3(l:list)->list:
	N = len(l)
	lo = 0
	hi = N-1
	mid = hi
	
	#print (l)
	while lo <= hi+mid :
		if l[lo] == -1:
			
			lo +=1
			#print(l,"lo:",lo)
		elif l[mid] == 1:
			l[mid],l[lo] = l[lo],l[mid]
			lo +=1
			#print(l,"mid:",mid)
		else : 
			l[hi],l[lo] = l[lo],l[hi]
			hi -= 1
			#print(l,"hi:",hi)
    #return

# Génère une liste de 10 éléments
#print(creerListe3(10))

#print (couleurs2(creerListe(10)))

#print (couleurs3(creerListe3(10)))
for i in range(10):
	if couleurs3(creerListe3(10)) == sorted(creerListe3(10)):
		print("oui")
	else:
		print("non")
		
'''

for nval in valx  :
	l = creerListe(nval)
	t1 = time.time()
	couleurs2(l)
	t3 = time.time()-t1
	triC.append(t3)
x = valx
y = triC
plot(x,y,"x-")
show()

'''
