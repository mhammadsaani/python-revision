# Data Types


"""
Fundamental Data Types

int 
float
bool
str
list
tuple
set
dict

"""


"""
Classes --> Custom Types (We can create our own types)
Like SuperCar
"""

""" 
Specialized Data Types
Modules 
"""

""" 
Complex (for numbers)
a = 2i + j 
a = complex(2, 3)
print(a)
"""


# None is also a type means nothing (Absence of value)


# need to import math
# math.ceil vs math.floor

# ceil makes the number bigger if 3.1 then 4  (not in case of 0)
# floor makes the number smaller if 3.1 then 3

# import math
# print(math.ceil(3.0))

# print(round(3.4))

# print(bin(5))

# print(int("101", 2))

# Operator Precedence

# a = 2 / 3 * 2
# print(a)

# max_range = 5
# for row in range(max_range):
#     for col in range(max_range - row):
#         print(col+1, end="")
#     print()

# max_range = 5
# for row in range(max_range):
#     for col in range(row):
#         print(" ", end="")

#     n = 2*max_range - ((2*row) + 1)
#     for col in range(n):
#         print("*", end="")

#     for col in range(row):
#         print(" ", end="")

# print("")

# [0, 9, 0]
# [1, 7, 1]
# [2, 5, 2]
# [3, 3, 3]
# [4, 1, 4]

# max_range = 5

# for row in range(max_range*2):
#     for col in range()

# a = 2 / 2 * 4
# print(a)

# def temp():
#     """
#     """

# print(temp())

# a = 'It\'s Sunny'
# a = f'I am Hammad {a}'
# print(a)

# tempList = [1, 2, 3]
# print(sum(tempList))

# a = 'it\ncomplicated'
# print(a)

# print(int(False))


# user_Name = input("Enter your User Name: ")
# password = input("Enter your Password: ")

# print(f'You user name is {user_Name} and it is {len(password)} long. {"*" * len(password)}')


# two_D = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]


# print(two_D[:1][:])

# tempList = ['1', '2', '3']

# # a=''.join(tempList)
# # print(a)

# print(tempList[:])

# a, b, c = 1, True, 3.4
# print(c)


# a, *c, e = [1,2,3,4]
# print(a)
# print(c)
# print(e)


# a = [[1, 2, 3], [1, 2, 3]]
# print(a)
# print("I am test")

# a =  [1, 2]

# print(a)


# arr = [range(5)]
# print(arr)

# result = "Greater" if 2>3 else "Lesser" if 3>5 else "Lesser2"
# print(result)

# print(ord('a'))
# print(ord('A'))
# print('A' > 'a')

# a = True
# b = 1
# print(id(a))
# print(id(b))
# print(a is b)
# print(a == b)

# users = {
#     'name': "Hammad",
#     'email': 'm.hammadsaani@gmail.com',
#     "password": '*****'
# }

# # for item in users:
# #     print(users.get(item))
# print(users.items())


# def my_function(a):
#     '''
#     This function takes a para a and prints it
#     '''
#     print(a)
    
# my_function(1)

# help(my_function)



# a = 'hellooooo12'
# print(a[0:10])

# if 5 > 3:
#     a = 5
    
# print(a)




# total = 0

# def temp():
#     global total
#     total = total
#     def addOne():
#         nonlocal total
#         total+=1
#         print(total)
#     addOne()
#     print(total)
    
# temp()
# print(total)




morse_code_chars = {
"A" : ".-",    
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : "·",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--.."
}





for character in morse_code_chars:
    value = morse_code_chars.get(character)
    value = value.replace("-", "9")
    morse_code_chars[character] = value
    
# print(morse_code_chars)


# morse_code_chars_dic = {'A': '.9', 'B': '9...', 'C': '9.9.', 'D': '9..', 'E': '·', 'F': '..9.', 'G': '99.', 'H': '....', 'I': '..', 'J': '.999', 'K': '9.9', 'L': '.9..', 'M': '99', 'N': '9.', 'O': '999', 'P': '.99.', 'Q': '99.9', 'R': '.9.', 'S': '...', 'T': '9', 'U': '..9', 'V': '...9', 'W': '.99', 'X': '9..9', 'Y': '9.99', 'Z': '99..'}
    
    
# def password_generator(website_name):
#     if len(website_name) < 5:
#         return "Give website with a name lenght more than 5"
#     website_name = website_name[0:5]
#     print(website_name)
#     password = morse_code_chars_dic.get(website_name[0].upper()) + "5" + website_name[1].lower() + morse_code_chars_dic.get(website_name[2].upper()) + "3" + website_name[3].lower() + morse_code_chars_dic.get(website_name[4].upper()) + "1JythoN"
#     print(password)
    
# password_generator("adslfv")


# .9..5i9.3k.1JythoN

# _list = [1, 2, 3, 4]
# i = 0
# while i != (n:=len(_list)):
#     print(n)
#     i+=1
    


# from collections import deque
	
# # Declaring deque
# queue = deque([["the","quick","brown","fox","jumps","over","the","lazy","dog"] ,"fox", "dog"])
# temp = queue.popleft()
# # a = [queue.popleft()(), queue.pop(), queue.pop()]
# # print(temp)

# print('fox' == "fox")



# def testArgs(*args, **kwargs):
#     print(kwargs)
#     print(args)
#     return sum(args)

# print(testArgs(1,2,3,4,5, test=1, test2=3))


# a = 1
# b = 1
# print(a == b)
# print(a is b)
# a = []
# b = []
# print(a == b)
# print(a is b)

# print(list(range(10)))

# print(False == 0)


# a = [1,2,3]
# print(a.pop())
# a = [[1,2,3], 
#      [4,5,6]]
# print(len(a))


def sumNumers(a, b):
    return a + b

def sumNumbers(a, b, c):
    return a + b + c

print(sumNumbers(2, 3))
print(sumNumbers(2, 3, 4))