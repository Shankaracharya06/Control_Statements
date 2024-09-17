'''
"WAP to validate the username and password entered by the user to login into an application"
credentials={"satya":"satya@679","divya":"divu@0806","shan":"shanky@612#","sachindra":"raisachindra@1970"}
username=input("Enter your username:")
password=input("Enter your password:")
if username in credentials:
    actual_password=credentials[username]
    if actual_password==password:
        print("Logged in successfully")
    else:
        print("Wrong Password")
else:
    print("username does not exist")

#WAP to check if the user entered char is vowel or not,only if the character is an alphabet
char=input("Enter any character:")
if char.isalpha():
    if char in "aeiouAEIOU":
        print("its a vowel")
    else:
        print("its consonent")
else:
    print("Not an alphabet")
    
#WAP to check if the user entered integer is a multiple of 5 only if it is an even number
integer=int(input("Enter an integer:"))
if integer % 2 == 0:
    if integer % 5 == 0:
        print(f"{integer} is an even number and also multiple of 5")
    else:
        print(f"{integer} is not multiple of 5")
else:
    print(f"{integer} is not an even number")
    '''