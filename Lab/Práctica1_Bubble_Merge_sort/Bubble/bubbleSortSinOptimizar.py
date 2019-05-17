import random

lista = []
for x in xrange(0,10):
	lista.append(random.randint(0,50))

print("Lista original: ")
print(lista)

def bubbleSort(a, n):
	i = 1
	j = 0
	contador = 0
	for i in xrange(n-1):
		for j in xrange(n-2):
			if a[j] > a[j+1]:
				tmp = a[j +1 ]
				a[j+1] = a[j]
				a[j] = tmp
			contador += 1
	print(a)

print("Lista ordenada; ")
bubbleSort(lista, 10)

