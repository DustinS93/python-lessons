# Concept: modifying list items - list[i] = value
def mark_done(items, choice):
    if choice < 1 or choice > len(items):
        return "invalid input"
    choice = choice - 1
    items[choice] = "[x] " + items[choice]
    return items
def print_list(items):
    number = 1
    for i in items:
        print(str(number) + ". " + i)
        number = number + 1
    
    


groceries = ['eggs', 'milk', 'bread', 'butter']
print_list(groceries)
choice = int(input("Choose a number: "))
print(mark_done(groceries, choice))