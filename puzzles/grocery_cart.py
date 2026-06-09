# Concept: list methods - append, remove, pop, in - building a cart manager
def add_item(cart, item):
    cart.append(item)
    print("Added item: ",  item)
    return cart

def remove_last(cart):
    removed = cart.pop()
    print("Removed: " + removed)
    return cart

def remove_item(cart, item):
    if item in cart:
        cart.remove(item)
        print("Removed: ", item)
        return cart
    else:
        print("item not in cart")

def find_item(cart, item):
    for i in cart:
        if i == item:
            return "Found " + item
    return item + " not found"

            


cart = ['eggs', 'milk', 'bread', 'ham']
new_item = input("Add item: ")
remove = input("Remove: ")
find = input("Search cart ")
print(add_item(cart, new_item))
print(remove_last(cart))
print(remove_item(cart, remove))
print(find_item(cart, find))