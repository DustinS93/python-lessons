# Concept: Using a dict to store counts of letter in a word
word = "banana"
counts = {}
for letter in word:
    if letter in counts:
        counts[letter] = counts[letter] +1 

for k, v in counts.items():
    print(f"{k}: {v}")
    