import random

contador = 0

def MaxHeapify(arr, n, i):
    global contador
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
 
    if l < n and arr[i] < arr[l]:
        contador += 1
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        contador += 1
        largest = r

    if largest != i:
        contador += 1
        arr[i],arr[largest] = arr[largest],arr[i]  
 
        MaxHeapify(arr, n, largest)
 

def HeapSort(arr):
    global contador
    n = len(arr)
 
    for i in range(n, -1, -1):
        contador += 1
        MaxHeapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        contador += 1
        arr[i], arr[0] = arr[0], arr[i]   
        MaxHeapify(arr, i, 0)

    return contador


def graficar(elementos):
    x = []
    yTheta = []
    yO = []
    yOmega = []
    lista = []
    for i in xrange(1, elementos+1):
        x.append(i)
        for j in xrange(1, i+1):
            lista.append(random.randint(1,elementos*2))
        yTheta.append(HeapSort(lista))
        contador = 0
        lista.sort()
        yO.append(HeapSort(lista))
        contador = 0
        lista.reverse()
        yOmega.append(HeapSort(lista))
        contador = 0
    return (x, yTheta, yO, yOmega)

x = []
yTheta = []
yO = []
yOmega = []
(x, yTheta, yO, yOmega) = graficar(10)
print("\nx: " + str(x) + "\n\nyTheta: " + str(yTheta) + "\nyO: " + str(yO) + "\nyOmega: " + str(yOmega))















