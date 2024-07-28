import re
import os

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
                if word in password:
                    print("can't have dictionary word. ")
                    valid = False
                
            
        #need to fix to where all caps doesn't work either
        if password.find(FName) != -1:
            ("First name cannot be used in password. ")
            valid = False 
            print("Can't have users name. ")    

        if password.find(LName) != -1:
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
             

def PasswordGenerator():
    print("Placeholder")


#Set of characters acceptable to be special characters 
SpecialList = ["!", "@", "#", "$", "%", "^", "&", "*"]

#Opening the dictionary file to check prefixes
Dict_File = open("Dictionary.txt", "r")


#User input area to get all variables
Length = int(input("How many characters should the password be? ")) 
UpperC = int(input("How many uppercase characters are required? "))
LowerC = int(input("How many lowercase characters are required? "))
SpecialC = int(input("How many special characters are required? "))
NumC = int(input("How many numeric characters are required? "))


#If no than any dictionary word above 5 characters is not allowed. 
Dict = input("Are dictionary words allowed? (Y,N): ")
if Dict == 'Y' or Dict == 'y':
    Dict_File == " "

#Getting name input if needed
Name_Input= input("Is the users name allowed? (Y,N): ")
if Name_Input == 'N' or Name_Input == 'n': 
   FName = input("Please enter your first name:\n ") 
   LName = input("Please enter your last name: ")
else:
#setting to an illegal character to pass to the function
    Name = " "

#Getting email input if needed
Email_Input = input("Is email allowed? (Y,N): ")
if Email_Input == 'N' or Email_Input == 'n':
    Email = input("Please enter your email: ")
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
    PasswordCheck(Length, UpperC, LowerC, SpecialC, FName, LName, Email, NumC, Dict_File)
elif(choice == '2'):
    ##generate password
   print("okay") 