# !/usr/bin/python3
# coding=utf-8

list = [ 'Sun', 123, 'Tue', 456, 'Thu', 1.2 ]
tinylist = [ 'tiny', 'list' ]

# similar operation as string
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list * 2)
print(tinylist * 2)
print(list + tinylist)

list.append('Google')
print(list)
del list[6]
print(list)


