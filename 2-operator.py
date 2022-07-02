# !/usr/bin/python3
# coding=utf-8

# Arithmetic
a = 3 
b = 2
c = 0

c = a + b
print("a + b = ", c)
c = a - b;
print("a - b = ", c)
c = a * b
print("a * b = ", c)
c = a / b
print("a / b = ", c)
c = a // b
print("a // b = ", c)
c = a % b
print("a % b = ", c)
c = a ** b
print("a ** b = ", c)

# Compare
# == != > < >= <=

# Assign
# = += -= *= /= %= **= //=

# Logic
# and or not

# Bits
# & | ^ ~ << >>

# Member
# in
# not in
a = 10
b = 1
list = [ 1, 2, 3, 4, 5]
if (a in list) :
    print("a is in list")
else :
    print("a is not in list")
if (b in list) :
    print("b is in list")
else :
    print("b is not in list")

# Identity
# is
# is not
# whether the object referred is the same
# similarly id(x) == id(y) , id(x) != id(y)
a = 20
b = 20
if (a is b) :
    print("a and b has the same identifie")
b = 30
if (a is not b) :
    print("a and b don't have the same identifier")

# Priority
