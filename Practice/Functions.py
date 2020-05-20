# function taking input string and returning it in reverse
your_sentence = input("What do you want to say?: ").strip()


def rev(sentence):
    return sentence[::-1]


print(rev(your_sentence))




