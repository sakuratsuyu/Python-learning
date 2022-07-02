# !/usr/bin/python3
# coding=utf-8

# Python don't support a single char
str = "Hello World"

print(str)

print(str[0])

print(str[2:5])
print(str[2:])

# `+` for connect strings
print(str + "TEST")
print(str[:6] + 'runoob')

# `*` for repeat string
print(str * 2)

# `in` and `not in` can be used


# String format
# the same as C

# Triple quotation
str = '''
Hello
World!
!@#$%^&*(/
'''
print(str)


# Unicode string
# support format like \u0020
str = u"hello\u0020world"

print(str.capitalize())

# string module
