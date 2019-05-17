import random

def MaxHeapify(arr, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  
 
        MaxHeapify(arr, n, largest)
 

def HeapSort(arr):
    n = len(arr)
 
    for i in range(n, -1, -1):
        MaxHeapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   
        MaxHeapify(arr, i, 0)

    return arr

def probarHeapSort(elementos):
	lista = []
	for x in xrange(0,elementos):
		lista.append(random.randint(0,elementos*2))
	print(str(elementos) + "elementos")
	print("\nLista desordenada de: " + str(lista))
	print("\nLista ordenada: " + str(HeapSort(lista)))

probarHeapSort(100)
















