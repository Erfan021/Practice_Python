print("Even Numbers")
even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print(even_numbers)

print("Odd Numbers")
odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
print(odd_numbers)

print("Words")
words = ["the", "lazy", "dog", "is", "sleeping"]
answers = [[w.upper(), w.lower(), len(w)] for w in words]
print(answers)


