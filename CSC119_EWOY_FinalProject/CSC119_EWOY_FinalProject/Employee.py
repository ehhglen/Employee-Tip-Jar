class Employee:
	def __init__(self, first, last, shift):
		self.firstName = first
		self.lastName = last
		self.whichShift = shift
		self.phoneNumber = ''

	def getFirstName(self):
		return self.firstName

	def getLastName(self):
		return self.lastName

	def getwhichShift(self):
		return self.whichShift

	def getPhoneNumber(self):
		return self.phoneNumber

	def setFirstName(self, first):
		self.firstName = first

	def setLastName(self, last):
		self.lastName = last
	
	def setwhichShift(self, shift):
		self.whichShift = shift

	def setPhoneNumber(self, phone):
		self.phoneNumber = phone

	


class Salaried(Employee):
	def __init__(self, first, last, shift, payRate):
		Employee.__init__(self, first, last)
		self.payrate = payRate

	def getPayrate(self):
		return self.payrate

	def setPayrate(self, payrate):
		self.payrate = payrate

class Hourly(Employee):
	def __init__(self, first, last, shift, tipsEarned):
		Employee.__init__(self, first, last, shift)
		self.wagerate = ''
		self.tipsearned = tipsEarned

	def getWagerate(self):
		return self.wagerate

	def setWagerate(self, wagerate):
		self.wagerate = wagerate
		
	def getTipsEarned(self):
		return self.tipsearned

	def setTips(self, tipsEarned):
		self.tipsearned = tipsEarned

	def __str__(self):
		return self.firstName + ' ' + self.lastName + ' ' + self.whichShift + ' ' + self.tipsearned