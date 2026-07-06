# Concept: Scripting a word count - read file   
import sys
with open(sys.argv[1]) as f:
    text = f.read()
length = len(text.split())
print(length)
