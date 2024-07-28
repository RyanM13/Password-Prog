import re
import string
import random

Play = True
while(Play == True):
	def PasswordCheck(Length, UpperC, LowerC, SpecialC, FName, LName, Email, NumC, Dict_File):
		#setting to False and than to true to keep the loop running when something is wrong.
		valid = False
		while(not valid):
			valid = True
			password = input("Please enter your password: ")

	#Initalizing counters 
			counterS = 0
			counterU = 0 
			counterL = 0
			counterN = 0

	#Loops that go through the string looking for errors
			for element in password:
				if element in SpecialList:
					counterS += 1 
			
			for element in password:
				if element.isupper():
					counterU += 1

			for element in password:
				if element.islower(): 
					counterL += 1

			for element in password:
				if element.isnumeric():
					counterN += 1

	#If statements checking the strings for the errors and setting to false to restart loop
			if len(password) < Length:
				print("Password not long enough. ")
				valid = False


			if counterS <  SpecialC:
				print("Not enough special characters. ")
				valid = False


			if counterU < UpperC:
				print("Not enough uppercase characters. ")  
				valid = False


			if counterL < LowerC:
				print("Not enough lowercase characters. ")
				valid = False


			if counterN < NumC:
				print("Not enough numbers. ")
				valid = False 

	#If password contains a word over 5 characters in dictionary it is invalid.
			for word in Dict_File:
				word = word.strip()
				if (len(word) > 5):
					if word in password.lower():
						print("can't have dictionary word. ")
						valid = False
					
				
			#need to fix to where all caps doesn't work either
			if FName.lower() in password.lower():
				("First name cannot be used in password. ")
				valid = False 
				print("Can't have users name. ")    

			if LName.lower() in password.lower():
				("Last name cannot be used in password. ")
				valid == False

			if password.find(Email) != -1:
				print("Email cannot be used in password") 
				valid = False 

	#validating 
			if valid:
				print("Password is valid!" )
				return True
			else:
				print("Password is invalid, please try again. ")
				

	def PasswordGenerator(Length, UpperC, LowerC, SpecialC, NumC):
	#variable to ask how many passwords the user wants generated
		Passwords_Needed = int(input("How many passwords would you like to generate: "))
	
		while(Passwords_Needed > 0):

   #Generates an amount of lowercase characters
			Lowercase_Letters = ''.join([random.choice(string.ascii_lowercase) 
											for char in range(UpperC)])
	#Generates an amount of uppercase characters
			Uppercase_letters = ''.join([random.choice(string.ascii_uppercase)
											for char in range(LowerC)]) 
	#Generates an amount of Numerical characters
			Numerical = ''.join([random.choice(string.digits)
									for numbers in range(NumC)]) 
	#Generates an amount of Special characters			
			Special_char = ''.join([random.choice(SpecialList)
								for char in range(SpecialC)])

    #Generates the remaining characters needed for length
			Length_char = ''.join([random.choice(string.ascii_letters)
									for char in range(Length - (LowerC + UpperC + NumC + SpecialC) )])
			
	#Concatenating the strings together
			Newpassword = Lowercase_Letters + Uppercase_letters + Numerical + str(Special_char) + Length_char

	#Turning the new string into a list for a list function
			Newpassword_List = list(Newpassword)

	#The list function shuffle moves the strings to different postions 
			random.shuffle(Newpassword_List)
			
	#Joining the list back to a string
			Final_Password = ''.join(Newpassword_List)
				
			print(str(Final_Password))
			
	#counter to know how many times to go through the loop
			Passwords_Needed -= 1

   

	#Set of characters acceptable to be special characters 
	SpecialList = ["!", "@", "#", "$", "%", "^", "&", "*"]

	#Opening the dictionary file to check prefixes
	Dict_File = open("Dictionary.txt", "r")


	#User input area to get all variables
	print("------------------------------------------------")
	Length = int(input("How many characters are required? ")) 
	UpperC = int(input("How many uppercase characters are required? "))
	LowerC = int(input("How many lowercase characters are required? "))
	SpecialC = int(input("How many special characters are required? "))
	NumC = int(input("How many numeric characters are required? "))


	#If no than any dictionary word above 5 characters is not allowed. 
	print('')
	Dict = input("Are dictionary words allowed? (Y,N): ")
	if Dict != 'N' and Dict != 'n':
		Dict_File = " "

	#Getting name input if needed
	Name_Input= input("Is the users name allowed? (Y,N): ")
	if Name_Input == 'N' or Name_Input == 'n': 
		FName = input("Please enter your first name: ")
		LName = input("Please enter your last name: ")
	else:
	#setting to an illegal character to pass to the function
		FName = " "
		LName = " "


	#Getting email input if needed
	Email_Input = input("Is email allowed? (Y,N): ")
	if Email_Input == 'N' or Email_Input == 'n':
		Email = input("Please enter your email: ")
	else:
	#setting to illegal character to void function variable
		Email = " "
		

	#Choice between creating your own or generating a password
	print('')
	choice = input("Enter 1 to create your own password\nEnter 2 to generate your password\n")
	print("------------------------------------------------")



	#Calling PasswordCheck if 1 
	#calling generate password if 2
	if(choice == '1'):
		PasswordCheck(Length, UpperC, LowerC, SpecialC, FName, LName, Email, NumC, Dict_File)
	elif(choice == '2'):
		##generate password
		PasswordGenerator(Length, UpperC, LowerC, SpecialC, NumC)

	Continue = input("Do you want to run the program again? Y/N ")
	if Continue == 'Y' or Continue == 'y':
		Play = True
		print("")
	else:
		Play = False