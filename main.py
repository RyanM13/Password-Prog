import re

def PasswordCheck(UpperC, LowerC, SpecialC, Name, Email, NumC):
     password = input("Please enter your password: ") 




UpperC = input("How many uppercase characters are required? ")
LowerC = input("How many lowercase characters are required? ")
SpecialC = input("How many special characters are required? ")
Name = input("Is the users name allowed? ")
Email = input("Is email allowed? ")
NumC = input("How many numeric characers are required? ")


print("Enter 1 to create your own password")
print("Enter 2 to generate your password")

choice = input()

SpecialList = ["!", "@", "#", "$", "%", "^", "&", "*"]

SpecialCase = r"[!-*]"
LowerCase = r"[a-z]"
CapitolCase = r"[A-Z]"
NumCase = r"[1-9]"
if(choice == '1'):
    PasswordCheck(UpperC, LowerC, SpecialC, Name, Email, NumC)
    ##if(x = re.findall(SpecialList, password)):
     #   print("okay")
elif(choice == '2'):
    ##generate password
   print("okay") 