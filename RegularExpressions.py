import re

print('\n\t\t\t--Part 1--')
print('\t\t\t==========\n')

pattern= r"cheese"

if re.match(pattern, 'cheese chicken burger'):
     print("Matched") # OUTPUT
else:
     print('Not matched')

if re.match(pattern, 'no cheese chicken burger'):
     print("Matched")
else:
     print('Not matched') # OUTPUT
     
print('\n\t\t\t--Part 2--')
print('\t\t\t==========\n')

pattern= r"cheese"

if re.search(pattern, 'cheese chicken burger'):
     print("Matched") # OUTPUT
else:
     print('Not matched')

if re.search(pattern, 'no cheese chicken burger'):
     print("Matched") # OUTPUT
else:
     print('Not matched')
     
if re.findall(pattern, 'cheese chicken burger with extra cheese'):
     print("Matched") # OUTPUT
else:
     print('Not matched')

print(re.findall(pattern, 'cheese chicken burger with extra cheese'))

print('\n\t\t\t--Part 3--')
print('\t\t\t==========\n')

string_= 'Hi, I am Irfan'
print(string_) # Output: Hi, I am Irfan
pattern= r'Irfan'
newstring= re.sub(pattern, 'Ian', string_)
print(newstring) # Output: Hi, I am Ian

print('\n\t\t\t--Part 4--')
print('\t\t\t==========\n')

pattern= r"h.ld"

if re.match(pattern, 'held'):
     print('Matched') # OUTPUT
else:
     print("Not matched")

print('\n\t\t\t--Part 5--')
print('\t\t\t==========\n')

pattern= r"^go.d$"

if re.match(pattern, 'gold'):
     print('Matched') # OUTPUT
else:
     print('Not matched')
     
if re.match(pattern, 'mold'):
     print('Matched')
else:
     print('Not matched') # OUTPUT
     
if re.match(pattern, 'gols'):
     print('Matched')
else:
     print('Not matched') # OUTPUT

print('\n\t\t\t--Part 6--')
print('\t\t\t==========\n')

pattern= r"[A-Z][A-Z][0-9]"

if re.match(pattern, 'AB8'):
     print('Matched') # OUTPUT
else:
     print('Not matched')
     
if re.match(pattern, '1B8'):
     print('Matched')
else:
     print('Not matched') # OUTPUT
     
print('\n\t\t\t--Part 7--')
print('\t\t\t==========\n')

pattern= r"cheese(burger)*"

if re.match(pattern, 'cheese'):
     print('Matched') # OUTPUT
else:
     print('Not matched')
     
if re.match(pattern, 'cheeseburger'):
     print('Matched') # OUTPUT
else:
     print('Not matched')
     
if re.match(pattern, 'cheesesandwich'):
     print('Matched') # OUTPUT
else:
     print('Not matched')
     
if re.match(pattern, 'burger'):
     print('Matched')
else:
     print('Not matched') # OUTPUT


