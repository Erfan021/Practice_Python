from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,5,4,4,4,6,7,7,8]
print(Counter(li))

sentence = 'This is the random sentence'
print(Counter(sentence))

dictionary = defaultdict(lambda: 'doesnot exist', {'a':1, 'b':2})
print(dictionary['a'])
print(dictionary['d'])

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)


import datetime

print(datetime.time(12,14,2))

print(datetime.date.today())

from array import array

arr = array('i', [1,2,3,4,5])
print(arr[2])