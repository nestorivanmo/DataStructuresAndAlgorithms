class BookDetail():
	def __init__(self, pricePerDay, minRentDays, maxRentDays,status='renting',rentedTo=None):
		self.pricePerDay = pricePerDay
		self.minRentDays = minRentDays
		self.maxRentDays = maxRentDays
		self.status = status
		self.rentedTo = rentedTo
	def getDetail(self):
		return (self.pricePerDay+","+self.minRentDays+","+self.maxRentDays)