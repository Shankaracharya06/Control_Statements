'''
#WAP to print sqaure of a number entered by user
num=int(input("Enter a number:"))
square=num**2
print(f"sqaure of the number is {square}")

#WAP to print the last element in the list entered by the user
user_list=eval(input("Enter the list:"))
last_element=user_list[-1]
print(f"The last element of the list is {last_element}")

#WAP to delete an element from the list entered by the user
user_list=eval(input("Enter a list:"))
del_element=user_list.pop()
print(f"The deleted element from the list is {del_element}")

#WAP to print the element present at the index position entered by the user
user_list=eval(input("Enter a collection:"))
index=int(input("Enter the index:"))
element=user_list[index]
print(f"The element present at index {index} is {element}")

#WAP to remove element present at index position entered by the user
user_list=eval(input("Enter a collection:"))
element=int(input("Enter the element which you want to delete from the collection:"))
user_list.remove(element)                                 #remove method will return none.It just remove the element from the list
print(f"Element deleted successfully")
print(f"The new list is:{user_list}")


#WAP to print reverse of a word entered by the user
word=input("Enter any word:")
revers=word[::-1]                                         #word[starting_index : ending_index : how much step u want to jump]
print(revers)


#WAP to perform basic mathematical operation on two numbers entered by the user and print the result using single print function
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
sum = num1 + num2
diff = num2 - num1
product = num1 * num2
div = num2 / num1
print(sum,diff,product,div, sep="\n")
'''