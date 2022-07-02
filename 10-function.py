# !/usr/bin/env bash
# coding=utf-8

def sum(a, b):
    return a + b

print(sum(2, 3))

# Mutable and immutable object
# String, Tuple and Number are immutable
# if `x = 5` and then `x = 10`, 
# then a new int object of 10 will generate and 5 is dismissed
# List and Dictionary are mutable

# Parameter pass of function
# Immutable type, like value pass in C
# Mutable type, like pointer pass in C

def ChangInt(a):
    a = 10
    return

b = 20
ChangInt(b)
print(b)

# Parameter
#   Essential
def prt(str):
    print(str)
    return

prt('123')

#   Keyword
def prtInfo(name, age):
    print('Name', name)
    print('Age', age)
    return

prtInfo(age = 18, name = "Miku")

#   Default
def prtInfo_(name, age = 18):
    print('Name', name)
    print('Age', age)
    return

prtInfo_( age = 9, name = "Miku")
# if `age` doesn't pass, it will use the default value
prtInfo_( name = "Miku")

#   Changeable length
def prt_( arg, *var_tuple ):
    print(arg)
    for var in var_tuple:
        print(var)
    return

prt_(1)
prt_(10, 20, 30)


# Anonymous function
# by lambda
# lambda is an expression, simpler than def
# lambda has its own naming space
sum = lambda arg1, arg2: arg1 + arg2
print(sum(1, 2))

# Global variant and local variant
total = 123
def sum_(a, b):
    total = a + b
    print(total)
    return total

sum_(1, 12)
print(total)
