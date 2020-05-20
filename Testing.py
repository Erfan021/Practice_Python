matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)

# List unpacking
a, b, *other, d = [1,2,3,4,5,6,7,8,9]
print(str(a) +'\n'+ str(b) +'\n'+ str(other) +'\n'+ str(d))

# Binary
print(bin(568))
print(int('0b101', 2))

# Ternary Operator / Conditional Expressions
is_Friend = True
can_message = 'message allowed' if is_Friend else 'not allow to message'
print(can_message)

# Short Circuiting Concept
if True or False:
    print('Going to print it')
    
if False and True:
    print('No matter, it will print')
    
# Range
print(range(100))
for i in range(0,10):
    print(i)
    
for _ in range(5):
    print("okay")
    print(_)

for _ in range(0, 20, 3):
    print(_)
    
# Enumerate
list_ = ['a','b','c','d']
for i,char in enumerate(list_):
    print(i, char)
    
for i, char in enumerate(list(range(30))):
    print(i, char)
    if char == 15:
        print(f'The index of 15 is: {i}')
        
# *args and **kwargs
def sum_all(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
        
    return sum(args) + total


print(sum_all(1,2,3,4, mum=5, num2=10))

# global, # nonlocal

# Map
nlist = [1,2,3,4,5,6]
def multiby2(item):
    return item * 2

print(list(map(multiby2, nlist)))
print(nlist)

# Filter
nlist2 = [2,3,4,5,6,7,8]
def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, nlist2)))
print(nlist2)

# Zip
list1 = [1,2,3]
list2 = [4,5,6]
print(list(zip(list1, list2)))
print(list1)
print(list2)

# Reduce
from functools import reduce
listA = [2,4,6,8,10,12]
def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, listA, 0))
print(listA)

import operator
lists = [[1,2,3], [4,5,6], [7,8,9]]
print(reduce(operator.add, lists))

# Lambda Expressions
print(list(map(lambda x: x * 2, nlist)))
print(list(filter(lambda x: x % 2 != 0 , nlist2)))
print(reduce(lambda acc, item: acc + item, listA))

listB = [5,4,3]
print(listB, end='\n')
listNew = list(map(lambda num:num**2, listB))
print(listNew)

listC = [(0,2), (4,3), (9,9), (10,-1)]
print(listC, end='\n')
listC.sort(key=lambda x: x[1])
print(listC)














