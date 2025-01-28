inp = "Today is my interview"
new_ = inp.replace("my","your")
# print(new_)

new_ = inp.replace(" ",",")
# print(new_)

tuple1 = (1,2,3)
# it's not possible to add element in tuple bcz of immutability


tuple1 = (1,2,3,5)
tuple2 = (2,4,5,6)
# output = []
# for item1 in tuple1:
#     for item2 in tuple2:
#         if item1 == item2:
#             output.append(item1)
# # print(tuple(output))

# string = "abcdefa"
# output = set()
# for item in string:
#     output.add(item)
# # print(str(output))
# out = ""
# for item in output:
#     out += item
# print(out)

# num = int(input("Enter num:"))
# fib = [1,2]
# if num == 1:
#     print(fib[0])
# elif num == 2:
#     print(fib)
# else:
#     for _ in range(2,num):
#         fib.append(fib[-1] + fib[-2])
#     print(fib)

# string = "abcdefa"
# reversed = string[::-1]
# print(reversed)

# input_= {'a':1,'b':1,'c':2,'d':2,'e':3}

# output__ = {1:['a','b'],2:['c','d'],3:['e']}
# out = {}
# for key in input_:
#     value = input_[key]
#     if value not in out:
#         out[value] = [key]
#     else:
#         out[value].append(key)
# print(out)