data = [
    {
        'first': 1,
        'second': 2,
        'third': 3,
    },
    {
        'car': 'red',
        'horn': 'sound',
        'nested': {'level': 2},
    },

    {'program': None}
]

print(data)

print("Pretty Print")

from pprint import pprint

pprint(data)

print('Depth 1')
pprint(data, depth= 1)

print('Depth 2')
pprint(data, depth= 2)

print('Depth 3')
pprint(data, depth= 3)

print('Width')
pprint(data, width=10)

print('........COMPREHENSIONS......')
print('\n')

iterable = 1 ,2 ,3, 4

list_comprehension = [2*num for num in iterable]
print("List Comprehension: ", list_comprehension)

set_comprehension = {2*num for num in iterable}
print("Set Comprehension: ", set_comprehension)

generator_comprehension = (2*num for num in iterable)
print("Generators: ")
print(next(generator_comprehension))
print(next(generator_comprehension))
print(next(generator_comprehension))

dict_comprehension = { num: 2*num for num in iterable}
print("Dictionary Comprehension: ", dict_comprehension)

print("Comprehension with predication \n")
with_map_filter = list(map(lambda num: 5*num,
                           filter(lambda num: num%2==0, iterable)))
print("With Map and Filter: ", with_map_filter)

simplified_comprehension = [5*num for num in iterable if num%2==0]
print("Simplified Comprehension: ", simplified_comprehension)

print("\n Nested Comprehension \n")
letters = 'A', 'B', 'C'
numbers = '1', '2', '3'

combines_lists = []
for number in numbers:
    combines_lists = []
    for letter in letters:
        combines_lists.append(letter+number)
    combines_lists.append(combines_lists)

print("Normal way of combining lists: ", combines_lists)

sim_combined_lists = [[letter+number for letter in letters] for number in numbers]
print("Simplified Combined Lists: ", sim_combined_lists)


