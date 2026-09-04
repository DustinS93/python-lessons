# Concept: Using a function with a loop to reverse a word
word = "excaliber"
word2 = "backstabber"
word3 = "cat"
word4 = "this will end up backwards as well..."

def reverse_word(reverse):
    length = len(reverse)
    rev_word = ""
    for l in reverse:
        length = length - 1
        rev_word = rev_word + reverse[length]
    return rev_word


print(reverse_word(word4))
print(reverse_word(word3))
print(reverse_word(word2))
print(reverse_word(word))
print(reverse_word(reverse_word(word2)))
