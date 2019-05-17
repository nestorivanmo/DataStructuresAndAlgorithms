import random

def bubble_sort(a, n):
	intercambio = 1
	i = 0
	j = 0
	while i < n-1 and intercambio == 1: 
		intercambio = 0
		for j in xrange(n-i-1):
			if a[j] > a[j + 1]:
				intercambio = 1
				tmp = a[j]
				a[j] = a[j + 1]
				a[j + 1] = tmp
		i += 1
	print(a)


lista = []
for x in xrange(0,250):
	lista.append(random.randint(1,250))

print("Lista desordenada:")
print(lista)
print("\nLista ordenada:")
bubble_sort(lista, 250)

