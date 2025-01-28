# # # import time
# from datetime import datetime, timedelta
# # current_time = datetime.now()
# # print(current_time)
# # unique_id =current_time.strftime("%S%f")
# # print(unique_id)

# current_time = datetime.now()
# current_hours = current_time.strftime("%H")
# current_minutes = current_time.strftime("%M")
# current = current_hours * 60 + current_minutes
# print(current_time)
# print()
# print(current_hours)
# print()
# print(current_minutes)


def isPrime(num):
    if num == '1':
        return False
    elif num == "2":
        return True
    else:
        for number in range(2,num+1):
            if num % number == 0:
                return False
        else:
            return True

string = input("Enter string here:")
out = []
for char in string:
    if type(char) != str:
        digit = int(char)
        if isPrime(digit) == True:
            out.append('*')
        else:
            out.append(digit)
    else:
        
print(out)