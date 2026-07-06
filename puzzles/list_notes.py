# Concept: a script that prints every .md filename in a folder
import sys
import os
folder = sys.argv[1]
names = os.listdir(folder)
for name in names:
    if name.endswith(".md"):
        print(name)