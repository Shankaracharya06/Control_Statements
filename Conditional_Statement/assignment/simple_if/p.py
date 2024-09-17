option=input("Choose any one option from below:\n A:Pizza\n B:Burger\n C:Vadapav\n D:Golgappa\n")
match option:
    case 'A':
        print("You have successfully ordered Pizza")
    case 'B':
        print("You have successfully ordered Burger")
    case 'C':
        print("You have successfully ordered Vadapav")
    case 'D':
        print("You have successfully ordered Golgappa")
    case _:
        print("Invalid Option")