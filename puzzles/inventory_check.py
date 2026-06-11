# Concept: Check inventory using for and while loop on a list with an input
def bag_check(bag):
    for items in bag:
        answer = ""
        while answer != "yes":
            print(f"Do you have this {items}")
            answer = input()
            if answer == 'quit':
                return 'bye'
    return "packed"
bag = ['ball', 'nuts', 'egg', 'fish']
print(bag_check(bag)) 