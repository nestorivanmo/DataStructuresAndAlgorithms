ins = ('-> ',1)
def getMenuOptions(s):
	if s is 'menu_title':
		return 'Welcome to Bokk'
	if s is 'menu_options':
		return [('(1) Login',0), ('(2) Signup',0),('(3) Exit',0), ins]
def getLoginOptions(s):
	if s is 'login_title':
		return [('Login...',0)]
	if s is 'login_email':
		return [('Email: ',1)]
	if s is 'login_pwd':
		return [('password: ',1)]
def getBadLoginOptions():
	return [('(1) Try again', 0), ('(2) Return', 0), ins]
def getSignUpTitle():
	return [('Signup...',0)]
def getSignUpOptions(s):
	return [(s,1)]
def getFinishSigningUpOptions():
	return [('(1) Confirm data', 0), ('(2) Repeat',0), ('(3) Return',0),ins]
def getTryAgainSignUpOptions():
	return [('(2) Try Again', 0), ('(3) Return',0),ins]
def getMainAppOptions():
	return [('(1) Library', 0), ('(2) Explore', 0), ('(3) Sell',0), ('(4) Sign Out', 0), ins]	
def getLibraryOptions():
	return [('(1) See all my books',0),('(2) Return',0),ins]
def getExploreOptions():
	return [('(1) Find a book',0),('(2) Search by genre',0),('(3) Specials',0),('(4) Return',0),ins]
def getSellOptions():
	return [('(1) Rent a book',0),('(2) Manage my renting books',0),('(3) Return',0),ins]
def getAddBookQuestions():
	return ['(1) title: ', '(2) author: ', '(3) country: ', '(4) ISBN: ', '(5) genre: ', '(6) price of rent per day ($): ', '(7) minimun rental days: ', '(8) maximun rental days: ']
def getAddBookMenuOptions():
	return [('\n(1) Confirm data',0),('(2) Return',0),ins]
def getManageRentingBooksOptions():
	return [('(1) Return',0),ins]
def getFindSpecificBookOptions():
	return ['(1) title: ', '(2) author: ','(3) ISBN: ']
def getSellersMenuOptions():
	return [('\n(1) View Sellers Details',0),('(2) Return',0),ins]
def getSellersSelection():
	return [('\n(0) Return',0),('Select a  seller...',0),ins]