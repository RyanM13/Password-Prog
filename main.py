import re
import os

def PasswordCheck(Length, UpperC, LowerC, SpecialC, Name, Email, NumC):
    #setting to False and than to true to keep the loop running when something is wrong.
     valid = False
     while(valid == False):
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

        #need to fix to where all caps doesn't work either
        if password.find(Name) != -1:
            ("Name cannot be used in password. ")
            valid = False 
            print("Can't have users name. ")    


        if password.find(Email) != -1:
            print("Email cannot be used in password") 
            valid = False 

#validating 
        if valid == True:
            print("Password is valid!" )
            return True
        else:
            print("Password is invalid, please try again. ")
             

#Set of characters acceptable to be special characters 
SpecialList = ["!", "@", "#", "$", "%", "^", "&", "*"]
   
#User input area to get all variables
Length = int(input("How many characters should the password be? ")) 
UpperC = int(input("How many uppercase characters are required? "))
LowerC = int(input("How many lowercase characters are required? "))
SpecialC = int(input("How many special characters are required? "))
NumC = int(input("How many numeric characters are required? "))
Name_Input= input("Is the users name allowed? (Y, N): ")
if Name_Input == 'Y' or Name_Input == 'y': 
   Name = input("Please enter your name: ") 
else:
#setting to an illegal character to pass to the function
    Name = " "
Email_Input = input("Is email allowed? ")
if Email_Input == 'Y' or Email_Input == 'y':
    Email = input("Please enter your email: (Y, N)")
else:
#setting to illegal character to void function variable
    Email = " "
    

#Choice between creating your own or generating a password
print("Enter 1 to create your own password")
print("Enter 2 to generate your password")

choice = input()

#Calling PasswordCheck if 1 
#calling generate password if 2
if(choice == '1'):
    PasswordCheck(Length, UpperC, LowerC, SpecialC, Name, Email, NumC)
elif(choice == '2'):
    ##generate password
   print("okay") 