# !/usr/bin/python3
# coding=utf-8

# different from List, Tuple is not allowed to update
# including delete some elements ( but we can delete the all tuple)
tuple = ( 'Sun', 123, 'Tue', 456, 'Thu', 1.2, )
tinytuple = ( 'tiny', 'list', )

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple * 2)
print(tinytuple * 2)
print(tuple + tinytuple)

# tuple by default without any bracket
x, y = 1, 2
print(x, y)

print('a', 4e-3, 1 + 2j, 'djipa')
