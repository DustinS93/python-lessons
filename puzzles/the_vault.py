# Concept: scope — local vs global variables, same name in both scopes uses the local copy
vault = "Crown jewels"

def lock():
    vault = "Can't access my key"
    return vault

def peek():
    return vault

print(lock())
print(peek())
print(vault)
