# !/usr/bin/python3
# coding=utf-8

# different from List, Tuple is not allowed to update
tuple = ( 'Sun', 123, 'Tue', 456, 'Thu', 1.2 )
tinytuple = ( 'tiny', 'list' )

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple * 2)
print(tinytuple * 2)
print(tuple + tinytuple)
