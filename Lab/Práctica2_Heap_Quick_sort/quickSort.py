import random 

def particionar(A,low,high):
	pivote = A[high]
	i = ( low - 1 )
	for j in range(low, high):
		if A[j] <= pivote:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i+1], A[high] = A[high], A[i+1]
	return (i + 1)

def quickSort(A, p, r):
	if p < r:
		q = particionar(A, p, r)
		quickSort(A, p, q-1)
		quickSort(A, q+1, r)
	return A


def probarQuickSort(elementos):
	lista = []
	for x in xrange(0,elementos):
		lista.append(random.randint(0,elementos*2))
	print(quickSort(lista, 0,len(lista)-1))	

print("\nLista con 10 elementos")
probarQuickSort(10)
print("\n")

print("\nLista con 100 elementos")
probarQuickSort(100)
print("\n")

