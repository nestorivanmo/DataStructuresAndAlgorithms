import csv
from random import randrange

class Node:
	id = 0
	city = ""

	def __init__(self, id, city):
		self.id = id
		self.city = city


#append Node objects to a list
def readFromFile():
	lista = []
	with open('country50.csv') as file:
		reader = csv.reader(file, delimiter=',')
		for row in reader:
			x = Node(row[0], row[1])
			if x.name != "city":
				lista.append(x)
	return lista


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
