from Node import *
import random 
import math 


counter = 0
counterForSortingAlgorithms = 0

def binarySearchRecursive(listOfItems, city, leftIndex, rightIndex):
	global counter
	counter += 1
	if leftIndex > rightIndex:
		return -1 
	midIndex = math.floor((leftIndex + rightIndex) / 2)
	midIndex = int(midIndex)
	if listOfItems[midIndex].city == city:
		return midIndex
	elif listOfItems[midIndex].city < city:
		return binarySearchRecursive(listOfItems, city, midIndex+1, rightIndex)
	else:
		return binarySearchRecursive(listOfItems, city, leftIndex, midIndex-1)

def bubble_sort(a):
	global counterForSortingAlgorithms
	interchange = 1
	i = 0
	j = 0
	n = len(a)
	while i < n-1 and interchange == 1: 
		counterForSortingAlgorithms += 1
		interchange = 0
		for j in xrange(n-i-1):
			counterForSortingAlgorithms += 1
			if a[j].city > a[j + 1].city:
				interchange = 1
				a[j].city, a[j+1].city = a[j+1].city, a[j].city
		i += 1
	return a

def Merge(A, p, q, r):
	global counterForSortingAlgorithms
	arrIzq = A[p:q+1]
	arrDer = A[q+1:r+1]
	izq = 0
	der = 0
	for k in xrange(p,r+1):
		if (der >= len(arrDer)) or (izq < len(arrIzq) and arrIzq[izq].city < arrDer[der].city):
			A[k] = arrIzq[izq]
			izq += 1
			counterForSortingAlgorithms += 1
		else:
			A[k] = arrDer[der]
			der += 1
			counterForSortingAlgorithms += 1
			

def MergeSort(A, p, r):
	global counterForSortingAlgorithms
	if p >= r:
		counterForSortingAlgorithms += 1
		return
	else:
		counterForSortingAlgorithms += 1
		q = (p + r ) / 2
		MergeSort(A, p, q)
		MergeSort(A, q + 1, r)
		Merge(A, p, q, r)
	return A



#Bubble Sort

listOfItems = readFromFile()
#printList(listOfItems)
counterForSortingAlgorithms = 0
listOfItems = bubble_sort(listOfItems)
#print("Now sorted: ")
#printList(listOfItems)

counter = 0
print("Binary Search with Bubble Sort")
print("\tLooking for 'Jaquimeyes'")
print("\tFound at: " + str(binarySearchRecursive(listOfItems, 'Jaquimeyes', 0, len(listOfItems)-1)) + " with a time of: " + str(counter + counterForSortingAlgorithms))
counter = 0
print("\tLooking for 'Mexico City'")
print("\tFound at: " + str(binarySearchRecursive(listOfItems, 'Mexico City', 0, len(listOfItems)-1)) + " with a time of: " + str(counter + counterForSortingAlgorithms))


# Graphs 

#Binary Search Best Case 
	# BubbleSort Best Case 
print("Binary Search Best Case")
#print("Bubble Sort Best Case")
listOfItems = readFromFile()
listOfItems = bubble_sort(listOfItems)
counterForSortingAlgorithms = 0
listOfItems = bubble_sort(listOfItems)
x = []
yBest = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	x.append(i+1)
	listToIterate = listOfItems[:i+1]
	mid = math.floor((0 + (len(listToIterate)-1)) / 2)
	city = listToIterate[int(mid)].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yBest.append(counterForSortingAlgorithms + counter)
print(yBest)

	# BubbleSort Average Case 
#print("Bubble Sort Average Case")
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems = bubble_sort(listOfItems)
yAverage = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	mid = math.floor((0 + (len(listToIterate)-1)) / 2)
	city = listToIterate[int(mid)].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yAverage.append(counterForSortingAlgorithms + counter)
print(yAverage)

	# BubbleSort Worst Case
#print("Bubble Sort Worst Case") 
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems.reverse()
listOfItems = bubble_sort(listOfItems)
yWorst = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	mid = math.floor((0 + (len(listToIterate)-1)) / 2)
	city = listToIterate[int(mid)].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yWorst.append(counterForSortingAlgorithms + counter)
print(yWorst)




#Binary Search Average Case 
	# BubbleSort Best Case 
print("Binary Search Average Case")
#print("Bubble Sort Best Case")
listOfItems = readFromFile()
listOfItems = bubble_sort(listOfItems)
counterForSortingAlgorithms = 0
listOfItems = bubble_sort(listOfItems)
x = []
yBest = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	x.append(i+1)
	listToIterate = listOfItems[:i+1]
	randomElement = random.randint(0,len(listToIterate)-1)
	city = listToIterate[randomElement].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yBest.append(counterForSortingAlgorithms + counter)
print(yBest)

	# BubbleSort Average Case
#print("Bubble Sort Average Case")
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems = bubble_sort(listOfItems)
yAverage = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	randomElement = random.randint(0,len(listToIterate)-1)
	city = listToIterate[randomElement].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yAverage.append(counterForSortingAlgorithms + counter)
print(yAverage) 

	# BubbleSort Worst Case 
#print("Bubble Sort Worst Case")
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems.reverse()
listOfItems = bubble_sort(listOfItems)
yWorst = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	randomElement = random.randint(0,len(listToIterate)-1)
	city = listToIterate[randomElement].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yWorst.append(counterForSortingAlgorithms + counter)
