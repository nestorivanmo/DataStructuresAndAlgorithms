import random

contador = 0

def Merge(A, p, q, r):
	arrIzq = A[p:q+1]
	arrDer = A[q+1:r+1]
	izq = 0
	der = 0
	global contador 
	for k in xrange(p,r+1):
		if (der >= len(arrDer)) or (izq < len(arrIzq) and arrIzq[izq] < arrDer[der]):
			A[k] = arrIzq[izq]
			izq += 1
			contador += 1
		else:
			A[k] = arrDer[der]
			der += 1
			contador += 1
			

def MergeSort(A, p, r):
	global contador 
	if p >= r:
		contador += 1
		return
	else:
		contador +=1
		q = (p + r ) / 2
		MergeSort(A, p, q)
		MergeSort(A, q + 1, r)
		Merge(A, p, q, r)
	return contador


lista = []
for x in xrange(0,1001):
	lista.append(random.randint(1,1001))
MergeSort(lista, 0, len(lista) - 1	)