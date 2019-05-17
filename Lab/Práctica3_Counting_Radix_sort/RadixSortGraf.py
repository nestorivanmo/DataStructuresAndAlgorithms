contador = 0

def obtenerElemSinClavesGraf(E):
    global contador
    Elem = []
    Elem.append("000000") 
    for i in range(1, len(E)):
        contador += 1
        Elem.append(E[i][0])
    return Elem

def formaArregloConClavesGraf(B, numCar):
    Btmp = []
    global contador
    for i in range(len(B)):
        contador += 1
        #print(B[i].name)
        Btmp.append([B[i]] * 2)
        #print(Btmp)
        A3 = list(B[i])
        #print(A3)
        Btmp[i][1] = ord(A3[numCar-1])
    return Btmp

def countingSort2Graf(A,k):
    global contador
    C=[0 for _ in range(k+1)]
    B=[list(0 for _ in range(2)) for _ in range(len(A))]
    for j in range(1, len(A)):
        contador += 1
        C[A[j][1]] = C[A[j][1]] + 1
    for i in range(1, k+1):
        contador += 1
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, 0, -1):
        contador += 1
        B[ C[A[j][1]] ][1] = A[j][1]
        B[ C[A[j][1]] ][0] = A[j][0]
        C[ A[j][1] ] = C[ A[j][1]  ] - 1
    return B

def obtenerMenorGraf(A):
    menor = len(A)
    for x in range(len(A)-1):
        if len(A[x]) < menor:
            menor = len(A[x])
    return menor
def radixSortGraf(A):
    numCar = obtenerMenorGraf(A)
    global contador
    for i in range(numCar, 0, -1):
        contador += 1
        cc = formaArregloConClavesGraf(A, i)
        ordenado = countingSort2Graf(cc,122)
        A = obtenerElemSinClavesGraf(ordenado)
    return contador

lista = readFromFile()
sattoloCycle(lista)
paises = []
for x in lista:
    paises.append(x.name)
paises.insert(0, "00000")
global contador
for x in range(1,51):
    contador = 0
    paises[x:]
    print(len(paises))
