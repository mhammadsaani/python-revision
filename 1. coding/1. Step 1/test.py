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

# class Solution:
#     def moveZeroes(self, nums) -> None:
#         for idx, value in enumerate(nums):
#             if value == 0:
#                 nums.pop(idx)
#                 nums.append(0)
#                 print(nums)

#         return nums


# sol = Solution()
# sol.moveZeroes([0,1,0])


# class Solution:
#     def factorialNumbers(self, N):
#         for i in range(1, N + 1):
#             value = self.find_factorial(i)
#             if value <= N:
#                 print(value, end=" ")
#             else:
#                 return

#     def find_factorial(self, num):
#         res = 1
#         for i in range(1, num + 1):
#             res *= i
#         return res


# sol = Solution()
# sol.factorialNumbers(25)


def long_function_with_x_args(
    aaaaaaaaaaaaaaa,
    bbbbbbbbbbbbbbbbbbbbbb,
    ccccccccccccccccccc,
    dddddddddddddddddd,
    eeeeeeeeeeeee,
):
    pass


# print(chr(92))
# print(66%57)