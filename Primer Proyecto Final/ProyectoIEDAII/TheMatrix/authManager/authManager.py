from fileManager.fileManager import *
from matrix.tree import *
from blocks.node import Node, User
class AuthManager():
	fm = FileManager()
	usersTree = AVL()
	usersFilePath = ''
	def __init__(self):
		self.usersFilePath = self.fm.getFilePath('userDataBase')
	def authenticateUser(self,email, pwd): 
		userExists,user = self.userExists(email)
		if userExists : 
			if pwd == user.password:
				return True,user,'' 
			else:
				return True,user,'Email or password incorrect'
		else:
			return False,None,'We couldnt find a user with this credentials. Try registering first !'
	def registerNewUser(self,name,lastname,email,password,city,country):
		userInDB = False
		user = User(name,lastname,email,password,city,country,None)
		userInDB,u = self.userExists(user.email)
		if userInDB:
			return userInDB, u, "This user is already registered..."
		else:
			self.registerUser(user)
		return userInDB, user,''
	def registerUser(self,user):
		self.usersTree.insert(user)	
		self.fm.writeUserTreeToFile(self.usersFilePath,self.usersTree)
	def loadTree(self):
		data = self.fm.readFromFile(self.usersFilePath)
		if data != []:
			for user in data:
				self.usersTree.insert(user)
	def userExists(self,email):
		u = self.usersTree.find(email)
		if u is None:
			return False,None
		return True,u
	def updateUser(self,userToUpdate,content):
		userToUpdate.updateRentingBooks(content)
		self.fm.writeUserTreeToFile(self.usersFilePath,self.usersTree)