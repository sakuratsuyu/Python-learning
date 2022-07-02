# !/usr/bin/python3
# coding=utf-8

# key - value
# key is unique, but value not
# therefore a key can be Number, String or Tuple, but not List
dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'

tinydict = { 'name' : 'runoob', 'code' : 14514, 'dept': 'sal' }

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

# Modify
dict['one'] = 'This is 1'
print(dict)
del dict[2]
print(dict)
tinydict.clear
print(dict)
del dict
