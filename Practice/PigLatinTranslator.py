# get sentence from user
your_sentence = input("What do you want to translate?; ").strip().lower()

# split the sentence into words
words = your_sentence.split()

# loop through words and convert into pig latin
new_words = []

for word in words:
    # if starts with vowel, add "yay"
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    # if starts with consonants, move first consonants to end and add "ay"
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# combine the converted words
translated_sentence = " ".join(new_words)

# print the final statement
print(translated_sentence)



