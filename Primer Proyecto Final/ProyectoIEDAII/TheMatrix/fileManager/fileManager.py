import os,csv,ast
from blocks.node import *
from matrix.tree import *
class FileManager():
	def getFilePath(self,s):
		filepath = ''
		if s == 'userDataBase':
			return 'files/userDataBase.txt'
		if s == 'userSignedIn':
			return 'files/userLogs.txt'
		if s == 'booksTree':
			return 'files/booksTree.txt'
		if s == 'personalLibrary':
			return 'files/personalLibrary.txt'
	def writeUserTreeToFile(self, filepath, tree):
		tree.treeAsList = []
		data = tree.orderedTreeWalk(tree.root)
		elements = []
		for key in data:
			element = tree.find(key)
			elements.append(element)
		with open(filepath, "w") as file:
			for element in elements:
				file.write(element.getUser() + "\n")
			file.close()
	def readFromFile(self,filepath):
		lista = []
		with open(filepath) as file:
			reader = csv.reader(file, delimiter='|')
			for row in reader:
				d = ast.literal_eval(row[6])
				user = User(row[0], row[1], row[2], row[3], row[4], row[5],d) #type of content: [{}]
				lista.append(user)
		return lista
	def writeCurrentAuthUser(self,filepath,user,auth):
		with open(filepath, "w") as file:
			if user is None:
				file.write(str(auth)+"|"+'none')
			else:
				file.write(str(auth)+"|"+user.email)
			file.close()
	def checkIfUserIsSignedIn(self):
		signedIn = ''
		with open(self.getFilePath('userSignedIn')) as file:
			reader = csv.reader(file, delimiter='|')
			for row in reader:
				signedIn = row[0]
				email = row[1]
		return signedIn,email
	def saveBookToFile(self,filepath,book):
		with open(filepath, "a") as file:
			file.write(book.getBook()+"\n")
			file.close()
	def writeBookTreeToFile(self,filepath,superTREE):
		superTREE.treeAsList = []
		info = [] 
		info = superTREE.orderedTreeWalk(superTREE.root)
		elements = []
		for key in info:
			element = superTREE.find(key)
			elements.append(element)
		with open(filepath, "w") as file:
			for element in elements:
				file.write(element.getBook() + "\n")
			file.close()
	def readFromBookTreeFile(self,filepath):
		data = []
		with open(filepath) as file:
			reader = csv.reader(file, delimiter='|')
			for row in reader:
				if row != []:
					d = ast.literal_eval(row[5])
					book = Book(row[0], row[1], row[2], row[3], row[4], d)
					data.append(book)
		return data