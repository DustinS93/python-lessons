# Shopping list app BuildV0.3 - add, view, mark done, persist to file
import os
shopping_list = []
if os.path.exists('shopping_list.txt'):
    with open('shopping_list.txt', 'r') as f:
        contents = f.readlines()
        for line in contents:
            shopping_list.append(line.strip())

while True:
    print("[1] Add Item [2] View List [3] Mark Done [4] Quit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        shopping_list.append(input("Add an Item: "))
    elif choice == 2:
        number = 0
        for i in shopping_list:
            number = number + 1
            print(str(number) + ". " + i)
    elif choice == 3:
        number = 0
        for i in shopping_list:
            number = number + 1
            print(str(number) + ". " + i)
        mark_item = int(input("Check Item: "))
        shopping_list[mark_item - 1] = "[x] " + shopping_list[mark_item - 1]
        number = 0
        for i in shopping_list:
            number = number + 1
            print(str(number) + ". " + i)
    elif choice == 4:
        with open('shopping_list.txt', 'w') as q:
            for item in shopping_list:
                q.write(item + '\n')
        print("Goodbye")
        break
    
        
    else: 
        print("Invalid Input")

