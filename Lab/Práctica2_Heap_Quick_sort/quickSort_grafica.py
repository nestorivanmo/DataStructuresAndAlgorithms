import random

contador = 0

def particionar(A,low,high):
	global contador
	pivote = A[high]
	i = ( low - 1 )
	for j in range(low, high):
		contador += 1
		if A[j] <= pivote:
			contador += 1
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i+1], A[high] = A[high], A[i+1]
	return (i + 1)

def quickSort(A, p, r):
	if p < r:
		q = particionar(A, p, r)
		quickSort(A, p, q-1)
		quickSort(A, q+1, r)
	return contador

def graficar(elementos):
	global contador
	lista = []
	x = []
	yTheta = []
	yO = []
	yOmega = []
	for i in xrange(1, elementos+1):
		contador = 0
		x.append(i)
		for j in xrange(1, i+1):
			lista.append(random.randint(-elementos*2,elementos*2))
		yTheta.append(quickSort(lista, 0, len(lista)-1))
		contador = 0
		lista.reverse()
		yOmega.append(quickSort(lista,0,len(lista)-1))
		contador = 0
		lista.sort()
		yO.append(quickSort(lista,0,len(lista)-1))
		contador = 0
	return (x, yTheta, yO, yOmega)


x = []
yTheta = []
yO = []
yOmega = []
(x, yTheta, yO, yOmega) = graficar(10)
print("\nx: " + str(x))
print("\nyTheta: " + str(yTheta) + "\n")
print("\nyO: " + str(yO) + "\n")
print("\nyOmega: " + str(yOmega) + "\n")













