# While Loop

print("While Loop")
# number = 1
# while number <= 10:
#     if number % 2 == 0:
#         print(number) # printing even numbers only
#     number = number + 1
#
# nameList = []
#
# while len(nameList) < 4:
#     addName = input("Enter name: ").strip().capitalize()
#     nameList.append(addName)
#
# print("Sorry list is full now")
# print(nameList)

# For Loop

print("For Loop")
# vowels = 0
# consonants = 0
#
# for letters in "I am Irfan Ahmed":
#     if letters.lower() in "aeiou":
#         vowels = vowels + 1
#     elif letters == " ":
#         pass
#     else:
#         consonants = consonants + 1
#
# print("There are {} vowels".format(vowels))
# print("There are {} consonants".format(consonants))


students = {
    "male": ["Rehan", "Irfan", "Ali", "Josh", "Salman"],
    "female": ["Sarah", "Rekha", "Heer", "Zainab", "Jennet"]
}

for keys in students.keys():
    for names in students[keys]:
        if "a" in names:
            print(names)










