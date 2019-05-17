import random

TAM = 10

lista = [10,20,30,40,50,60,70,80,90,100]

def insertIntoHashTable(cities, arrayIn2D):
    for k in range(TAM):
        key = random.randint(0,TAM-1)
        print(str(key))
        if arrayIn2D[key][0] is None:
            arrayIn2D[key][0] = lista[key]
        else:
            positionToInsert = 0
            while(arrayIn2D[key][positionToInsert] is not None):
                positionToInsert += 1
            arrayIn2D[key][positionToInsert] = lista[key]

def printHashTable(arrayIn2D):
    for i in range(TAM):
        if arrayIn2D[i][0] is not None:
            print(i)
            for j in range(TAM):
                if arrayIn2D[i][j] is not None:
                    print(arrayIn2D[i][j])
