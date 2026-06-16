# Concept: Error handling - to except an error from user input and ask them to try again
grocery_list = ["apples", "banana", "cherry"]

def numbered_list(grocery_list):
    number = 1
    for i in grocery_list:
        print(str(number) + ". " + i)
        number = number + 1

numbered_list(grocery_list)

try:
    choice = int(input("Pick a number: "))
    choice = choice - 1
    if choice not in range(len(grocery_list)):
        print("Not a valid number")
    else:
        print(grocery_list[choice])
except ValueError:
    print("not a number")


