import re

def PasswordCheck(Length, UpperC, LowerC, SpecialC, Name, Email, NumC, Uppercase, Lowercase, Numcase):
     valid = False
     while(valid == False):
        valid = True
        password = input("Please enter your password: ")
        counterS = 0
        counterU = 0 
        counterL = 0
        counterN = 0
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
             
        if valid == True:
            print("Password is valid!" )
            return True
        else:
            print("Password is invalid, please try again. ")
             
         

Length = int(input("How long should the password be? "))
UpperC = int(input("How many uppercase characters are required? "))
LowerC = int(input("How many lowercase characters are required? "))
SpecialC = int(input("How many special characters are required? "))
Name = input("Is the users name allowed? ")
Email = input("Is email allowed? ")
NumC = int(input("How many numeric characers are required? "))


print("Enter 1 to create your own password")
print("Enter 2 to generate your password")

choice = input()

SpecialList = ["!", "@", "#", "$", "%", "^", "&", "*"]


LowerCase = r"[a-z]"
Uppercase = r"[A-Z]"
NumCase = r"[1-9]"
if(choice == '1'):
    PasswordCheck(Length, UpperC, LowerC, SpecialC, Name, Email, NumC, LowerCase,Uppercase, NumCase)
    ##if(x = re.findall(SpecialList, password)):
     #   print("okay")
elif(choice == '2'):
    ##generate password
   print("okay") 