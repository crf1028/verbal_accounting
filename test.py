# from array import array
# from sys import getsizeof
#
# a = ('B', ['A', ])
#
# print a, type(a), getsizeof(a)
#
# b = 'Asset'
#
# print b, type(b), getsizeof(b)

# a = {'b':'c', 'e': 'none'}
# a['e'] = 'k'
#
# print a

# class A:
#     def __init__(self):
#         self.a = 'a'
#
# class B:
#     pass
#
# b=A()
#
# c = B()
#
#
# print type(b), isinstance(b, A), isinstance(c, A)
# a = round(float('897'), 2)
# print a, type(a)
# a = 'gk'
# a = a.split(',')
# print a[0], type(a), a
#
# a = {'b': 4}
#
# a['c']

# a = [1 , 2]
#
# a.extend([1])
#
# print a

# print sorted([1,8,3,4])

# if 1 in [0] or [1]:
#     print 'aa'

# if not ['a'] or not []:
#     print 'a'

# a = 'b'
#
# exec(a + "= 'c'")
#
#
# print a.value()

# a = []
# b =12
# a.extend([b])
# b=23
# a.extend([b])
# print a, b

# a = [1,2,3]
# b = [2,3,4]
# print a.join(b)

# a = [1,2,3]
# a[0:0] = 5
# print a
# a=5
# b=a
# b-=6
# print a,b
# for i in range(-1, -3, -1):
#     print i

# a = 'str'
# b = a
# a[1].pop()
# from collections import deque
# a = deque([])
# a.extend(['a'])
# print type(a)
# a = {}
# a.update({'a': ['c']})
# a.update({'a': ['d','e']})
# print a
# input_in = "receive investment, by cash, 10000"
# print input_in.split(',')[0], input_in.split(',')[1],input_in.split(',')[2][1:].isdigit()
# from math import *
# print pow(10, 2)
#
# import math
# print math.pow(10,2)

# a = {'a': 1, "b": 2}
# for i in a:
#     print i
# a='abc'
# print a.split(',')[0]

# class Book:
#     def __init__(self, name, page):
#         self.name = name
#         self.page = page
#
#     def __radd__(self, other):
#         return self.page + other
#
#     def __rsub__(self, other):
#         return self.page - other
#
#
#
# lst = [Book('crf', 500), Book('zyj', 200), Book('1qq', 700)]
#
# print lst[0] + lst[1], lst[0]-lst[1] - lst[2], sum(lst), reduce(lambda x,y: x-y, lst)

# a = "purchased equipment, paid in cash, 12000"
# tem_lst = a.split(',')
# tem_lst[1][0:0] = ''
# print tem_lst
# a = {'a': 1}
# print a['a']
# def a():
#     return ValueError
#
# try:
#     a()
# except:
#     print 'aa'
#
# a={'a':1,'b':2,'c':3}
#
# for key, value in a.items():
#     print key,value
a=[1,2,3,4,5,6]
b=[6,5,4,3,2,1]
for i,j in zip(a,b):
    print i,j