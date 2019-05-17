from Node import *
import random

counter = 0
def linearSearchRecursive(listOfItems, city, k):
	global counter
	if k > len(listOfItems):
		return -1
	if listOfItems[k].city == city:
		return k
	counter += 1
	return linearSearchRecursive(listOfItems, city, k+1)

listOfItems = readFromFile()
printList(listOfItems)
# Best case -> search for "Malie"
print("Found at place number: " + str(linearSearchRecursive(listOfItems, "Malie", 0)) + " with a time of " + str(counter))
counter = 0
# Average case -> search for anything in between "Malie" and "Duraznopampa" -> "Jaquimeyes"
print("Found at place number: " + str(linearSearchRecursive(listOfItems, "Jaquimeyes", 0)) + " with a time of " + str(counter))
counter = 0
# Worst case -> search for "Duraznopampa"
print("Found at place number: " + str(linearSearchRecursive(listOfItems, "Duraznopampa", 0)) + " with a time of " + str(counter) )
counter = 0

# Graphs 

# Best case 
x = []
yBest = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	x.append(i+1)
	listToIterate = listOfItems[:i+1]
	city = listToIterate[0].city
	linearSearchRecursive(listToIterate, city, 0) 
	yBest.append(counter + 1)
print(yBest)

# Average Case 
yAverage = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	randomElement = random.randint(0,len(listToIterate)-1)
	city = listToIterate[randomElement].city
	linearSearchRecursive(listToIterate,city, 0) 
	yAverage.append(counter + 1)
print(yAverage)

# Worst Case 
yWorst = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	city = listToIterate[len(listToIterate)-1].city
	linearSearchRecursive(listToIterate, city, 0) 
	yWorst.append(counter + 1)
print(yWorst)








