import math
import random

cero = []
uno = []
dos = []
tres = []
cuatro = []
cinco = []
seis = []
siete = []
ocho = []
nueve = []

TAM = 10000
#function that generates n numbers of length 2^32
def generate2exp32numbers(n):
    numbers = []
    for x in range(0,n):
        number = random.randint(0,4294967295)
        if number not in numbers:
            numbers.append(number)
            lista = list(str(number))
            if int(lista[0]) == 0:
                cero.append(number)
            elif int(lista[0]) == 1:
                uno.append(number)
            elif int(lista[0]) == 2:
                dos.append(number)
            elif int(lista[0]) == 3:
                tres.append(number)
            elif int(lista[0]) == 4:
                cuatro.append(number)
            elif int(lista[0]) == 5:
                cinco.append(number)
            elif int(lista[0]) == 6:
                seis.append(number)
            elif int(lista[0]) == 7:
                siete.append(number)
            elif int(lista[0]) == 8:
                ocho.append(number)
            elif int(lista[0]) == 9:
                nueve.append(number)
    return numbers

#function that returns the position of a certain element in a hash table
def hashNestor(number):
    position = ""
    number = str(number)
    lista = list(number)
    for x in range(0,3):
        position += number[random.randint(0,len(number)-1)]
    listaDos = list(position)
    rz = random.randint(1,10)
    if rz < 6:
        if int(lista[0]) == 1 or int(lista[0]) == 2 or int(lista[0]) == 3:
            rr = random.randint(4,9)
            listaDos[0] = rr
    else:
        ra = random.randint(0,2)
        if int(lista[ra]) == 1 or int(lista[ra]) == 2 or int(lista[ra]) == 3:
            listaDos[ra] = random.randint(4,9)

    ps = ""
    for i in range(len(listaDos)):
        ps += str(listaDos[i])
    return int(ps)

#function that generates the hash table
def generateHashTable(numbers):
    positions = []
    for x in range(len(numbers)):
        positions.append(hashNestor(numbers[x]))
    return positions

#function that counts the number of collisions
def countCollisions(positions):
    occurances = []
    collisions = 0
    for x in range(len(positions)):
        if positions[x] not in occurances:
            occurances.append(positions[x])
        else:
            collisions += 1
    return (occurances, collisions)

#Assigning numbers to a hash table of 1000 elements (numberOfElements)
numbers = generate2exp32numbers(TAM)
positions = generateHashTable(numbers)
(occurances,collisions) = countCollisions(positions)
#print(occurances)
print("\n" + str(collisions))

#print("\nCollisions -> " + str(collisions) + "\n")
