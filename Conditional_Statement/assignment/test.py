'''
character=input("Enter any character:")
if character in 'aeiouAEIOU':
    vowel_list=[character]
else:
    if 'a' <= character <= 'z' or 'A' <= character <= 'Z':
        print(ord(character))

number_of_days = int(input("Enter number  of day:"))
if number_of_days <= 5:
    charge = 5
    total_charge = number_of_days * 5
    print(total_charge)
elif 5 < number_of_days <= 10:
    charge = 4
    total_charge = number_of_days * 4
    print(total_charge)
elif 10 < number_of_days <=15:
    charge = 3
    total_charge = number_of_days * 3
    print(total_charge)
else:
    charge = 2
    total_charge = number_of_days * 2
    print(total_charge)
    

side1 = int(input("Enter side1:"))
side2 = int(input("Enter side2:"))
side3 = int(input("Enter side3:"))
if side1==side2:
    if side1==side3:
        print("Equilateral Traingle")
    else:
        print("isosceles traingle")
else:
    if side2==side3:
        print("isoceles traingle")
    else:
        print("scalene traingle")
        '''
num = int(input("Enter a number:"))
print(len(str(num)))