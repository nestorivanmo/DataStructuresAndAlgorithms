class Error():	
	errorMsg = ""
	def __init__(self):
		pass
	def setError(self, errorMsg):
		self.errorMsg = errorMsg
		print("ERROR: " + str(self.errorMsg))
	def printError(self):
		print("ERROR: " + str(self.errorMsg))