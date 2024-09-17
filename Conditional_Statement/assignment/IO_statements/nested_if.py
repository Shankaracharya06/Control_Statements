#Write a program to create an Instagram login page.
login_username = {"shanky" : "shanky@612","satya" : "satya@72011" ,"divya" : "divya@82001" ,"susmna" : "cutipie1997@"}
login_email = {"shankyrai612@gmail.com" : "shanky@612","satyarai007@gmail.com" : "satya@72011" ,"divyanidhisingh0012@gmail.com" : "divya@82001" ,"susmnarai1997@gmail.com" : "cutipie1997@"}
login_phone_number = {"6394399793" : "shanky@612","8081943453" : "satya@72011" ,"8840338328" : "divya@82001" ,"8081962502" : "cutipie1997@"}
print("########## Instagram ###########")
username = input("Enter your username:")
password = input("Enter your password")
if username not in login_username:
    print("wrong username try with your email id")
    email = input("Enter your email:")
    if email not in login_email:
        print("wrong email id try with your number")
        phone_number = input("Enter your phone number:")
        if  phone_number not in login_phone_number:
            print("wrong phone number")
elif username in login_username:
    actual_password = username[lo]
    if actual_password == password:
        print("you have successfully logged in")
    else:
        print("wrong password")




#Program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater than 3
#Write a program.To check the greater among four numbers using nested if.
#Write a program to find the second greatest among four numbers.
#Write a program.To check the type of a given character.
#Write a program to consider an integer number. Print happy if the number is divisible by two. Print SAD if the number is divisible by 5 and print square of the numbers only if it is divisible by seven else print the number as it is.
#Write a program to find the smallest among three numbers.
#Program to consider an input string. Print the string as it is if it is palindrome. Print the reverse string if it has an even number of characters. Print all the characters present at an odd index if the string is having an odd number of characters.
#Write a program to print middle Character.Given string only if it is upper case character.
#Write a program to check whether a given character is vowel or consonant using nested if.
#Write a program to print the length of given data only if it is even.
#Write a program to check greatest among three numbers using nested if.
#Write a program.To check second greatest among three numbers using nested if.
#Write a program that determines the movie ticket price based on the age and day of the week
#Adults (18+): $12 (except for Tuesdays: $10)
#Children (under 18): $8 (except for Tuesdays: $6)
#Seniors (65+): $8 (always)
#Leap Year Checker: Write a program that determines if a given year is a leap year. A leap year is a year divisible by 4, but not by 100 unless it's also divisible by 400.
#Vending Machine: Create a program for a vending machine that takes product code (integer) and amount paid (float) as input. It should check the product price (stored in a dictionary) and dispense the product if enough is paid. Use nested ifs for different error messages (e.g., invalid code, insufficient funds).
#Restaurant Discount: Write a program that calculates a restaurant bill with a discount based on the day of the week and party size:
#Weekdays (Mon-Fri), party < 4: No discount.
#Weekdays (Mon-Fri), party >= 4: 10% discount.
#Weekends (Sat-Sun), any party size: 15% discount.
#Shape Identifier: Design a program that takes two inputs (length1, length2) and identifies the geometric shape based on the values:
#If lengths are equal: Square
#If one length is twice the other: Rectangle
#Otherwise: Not a square or rectangle
#WAP to check the type of a triangle (Equilateral,isosceles,scalene) using nested -if
#Wap to accept any number from 1 to 5 and display that number in word form. if they enter more than 5 then print no match.

#Wap to take input as only collections. 
#i) if the type of input is a list then  ask the value from the user and insert it in the middle index of that list. and print that list.
#	ii) if type of input is tuple print 'cannot append tuple is immutable'
#	iii)if type is set, take the input from the user. if the value is immutable then only add it to the set and print the set otherwise print 'enter only immutable collection'
#	iv) if type of input is dictionary take key and value as user input and add the key and value 	pair using syntax to add key value . and print the dictionary.
