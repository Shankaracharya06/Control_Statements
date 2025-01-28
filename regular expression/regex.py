import re

'''
? -> 0 or 1 occurence
'''
string = "colour color which colour do you choose"
pattern = "colou?r"
result = re.findall(pattern, string)
print(result)

'''
. -> any character (but one only)
'''
string = "grey may be gray but not gruy gray is combo of black and white"
pattern = "gr.y"
result = re.findall(pattern, string)
print(result)

'''
[characters] -> character set (matches one char only)
'''
string = "grey may be gray but not gruy gray is combo of black and white"
pattern = "gr[ea]y"
result = re.findall(pattern, string)
print(result)

string = "Smith once used to be a blacksmith Steve Smith"
pattern = "[Ss]mith"
result = re.findall(pattern, string)
print(result)


'''
+ -> one or more occurence
'''
string = 'he looked at hanna and yelled, "Hannnna!, what have you done hannnna?"'
pattern = "[Hh]ann+a"
result = re.findall(pattern, string)
print(result)

'''
\d -> digit char -> [0123456789] one digit only
'''
string = "99 people called 911 in last 20 days"
# pattern = "\d+"
pattern = "[0-9]+"
result = re.findall(pattern, string)
print(result)


'''
[a-zA-Z] -> char set -> one alphabet only
'''
string = "XAEA-12"
pattern = "[a-zA-Z]"
result = re.findall(pattern, string)
print(result)

'''
^ -> in char set represents negation, 
     meaning anything other than the chars mentioned in the char set.
     
'''
string = "humpty dumpty sat on a wall"
pattern = "[^aeiouAEIOU]"
result = re.findall(pattern, string)
print(result)

'''
^ -> outside char set represents startswith
$ -> represents ending with
'''
string = "mary had a little lamb his fleece was white as snow"
pattern = "^mary"
result = re.findall(pattern, string)
print(result)
pattern = "snow$"
result = re.findall(pattern, string)
print(result)


''''^ and $ if used on a same pattern, checks if the pattern is a single word in that string'''
string = "twinkle"
pattern = "^twinkle$"
result = re.findall(pattern, string)
print(result)


string = "python is king java is ... python is better than java"
pattern = "(python|java)"
result = re.findall(pattern, string)
print(result)

string = "Sh@zzy_is @maz!ng"
pattern = r"\b[a-zA-Z]+"
result = re.findall(pattern, string)
print(result)

string = "1 machli jal ki raani hai"
pattern = r"\b[a-zA-Z]+\b"
result = re.findall(pattern, string)
print(result)


string = "1 of 10 books cost rs. 100 each if 20000 people buy 125 books calculate total cost"
pattern = r"\b\d{2,5}\b"
result = re.findall(pattern, string)
print(result)