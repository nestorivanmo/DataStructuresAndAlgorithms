import os, sys
from uielements.menu import *
from uielements.errors import *
from constants.strings import *
from constants.errorStrings import *
from authManager.authManager import *
from fileManager.fileManager import * 
from bookManager.bookManager import *
class WindowManager():
	menu = Menu()
	error = Error()
	authManager = AuthManager() 
	bookManager = BookManager()
	exploreManager = ExploreManager()
	fm = FileManager()
	userSignedIn = ''
	email = ''
	user = None
	def __init__(self):
		self.userSignedIn,self.email = self.fm.checkIfUserIsSignedIn()
	def getUserSignedIn(self):
		return self.user
	def runApplication(self):
		self.authManager.loadTree()
		if self.userSignedIn == 'True':
			exists,self.user = self.authManager.userExists(self.email)
			self.showMainAppWindow(self.user, False)
		else:
			self.showWindow('welcome')
	def showWindow(self,window):
		if window == 'welcome':
			WelcomeWindow().present()
		if window == 'login':
			LoginWindow().present()
		if window == 'signup':
			SignUpWindow().present()
	def showMainAppWindow(self,user,firstTime):
		MainAppWindow(user,firstTime).present()
	def showLibraryWindow(self,user):
		LibraryWindow(user).present()
	def showExploreWindow(self,user):
		ExploreWindow(user).present()
	def showSellWindow(self,user):
		SellWindow(user).present()	
	def showMenu(self, options):
		return self.menu.displayOptions(options) 
	def setError(self, errorMsg):
		self.error.setError(errorMsg)
	def clearWindow(self):
		os.system('cls' if os.name == 'nt' else 'clear')
	def getOptionsInString(self,num):
		options = []
		x = 1
		while x <= num:
			options.append(str(x))
			x += 1
		return options
class WelcomeWindow(WindowManager):
	def present(self):
		self.clearWindow()
		menuAns = Menu(getMenuOptions('menu_title'), [getMenuOptions('menu_options')], self.getOptionsInString(3)).run()
		if menuAns is '1': 
			self.showWindow('login')
		elif menuAns is '2': 
			self.showWindow('signup')
		elif menuAns is '3':
			print("See u later!")
		else:
			if menuAns is not '3':
				self.setError(getThreeOptionsError())
				self.clearWindow()
class LoginWindow(WindowManager):
	def present(self):
		self.clearWindow()
		self.showMenu([getLoginOptions('login_title')])
		auth = False
		menuAns = ''
		while (auth == False) and (menuAns is not '2'):
			email = self.showMenu([getLoginOptions('login_email')])
			pwd = self.showMenu([getLoginOptions('login_pwd')])
			auth,user,error = self.authManager.authenticateUser(email,pwd)
			if auth:
				if error == '':
					self.fm.writeCurrentAuthUser(self.fm.getFilePath('userSignedIn'), user, True)
					self.showMainAppWindow(user,False)
				else:
					self.setError(error)	
					menuAns = self.showMenu([getBadLoginOptions()])
			else:
				self.setError(error)
				menuAns = self.showMenu([getBadLoginOptions()])
		if menuAns == '2':
			self.showWindow('welcome')
class SignUpWindow(WindowManager):
	def present(self):
		self.clearWindow()
		self.showMenu([getSignUpTitle()])
		menuAns = ''
		signup = True
		while (menuAns is not '1') and (menuAns is not '3'):
			name = self.showMenu([getSignUpOptions('Name: ')])
			lastname = self.showMenu([getSignUpOptions('Last Name: ')])
			email = self.showMenu([getSignUpOptions('Email: ')])
			password = self.showMenu([getSignUpOptions('Password: ')])
			city = self.showMenu([getSignUpOptions('City: ')])
			country = self.showMenu([getSignUpOptions('Country: ')])
			menuAns = self.showMenu([getFinishSigningUpOptions()])
			if menuAns == '1':
				signupError,user,error = self.authManager.registerNewUser(name,lastname,email,password,city,country)
				if signupError:
					if error == '':
						self.setError(getSignUpError())		
					else:
						self.setError(error)					
					menuAns = self.showMenu([getFinishSigningUpOptions()])
				else:
					self.fm.writeCurrentAuthUser(self.fm.getFilePath('userSignedIn'), user, True)
					self.showMainAppWindow(user,True)
			elif menuAns == '2':
				self.clearWindow()
			elif menuAns != '3' and menuAns != '1':
				self.setError(getThreeOptionsError())
				menuAns = self.showMenu([getFinishSigningUpOptions()])
			if menuAns == '3':
				self.showWindow('welcome')
