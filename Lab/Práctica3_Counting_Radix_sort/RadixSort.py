from Node import *

def obtenerElemSinClaves(E):
    Elem = []
    Elem.append("000000") 
    for i in range(1, len(E)):
        Elem.append(E[i][0])
    return Elem

def formaArregloConClaves(B, numCar):
    Btmp = []
    for i in range(len(B)):
        #print(B[i].name)
        Btmp.append([B[i]] * 2)
        #print(Btmp)
        A3 = list(B[i])
        #print(A3)
        Btmp[i][1] = ord(A3[numCar-1])
    return Btmp

def countingSort2(A,k):
    C=[0 for _ in range(k+1)]
    B=[list(0 for _ in range(2)) for _ in range(len(A))]
    for j in range(1, len(A)):
        C[A[j][1]] = C[A[j][1]] + 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, 0, -1):
        B[ C[A[j][1]] ][1] = A[j][1]
        B[ C[A[j][1]] ][0] = A[j][0]
        C[ A[j][1] ] = C[ A[j][1]  ] - 1
    return B

def radixSort(A):
    menor = len(A)
    for x in range(len(A)-1):
        if len(A[x]) < menor:
            menor = len(A[x])
    numCar = menor
    for i in range(numCar, 0, -1):
        cc = formaArregloConClaves(A, i)
        ordenado = countingSort2(cc,122)
        A = obtenerElemSinClaves(ordenado)
    return A

lista = readFromFile()
sattoloCycle(lista)

paises = []
for x in lista:
	paises.append(x.name)

print(paises)
paises.insert(0, "00000")
print(len(paises))
print("Ahora ordenada: ")
paises = radixSort(paises)
paises = paises[1:]
for x in range(len(paises)):
    lista[x].name = paises[x]
    lista[x].id = x+1
printList(lista)






