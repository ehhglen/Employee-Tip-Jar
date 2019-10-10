def validateNumeric(text):
	while True:
		# Cast text into integer
		try:
			text = int(text)
			break
		except ValueError as e:
			print('Error', e)
			text = input('Please enter a numeric value: ')
	return text 

def validateRange(number, lowRange, highRange):

	while True:
		if number >= lowRange and number <= highRange:
			return number
		else:
			print('Your selection number must be between', lowRange, 'and', highRange)
			number = input('Please enter a correct value: ')
			number = validateNumeric(number)