# !/usr/bin/python3
# coding=utf-8

# Condition
num = 9
if num == 3:
    print('num is 3')
elif num == 2:
    print('num is 2')
else:
    print('roadman')

# Loop
# break & continue

# while
count = 0
while count < 9:
    print('The count is', count)
    count += 1

count = 0
while count < 5:
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is not less than 5")

# for
for letter in 'Python':
    print(letter)

fruits = [ 'banana', 'apple', 'mango']
for index in range(len(fruits)):
    print(fruits[index])

for num in range(1, 50):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print('%d is a prime' % num)

# the statement after `else` will be execute after the loop ends

# Example loop nesting
# Print the prime between 2 and 10
i = 2
while (i < 100):
    j = 2
    while j <= i / j:
        if not(i % j):
            break
        j += 1
    if j > i / j:
        print(i, 'is prime')
    i += 1

# pass
# `pass` don't do anything, just for occupation to make grammar right

