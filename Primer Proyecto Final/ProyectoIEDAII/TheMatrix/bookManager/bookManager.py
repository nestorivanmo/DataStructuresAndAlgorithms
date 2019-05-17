from blocks.node import *
from blocks.bookdetail import *
from authManager.authManager import *
from sortManager.sortManager import *
from fileManager.fileManager import *
from matrix.tree import *
class BookManager():
	bookTree = AVL()
	fileManager = FileManager()
	authManager = AuthManager()
	def insertIntoTree(self,book):
		b = self.checkIfBookExists(self.bookTree,book)
		self.bookTree.insert(b)
		self.fileManager.writeBookTreeToFile(self.fileManager.getFilePath('booksTree'),self.bookTree)
	def checkIfBookExists(self,tree,book):
		b = tree.find(book.key)
		if b is None:
			return book 
		else:
			bookToUpdate = tree.delete(book.key)
			bookToUpdate.updateDetails(book.details[0])
			return bookToUpdate
	def updateBookInfo(self,bookToUpdate,bookUpdated):
		bookToUpdate = bookUpdated
		return bookToUpdate
	def saveBook(self, answers, user):
		content = []
		bookDetails = {}
		bookDetails[user.email] = [answers[5],answers[6],answers[7],'renting',None]
		content.append(bookDetails)
		book = Book(answers[0],answers[1],answers[2],answers[3],answers[4],content)
		details = {}
		details[book.title+"_"+book.author+"_"+book.isbn] = [answers[5],answers[6],answers[7],'renting',None]
		self.authManager.updateUser(user,details)
		self.insertIntoTree(book)
		return book
	def readBooksFromTree(self):
		data = self.fileManager.readFromBookTreeFile(self.fileManager.getFilePath('booksTree'))
		if data != []:
			for book in data:
				b = self.bookTree.find(book.key)
				if b is None:
					self.bookTree.insert(book)
	def retrieveRentingBooks(self,user): 
		print("\nBook - Price Per Day - Min. Rental Days - Max. Rental Days - Status - Rented To\n")
		for d in user.rentingBooks:
			for book,details in d.iteritems():
				title = str(book)
				pos = title.find('_')
				title = title[:pos]
				bookTitle = title
				ppd = str(details[0])
				minrd = str(details[1])
				maxrd = str(details[2])
				status = str(details[3])
				rentedTo = str(details[4])
			print("\t" + bookTitle + " - " + ppd + "-" + minrd + "-" + maxrd + " - " + status + " - "+ rentedTo)
		print("\n")
class ExploreManager():
	bookTree = AVL()
	userTree = AVL()
	sortManager = SortManager()
	fileManager = FileManager()
	def receiveUserAndBookTrees(self, bookTree, userTree):
		self.bookTree = bookTree
		self.userTree = userTree
	def writeToFileUserAndBookTrees(self):
		self.fileManager.writeBookTreeToFile(self.fileManager.getFilePath('booksTree'),self.bookTree)
		self.fileManager.writeUserTreeToFile(self.fileManager.getFilePath('userDataBase'),self.usersTree)
	def findFromInput(self,answers):
		book = self.bookTree.find(answers[0]+"_"+answers[1]+"_"+answers[2])
		if book != None:
			return book 
		return None
	def printBookNicely(self,book,user):
		email = user.email
		numSellers = 0
		if book != None:
			print("\nTitle: " + str(book.title))
			print("Author: " + str(book.author))
			for seller in book.details:
				for key,value in seller.iteritems():
					if email == key:
						pass
					else:
						numSellers += 1
			print("Number of sellers: " + str(numSellers) + "\n")
		else:	
			print("Sorry, we could not complete your request at this time")
	def findUser(self,userEmail):
		user = self.userTree.find(userEmail)
		if user == None:
			return None
		else:
			return user
	def printSellersNicely(self,user,book):
		S = []
		x = 0
		email = user.email
		updatedDetails = []
		for seller in book.details:
				for userEmail, details in seller.iteritems():
					s = ''
					if email == userEmail:
						pass
					else:
						updatedDetails.append(seller)
						x += 1
						user = self.findUser(userEmail)
						s += self.printUserNicely(user, x)
						s += ("\tPrice per day: $" + str(details[0]) + " \n")
						s += ("\tMinimun rental days: " + str(details[1]) + " days\n")
						s += (("\tMinimun rental days: " + str(details[1]) + " days\n"))
						S.append(s)
		return S,updatedDetails
	def printUserNicely(self,user,num):
		if user == None:
			return ("Sorry, this seller is not available anymore")
		else:
			return("\nSeller #" +str(num)+ ": " + str(user.name) + " " + str(user.lastname) + "\n")
	def performSell(self, user, book, sellerDictionary,numOfSeller):
		seller = self.userTree.find(sellerDictionary.keys()[0])
		if seller == None:
			print("Sorry, operation cannot be done at this moment")
		else:
			print(str(user.name) + " wants to rent " + str(book.title) + " from " + str(seller.name))
		return user
			