print(yWorst)







#Binary Search Worst Case 
print("Binary Search Worst Case")
	# BubbleSort Best Case 
listOfItems = readFromFile()
listOfItems = bubble_sort(listOfItems)
counterForSortingAlgorithms = 0
listOfItems = bubble_sort(listOfItems)
x = []
yBest = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	x.append(i+1)
	listToIterate = listOfItems[:i+1]
	binarySearchRecursive(listToIterate, "xxxxxxxx", 0, len(listToIterate)-1)
	yBest.append(counterForSortingAlgorithms + counter)
print(yBest)

	# BubbleSort Average Case 
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems = bubble_sort(listOfItems)
yAverage = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	binarySearchRecursive(listToIterate, "xxxxxxxx", 0, len(listToIterate)-1)
	yAverage.append(counterForSortingAlgorithms + counter)
print(yAverage) 

	# BubbleSort Worst Case 
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems.reverse()
listOfItems = bubble_sort(listOfItems)
yWorst = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	binarySearchRecursive(listToIterate, "xxxxxxxx", 0, len(listToIterate)-1)
	yWorst.append(counterForSortingAlgorithms + counter)
print(yWorst)






#Merge Sort

listOfItems = readFromFile()
#printList(listOfItems)
counterForSortingAlgorithms = 0
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
#print("Now sorted: ")
#printList(listOfItems)
print("\nBinary Search with Merge Sort")
counter = 0
print("\tLooking for 'Jaquimeyes'")
print("\tFound at: " + str(binarySearchRecursive(listOfItems, 'Jaquimeyes', 0, len(listOfItems)-1)) + str(counter + counterForSortingAlgorithms))
counter = 0
print("\tLooking for 'Mexico City'")
print("\tFound at: " + str(binarySearchRecursive(listOfItems, 'Mexico City', 0, len(listOfItems)-1)) + str(counter + counterForSortingAlgorithms))

# Graphs 

# Binary Search Best Case 
print("Binary Search Best Case")
	# MergeSort Best Case 
listOfItems = readFromFile()
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
counterForSortingAlgorithms = 0
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
x = []
yBest = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	x.append(i+1)
	listToIterate = listOfItems[:i+1]
	mid = math.floor((0 + (len(listToIterate)-1)) / 2)
	city = listToIterate[int(mid)].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yBest.append(counterForSortingAlgorithms + counter)
print(yBest)
		
	# MergeSort Average Case 
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
yAverage = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	mid = math.floor((0 + (len(listToIterate)-1)) / 2)
	city = listToIterate[int(mid)].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yAverage.append(counterForSortingAlgorithms + counter)
print(yAverage)
	# MergeSort Worst Case 
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems.reverse()
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
yWorst = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	mid = math.floor((0 + (len(listToIterate)-1)) / 2)
	city = listToIterate[int(mid)].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yWorst.append(counterForSortingAlgorithms + counter)
print(yWorst)





# Binary Search Average Case 
print("Binary Search Average Case")

listOfItems = readFromFile()
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
counterForSortingAlgorithms = 0
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
x = []
yBest = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	x.append(i+1)
	listToIterate = listOfItems[:i+1]
	randomElement = random.randint(0,len(listToIterate)-1)
	city = listToIterate[randomElement].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yBest.append(counterForSortingAlgorithms + counter)
print(yBest)
		
	# MergeSort Average Case 
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
yAverage = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	randomElement = random.randint(0,len(listToIterate)-1)
	city = listToIterate[randomElement].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yAverage.append(counterForSortingAlgorithms + counter)
print(yAverage)
	# MergeSort Worst Case 
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems.reverse()
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
yWorst = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	randomElement = random.randint(0,len(listToIterate)-1)
	city = listToIterate[randomElement].city
	binarySearchRecursive(listToIterate, city, 0, len(listToIterate)-1)
	yWorst.append(counterForSortingAlgorithms + counter)
print(yWorst)







# Binary Search Worst Case 
print("Binary Search Worst Case")

listOfItems = readFromFile()
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
counterForSortingAlgorithms = 0
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
x = []
yBest = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	x.append(i+1)
	listToIterate = listOfItems[:i+1]
	binarySearchRecursive(listToIterate, "xxxxxxxx", 0, len(listToIterate)-1)	
	yBest.append(counterForSortingAlgorithms + counter)
print(yBest)
		
	# MergeSort Average Case 
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
yAverage = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	binarySearchRecursive(listToIterate, "xxxxxxxx", 0, len(listToIterate)-1)
	yAverage.append(counterForSortingAlgorithms + counter)
print(yAverage)
	# MergeSort Worst Case 
counterForSortingAlgorithms = 0
listOfItems = readFromFile()
listOfItems.reverse()
listOfItems = MergeSort(listOfItems, 0, len(listOfItems)-1)
yWorst = []
listToIterate = []
for i in range(len(listOfItems)):
	counter = 0
	listToIterate = listOfItems[:i+1]
	binarySearchRecursive(listToIterate, "xxxxxxxx", 0, len(listToIterate)-1)
	yWorst.append(counterForSortingAlgorithms + counter)
print(yWorst)



