# Shopping list app BuildV0.1
shopping_list = []
while True:
    print("[1] Add Item [2] View List [3] Quit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        shopping_list.append(input("Add an Item: "))
    elif choice == 2:
        number = 0
        for i in shopping_list:
            number = number + 1
            print(str(number) + ". " + i)
    elif choice == 3:
        print("Goodbye")
        break
    else: 
        print("Invalid Input")
       