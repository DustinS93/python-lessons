# Concepet: Scripting a word count
import sys
with open(sys.argv[1]) as f:
    text = f.read()
length = len(text.split())
print(length)
