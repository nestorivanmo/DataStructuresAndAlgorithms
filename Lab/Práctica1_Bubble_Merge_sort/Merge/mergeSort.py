import random

def Merge(A, p, q, r):
	arrIzq = A[p:q+1]
	arrDer = A[q+1:r+1]
	izq = 0
	der = 0
	for k in xrange(p,r+1):
		if (der >= len(arrDer)) or (izq < len(arrIzq) and arrIzq[izq] < arrDer[der]):
			A[k] = arrIzq[izq]
			izq += 1
		else:
			A[k] = arrDer[der]
			der += 1


def MergeSort(A, p, r):
	if p >= r:
		print("returning")
		return
	else:
		print(str(p) + ":" + str(r))
		q = (p + r ) / 2
		print(q)
		MergeSort(A, p, q)
		MergeSort(A, q + 1, r)
		Merge(A, p, q, r)


lista = []
for x in xrange(0,51):
	lista.append(random.randint(1,1000))
# print(lista)

lista2 = [4,2,3,3,5,7,8,1,3,4,6]
MergeSort(lista, 0, len(lista2) - 1	)
# print(lista)
