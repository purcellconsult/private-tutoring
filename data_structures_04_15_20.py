###########################
# 4 builtin data structures in python
#
# list -> mutable
# tuple -> immutable
# dictionary -> key/value mappings
# sets -> holds unique items
#############################


import random

# list
# -----
# mutable data structures: can be modified

x = [2, 4, 6, 8]
for item in x:
    print(item)


for item, value in enumerate(x):
    print(item, value)

i = 0
while i < len(x):
    print(x[i])
    i += 1

empty = []
for x in range(1, 11):
    empty.append(x)

nums = [x for x in range(1, 11)]

''' 
generates 10 random numbers
'''
for x in range(10):
    random.seed(a=1)
    print(random.randint(1, 100), end=' ')

x = [1, 2, 100, 20, 50, 70]
y = random.choice(x)
print(y)


print()
# tuple
# immutable data structure. can't be change in memory
# ------

x = (1, )  # is a tuple with a single element
y = (2, 4, 6, 8, 10)
y = (100, 200)
# y[0] = 100  can't reassign immutable objects
print(y)
print(y.count(100))  # 1


# dictionary

fruits = {'a': 'apple', 'o': 'orange', 'k': 'kiwi'}
print(fruits.items())  # returns all items in dictionary
print(fruits.keys())  # returns all keys in dictionary
print(fruits.values())  # returns all values in dictionary

print(fruits['a'])
print(fruits.get('o'))

# how to iterate over a dictionary

for key, value in fruits.items():
    print(key, value)

# python formats code using whitespace

phone_numbers = {

    'car insurance': '538-725-7261',
    'pizza company': '282-376-2176'
}


# set data structure
# ------------------
# sets can have unique items
# order is not maintained

x = {1, 1, 2, 1, 2, 2, 3, 5, 10}
print(x)

a = {1, 2, 3}
b = {10, 2, 300}
c = a.union(b)
print(c)

list_of_nums = [1, 2, 3, 4, 5, 9, 1, 2]
unique = list(set(list_of_nums))  # creates a list with unqiue elements
print(unique)

list_of_nums[3] = 100