class MainAppWindow(WindowManager):
	def __init__(self,user,firstTime):
		self.user = user 
		self.firstTime = firstTime
		self.bookManager.readBooksFromTree()
	def showIntro(self):
		self.clearWindow()
		if self.firstTime:
			print("Welcome " + self.user.name + ", are you ready?")
		else:
			print("Welcome back " + self.user.name + " !")
	def printUserName(self):
		print("["+self.user.name+"]")
	def present(self):
		self.clearWindow()
		self.showIntro()
		selectedOption = Menu('', [getMainAppOptions()], self.getOptionsInString(4)).run()
		if selectedOption == '1':
			self.showLibraryWindow(self.user)
		if selectedOption == '2':
			self.showExploreWindow(self.user)
		if selectedOption == '3':
			self.showSellWindow(self.user)
		if selectedOption == '4':
			self.fm.writeCurrentAuthUser(self.fm.getFilePath('userSignedIn'), None, False)
			self.showWindow('welcome')
class LibraryWindow(WindowManager):
	def __init__(self, user):
		self.user = user
	def present(self):	
		self.clearWindow()
		selectedOption = Menu('My Library', [getLibraryOptions()], self.getOptionsInString(2)).run()
		if selectedOption == '1':
			pass
		if selectedOption == '2':
			self.showMainAppWindow(self.user, False)
class ExploreWindow(WindowManager):
	def __init__(self,user):
		self.user = user 
	def present(self):
		self.clearWindow()
		selectedOption = Menu('Explore books', [getExploreOptions()], self.getOptionsInString(4)).run()
		if selectedOption == '1':
			self.clearWindow()
			self.bookManager.readBooksFromTree()
			self.authManager.loadTree()
			self.exploreManager.receiveUserAndBookTrees(self.bookManager.bookTree, self.authManager.usersTree)
			option,answers = Menu('Search for a book', [getAddBookMenuOptions()], self.getOptionsInString(len(getAddBookMenuOptions())),getFindSpecificBookOptions(), True).runMultipleAnswerMenu()
			if option == '1':
				b = self.exploreManager.findFromInput(answers)
				if b != None:
					print("Yay, here is your book...")
					self.exploreManager.printBookNicely(b,self.user)
					opt = Menu('', [getSellersMenuOptions()], self.getOptionsInString(2)).run()
					if opt == '1':
						s,updatedDetails = self.exploreManager.printSellersNicely(self.user,b)
						for x in s:
							print(x)
						selectedSeller = Menu('', [getSellersSelection()], self.getOptionsInString(2)).run()
						numOfSeller = int(selectedSeller)-1
						sellerDictionary = updatedDetails[numOfSeller]
						self.user = self.exploreManager.performSell(self.user, b, sellerDictionary, numOfSeller, updatedDetails)
					if opt == '2':
						self.showExploreWindow(self.user)
				else:
					print("Sorry, we could not find that book for you...")
					self.showExploreWindow(self.user)
			if option == '2': 
				self.showExploreWindow(self.user)
		if selectedOption == '4':
			self.showMainAppWindow(self.user, False)
class SellWindow(WindowManager):
	def __init__(self,user):
		self.user = user 
	def present(self):	
		self.clearWindow()
		selectedOption = Menu('Rent a book', [getSellOptions()], self.getOptionsInString(4)).run()
		if selectedOption == '1': #rent a book
			self.clearWindow()
			option,answers = Menu('Add a book', [getAddBookMenuOptions()], self.getOptionsInString(len(getAddBookMenuOptions())),getAddBookQuestions(), True).runMultipleAnswerMenu()
			if option == '1': #add book
				book = self.bookManager.saveBook(answers, self.user)
				self.showSellWindow(self.user)
			if option == '2': #return to sell window
				self.showSellWindow(self.user)
		if selectedOption == '2': #manage my renting books
			self.clearWindow()
			print('My Renting Books')
			self.bookManager.retrieveRentingBooks(self.user)
			option = Menu('', [getManageRentingBooksOptions()], self.getOptionsInString(1),None,False).run()
			if option == '1':
				self.showSellWindow(self.user)
		if selectedOption == '3': #return to main window app 
			self.showMainAppWindow(self.user, False)