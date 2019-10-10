# Final Project by Echglene Woy

import Employee
import validation
import sys
 

def main():

	
	# Declare variables

	employeeItems = []
	firstName = ''
	lastName = ''
	shift = 'lunch', 'dinner' 
	tipjar = []

	# Open Employee.txt file and load the data
	try:
		with open('Employee.txt', 'r') as infile:
			for line in infile:
				line = line.rstrip()
				employeeItems = line.split()
				fileEmployee = createEmployee(employeeItems)
				tipjar.append(fileEmployee)
				
	# Exception handling 
	except IOError:
		print('An error has occured opening the file!')
		print('The program will now exit!')
		sys.exit()
	#except: # Had to comment this exception because it would not let program run
	#	print('An error has occured!')
	#	print('The program will now exit!')
	#	#sys.exit()
				

	
	# Display Header
	print('\nEchglene\'s Tip Storage System')
	print('------------------------------')


	# Display Menu
	while True:
		print('\nMain Menu')
		print('---------\n')
		print('1. Add Tips')
		print('2. View Total Tips Earned')
		print('3. View Schedule')
		print('4. Exit Program')
		mainMenuChoice = input('Enter a selection: ')

		# Validate user input
		mainMenuChoice = validation.validateNumeric(mainMenuChoice) 


		# If-Else Statements
		if mainMenuChoice == 1:
			earnedTips = addTips()
			tipjar.append(earnedTips	)
			print(earnedTips.getFirstName(), '|', earnedTips.getLastName(), '|', earnedTips.getwhichShift(), '|', '$'+ earnedTips.getTipsEarned(), 'has been added to the tipjar!')

		elif mainMenuChoice == 2:
			viewTips(tipjar)
			 
		elif mainMenuChoice == 3:
			print('\nThis selection is not available in beta; please choose a different selection!')

		elif mainMenuChoice == 4:
			print('\nThe program will now exit! Goodbye!')
			writeToFile(tipjar)
			break 

		else: 
			print('You have made an incorrect selection!')

# This function will add tips
def addTips(): 

	# Get type of employee
	print('\n1. Hourly')
	print('2. Salaried\n')
	choice = input('Select type of employee: ')

	# Valdating user input... I tried putting this in my program but when I do, there is an error that occurs after user inputs 'what shift did you work?'
	'''choice = validation.validateNumeric(choice)
	choice = validation.validateRange(choice, 1, 2)'''

	# Get employee information
	print('Employee Information')
	print('--------------------')

	firstName = input('First Name: ')
	lastName = input('Last Name: ')
	whichShift = input('What shift did you work? (lunch/dinner): ')
	
	if choice == '1':
		tipsEarned = input('Enter tips earned throughout shift: ')

		# Create Hourly Employee object
		hourlyEmployee = Employee.Hourly(firstName, lastName, whichShift, tipsEarned)
		

		# Return employee
		return hourlyEmployee
	elif choice == '2':
		print('Not yet implemented!')


# This function views the tips the user inputs
def viewTips(jar):

	# Display employee tip jar header	
	print('\nTotal Tips Earned')
	print('--------------------')

	# Iterate through tipjar list to see all the tips 
	for tips in jar:
		print(tips) 

# This function makes it so the program will run and not get stuck 
def createEmployee(e):
	print('Employee method ran!')
	return e

# This functions receives the list and writes to a file
def writeToFile(jarOfTips):

	# Open the Employee.txt file and write information to text file 
	with open('Employee.txt', 'a') as outfile:
		for employee in jarOfTips:
			if isinstance(employee, Employee.Hourly):
				outfile.write(employee.getFirstName() + ' ' + employee.getLastName() + ' ' + employee.getwhichShift() + ' ' + employee.getTipsEarned() + '\n') 

main()

