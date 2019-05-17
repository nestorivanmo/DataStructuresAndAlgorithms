from Node import * 
import random

counter = 0
def linearSearchImproved(listOfItems, city):
	global counter 
	foundElement = -1
	for k in range(len(listOfItems)):
		counter += 1
		if listOfItems[k].city == city:
			foundElement = k
			break
	return foundElement + 1

listOfItems = readFromFile()
printList(listOfItems)

# Best case -> search for "Malie"
print("Found at place number: " + str(linearSearchImproved(listOfItems, "Malie")) + " with a time of " + str(counter))
counter = 0
# Average case -> search for anything in between "Malie" and "Duraznopampa" -> "Jaquimeyes"
print("Found at place number: " + str(linearSearchImproved(listOfItems, "Jaquimeyes")) + " with a time of " + str(counter))
counter = 0
# Worst case -> search for "Duraznopampa"
print("Found at place number: " + str(linearSearchImproved(listOfItems, "Duraznopampa")) + " with a time of " + str(counter) )
counter = 0

# Graphs

# Best Case 
x = []
yBest = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	x.append(i+1)
	listToIterate = listOfItems[:i+1]
	city = listToIterate[0].city
	linearSearchImproved(listToIterate, city)
	yBest.append(counter)
print(yBest)

# Average Case 
yAverage = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	randomElement = random.randint(0,len(listToIterate)-1)
	city = listToIterate[randomElement].city
	linearSearchImproved(listToIterate, city)
	yAverage.append(counter)
print(yAverage)

# Worst Case 
yWorst = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	city = listToIterate[len(listToIterate)-1].city
	linearSearchImproved(listToIterate, city)
	yWorst.append(counter)
print(yWorst)







