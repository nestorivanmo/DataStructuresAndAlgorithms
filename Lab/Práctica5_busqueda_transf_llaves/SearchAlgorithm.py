from Node import *;
from HashFunction import*;
import random

TAM = 1000

def fillHashTable(hashTable):
    for x in range(len(hashTable)):
        nList = [random.randint(1,11)]
        hashTable[x] = nList
    return hashTable

def appendToHashTable(hashTable):
    for x in range(len(hashTable)):
        hashTable[x].append(random.randint(1,11))
    return hashTable

def generateHashTable():
    hash_table = [None] * TAM
    return hash_table

def insertIntoHashTable(listOfItems, hashTable):
    for x in range(len(hashTable)):
        key = hashNestor(listOfItems[x].id)
        if hashTable[key] is None:
            hashTable[key] = [listOfItems[x]]
        else:
            hashTable[key].append(listOfItems[x])

def printHashTable(hashTable):
    for i in range(len(hashTable)):
        if hashTable[i] is not None:
            print(str(i) + " -> " + str(len(hashTable[i])))
            for j in range(len(hashTable[i])):
                print("[" + str(hashTable[i][j].id) + "]")

counter = 0
def searchInHashTable(item, hashTable):
    global counter
    numberToLookAt = hashNestor(item)
    if hashTable[numberToLookAt] is None:
        print("NONE")
    else:
        for x in range(len(hashTable[numberToLookAt])):
            counter += 1
            if hashTable[numberToLookAt][x] == item:
                print("IT'S PRESENT")
        print("NOT IN LIST")


cities = readFromFile()
hashTable = generateHashTable()
insertIntoHashTable(cities, hashTable)
printHashTable(hashTable)
searchInHashTable(2197941627, hashTable)

