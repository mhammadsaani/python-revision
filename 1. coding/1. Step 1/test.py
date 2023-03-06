# import collections

# _list = [x *x
#          for x in range(10)
#          if x % 2 == 0]

# _set = {x *x
#          for x in range(10)
#          if x % 2 == 0}

# _dict = {x: x*x
#          for x in range(10)
#          if x % 2 == 0}

# temp = {}
# for x in range(10):
#     if x % 2 == 0:
#         temp[x] = x*x

# print(_list)
# print(_set)
# print(temp, _dict)


# tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
# result = sorted(tuples, key=lambda x: x[1])
# # [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]
# print(result)

# import string
# print(type(string.ascii_uppercase))

# import math
# print(11.8/2)
# print(int(11.8/2))

# a = [1,2,3]
# # a.insert(1, 'h')
# # print(a)
# # a.pop()
# # print(a)
# # print(dir(a))
# a.remove(2)
# for method in dir(a):
#     if 'copy' in method:
#         print(method, dir(a))


# a = 0
# if a == 1:
#     print('this')
# elif a == 10:
#     print("that")
# else:
#     assert False, ("This should not happen but happening")

temp_list = [1,
             2]
print(temp_list.append(3))
print(temp_list)
