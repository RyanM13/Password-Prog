import re

def PasswordCheck():
     password = input("Please enter your password: ") 

     if len(password) < 10:
        print("Password too short.")
        PasswordCheck()
   

     elif not (re.search(CapitolCase, password)):
        print("Needs uppercase.") 
        PasswordCheck()
        

     elif not (re.search(LowerCase, password)):
        print("Needs lowercase")
        PasswordCheck()
      
     elif not (re.search(NumCase, password)):
        print("Needs numbers")
        PasswordCheck()
     return

print("Instructions:\n\nEnter a password with at least 2 special characters.")
print("Can not be your name or email")
print("Needs at least one capitol letter")
print("Finally it needs at least one number\n")

name = input("Please enter your name: ")
email = input("Please enter your email: ")

print("Enter 1 to create your own password")
print("Enter 2 to generate your password")

choice = input()

SpecialList = ["!", "@", "#", "$", "%", "^", "&", "*"]

SpecialCase = r"[!-*]"
LowerCase = r"[a-z]"
CapitolCase = r"[A-Z]"
NumCase = r"[1-9]"
if(choice == '1'):
    PasswordCheck()
    ##if(x = re.findall(SpecialList, password)):
     #   print("okay")
elif(choice == '2'):
    ##generate password
   print("okay") 


