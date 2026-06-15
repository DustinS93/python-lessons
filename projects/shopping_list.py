# Shopping list app BuildV0.4 - dict refactor, add delete item
import os
shopping_list = []
if os.path.exists('shopping_list.txt'):
    with open('shopping_list.txt', 'r') as f:
        contents = f.readlines()
        for line in contents:
            parts = line.strip().split(",")
            shopping_list.append({"name": parts[0], "done": parts[1] == "True"})
while True:
    print("[1] Add Item [2] View List [3] Mark Done [4] Remove Item [5] Quit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        shopping_list.append({"name": input("Add an Item: "), "done": False})
    elif choice == 2:
        number = 0
        for i in shopping_list:
            number = number + 1
            if i["done"]:
                print(str(number) + ". [x] " + i["name"])
            else:
                print(str(number) + ". " + i["name"])
    elif choice == 3:
        number = 0
        for i in shopping_list:
            number = number + 1
            if i["done"]:
                print(str(number) + ". [x] " + i["name"])
            else:
                print(str(number) + ". " + i["name"])
        mark_item = int(input("Check Item: "))
        shopping_list[mark_item - 1]["done"] = True 
        number = 0
        for i in shopping_list:
            number = number + 1
            if i["done"]:
                print(str(number) + ". [x] " + i["name"])
            else:
                print(str(number) + ". " + i["name"])
    elif choice == 4:
        remove_item = int(input("Choose Item to Remove: "))
        shopping_list.pop(remove_item - 1)
    elif choice == 5:
        with open('shopping_list.txt', 'w') as q:
            for item in shopping_list:
                q.write(item["name"] + "," + str(item["done"]) + "\n")
        print("Goodbye")
        break
    else: 
        print("Invalid Input")