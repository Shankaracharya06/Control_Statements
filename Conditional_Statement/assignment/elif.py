'''
#Write a program to check the relation between two integer numbers.
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
if num1 ==  num2:
    print("Both are equal")
elif num1 > num2:
    print(f"{num1} is greater")
elif num2 > num1:
    print(f"{num2} is greater")
elif num1 % num2 == 0:
    print(f"{num1} is divisble by {num2} and multiple of {num2}")
elif num2 % num1 == 0:
    print(f"{num2} is divisble by {num1} and multiple of {num1}")
else:
    print("No relation")

#Write a program to check whether a given character is uppercase or lowercase or number. If character is uppercase print uppercase, If character is lowercase print lowercase. If the character is a number, print the ascii number of it. 
character = input("Enter any character:")
if character.isupper():
    print("It is uppercase")
elif character.islower():
    print("It is lowercase")
elif character.isnumeric():
    print(f"it is numeric and ASCII value of {character} is {ord(character)}")

#Write a program to check whether a given character is a vowel or consonant. If a given character is a vowel, store the character inside the list. If a given character is consonant, display the ASCII value of that character.
character=input("Enter any character:")
if character in 'aeiouAEIOU':
    vowel_list=[character]
else:
    if 'a' <= character <= 'z' or 'A' <= character <= 'Z':
        print(f"ASCII value of {character} is {ord(character)}")
'''
#Write a program to check if the given data is individual data type or not. 
#write a program to check whether the given integer single digit or two digits or three digits or more than three digits
#write a program to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of both 3 and 5
#Write a program to predict grade of the student based on the obtained result 
#Write a program to check whether the entered character is uppercase or lowercase or number or special character
#Write a program to find the greatest among two numbers
#Write a program to find the smallest among three numbers 
#Write a program to find the greatest among four numbers
#Write a program to find the smallest among four numbers
#Write a program to calculate the electricity bill.According to the following criteria, for 1st 100 units there is no charge, For next 100 units there is ₹5 per unit and after 200 units, the price is rupees 10 per unit.If the input is 350 then total bill amount is Rupees 2000. 
#Write a program to accept percentages from the user and display the grade according to the following criteria. If marks is greater than 90, grade is A. If marks is greater than 80 and less than equals to 90, gra inde is B if marks is greater than or equal to 60, and less than equals to 80 grade is C, else if it is less than 60 grade is D
#Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria if cost price is greater than One Lac.The tax is 50%, if it is greater than 50,000 and less than equals to 1,00,000 the tax is 10% and if it is less than equals to 50,000 the tax is 5%.
#Write a program to accept a number from one to seven and display the name of the day. Like one for Sunday, 2 for Monday and so on.
#Write a program to accept a number from 1:00 to 12:00 and display name of the month and days in that month like one for January and number of days is 31 and so on.
#Accept any city from the user and display monuments of that city. For Delhi it is Red Fort, Agra- Taj Mahal, Jaipur- Jal Mahal.
#Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
#Accept the number of days from the user and calculate the charge of library according to the following criteria. Till five days it is ₹2 per day, 6 to 10 days it is ₹3 per day, 11 to 15 days it is ₹4.00 per day and after 15 days it is five Rupees per day.
#Accept the kilometers covered and calculate the bill according to the following criteria. For 1st 10 kilometers it is ₹11.00 per kilometer, For next 90 kilometers it is rupees 10 per kilometer and after that it is ₹9 per kilometer. 
#WAP to convert temperature from celsius to kelvin and kelvin to celsius using the elif statement.