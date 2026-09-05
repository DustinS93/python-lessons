# Concept: capstone - a function that builds and returns a letter-frequency dict
word_to_pass = "escapade"
word_to_pass2 = "thingamajigger"

def letter_tally(word):
    tally = {}
    for letter in word:
        if letter in tally:
            tally[letter] = tally[letter] + 1
        else:
            tally[letter] = 1
    return tally



def print_report(word):
    result = letter_tally(word)
    print("--Word Report--")
    print(f"Word: {word}")
    print(f"Length: {len(word)}")
    print(f"First Letter: {word[0]}")
    print(f"Last Letter: {word[-1]}")
    print(f"Uppercase: {word.upper()}")
    print(f"Reversed: {word[::-1]}")
    print("Letter Counts:")
    for k, v in result.items():
        print(f"{k}: {v}")
    

print_report(word_to_pass2)

print_report(word_to_pass)
