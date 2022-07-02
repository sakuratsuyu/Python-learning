# !/usr/bin/env bash
# coding=utf-8

# Data type is not allowed to change

# the following statement will create a new object
var = 1

# `del` to delete the object
del var

# int   long    float   complex
z1 = 1 + 2j
z2 = 5 - 3j
print(z1 / z2)

# Number type transform
# int(x) long(x) float(x) complex(real [, imag]) str(x) tuple(x) list(x) chr(x)
# repr(x) to transform an int to expression string
# unichr(x) to transform an int to a unicode char
# ord(x) to transform a char to an int
# hex(x), oct(x) to transform an int to a hex / oct string

x = 10
a = 'a'
print(repr(x))
print(ord(a))
print(hex(x))
print(oct(x))

# math & cmath module

# >>> import math
# >>> dir(math)

