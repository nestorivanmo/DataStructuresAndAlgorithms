class Menu():
	def __init__(self,title=None,options=None,reestrictedOptions=None,questions=None,multipleAnswer=False):
		self.options = options
		self.title = title
		self.reestrictedOptions = reestrictedOptions
		self.questions = questions
		self.multipleAnswer = multipleAnswer
	def displayOptions(self, options):
		self.options = options
		for option in options:
			for i in range(len(option)):
				opt = option[i][1]
				content = option[i][0]
				if opt == 0:
					print(content)
				elif opt == 1:
					return raw_input(content) 
	def printTitle(self):
		if self.title != '':
			print(self.title)
	def run(self):
		selectedAns = -1
		self.printTitle()
		selectedAns = self.displayOptions(self.options)
		while selectedAns not in self.reestrictedOptions:
			selectedAns = self.displayOptions(self.options)
			if selectedAns in self.reestrictedOptions:
				return selectedAns
		return selectedAns
	def runMultipleAnswerMenu(self):
		self.printTitle()
		answers = []
		for question in self.questions:
			answer = raw_input(question)
			answers.append(answer)
		selectedAns = -1
		selectedAns = self.displayOptions(self.options)
		while selectedAns not in self.reestrictedOptions:
			selectedAns = self.displayOptions(self.options)
			if selectedAns in self.reestrictedOptions:
				return selectedAns
		return selectedAns,answers