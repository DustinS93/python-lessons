vault = "Crown jewels"

def lock():
    vault = "Can't access my key"
    return vault

def peek():
    return vault

print(lock())
print(peek())
print(vault)
