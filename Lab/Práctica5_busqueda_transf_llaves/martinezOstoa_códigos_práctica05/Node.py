import csv
import random
class Node:
	id = 0
	city = ""

	def __init__(self, id, city):
		self.id = id
		self.city = city


#append Node objects to a list
def readFromFile():
	listOfCities = []
	with open('MOCK_DATA.csv') as file:
		reader = csv.reader(file, delimiter=',')
		for row in reader:
			id = random.randint(1,4294967296)
			x = Node(id, row[0])
			#if x.name != "city"
			listOfCities.append(x)
	return listOfCities


#algorithm for shuffling a list's items
def sattoloCycle(items):
	i = len(items)
	while i > 1:
		i -= 1
		j = randrange(i)
		items[j], items[i] = items[i], items[j]


#algorithm for printing elements in a Node list
def printList(items):
	for x in items:
		print(str(x.id) + ", " + x.city)
