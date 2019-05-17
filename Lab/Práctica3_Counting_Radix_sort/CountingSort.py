from Node import *


def countingSort(A, maxVal):
	count = [0] * (maxVal + 1)
	for a in A:
		count[int(a.id)] += 1
	i = 0
	for a in range(maxVal + 1):
		for c in range(count[a]):
			A[i].id = a
			i += 1
	return A

lista = readFromFile()
sattoloCycle(lista)
printList(lista)
lista = countingSort(lista,500)
printList(lista)