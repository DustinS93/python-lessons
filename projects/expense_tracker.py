# Project two, Expense tracker Build V0.2
import os
def load_expenses():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as f:
            lines = f.readlines()
        loaded_expenses = []
        for line in lines:
            parts = line.strip().split(",")
            loaded_expenses.append({"description": parts[0], "category": parts[1], "amount": float(parts[2])})
        return loaded_expenses
    else:
        return []
def save_expenses(expenses):
    with open("expenses.txt", "w") as f:
        for e in expenses:
            f.write(e["description"] + "," + e["category"] + "," + str(e["amount"]) + "\n")
def print_list():
    number = 0
    for e in expenses:
        number = number + 1
        print(str(number) + ". " + e["description"] + " " + e["category"] + " " + str(e["amount"]))

result = load_expenses()
expenses = result

while True:
    print("--- Menu ---")
    print("[1] Add Expense [2] View All [3] View Totals [4] Delete [5] Quit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        description = input("What did you buy?: ")
        category = input("What kind of purchase was this?: ")
        try:
            amount = float(input("How much did you spend?: "))
        except ValueError:
            print("Not A MF Float!")
            print("Try Again:")
            continue
        expenses.append({"description": description, "category": category, "amount": amount})
        save_expenses(expenses)
    elif choice == 2:
        print_list()
    elif choice == 3:
        total = {}
        for e in expenses:
            if e["category"] not in total:
                total[e["category"]] = 0
            total[e["category"]] = total[e["category"]] + (e["amount"])
        for t in total.keys():
            print(f"{t.capitalize()}: ${total[t]:.2f}")
    elif choice == 4:
        print_list()
        n = input("Which item do you want to remove? ")
        expenses.pop(int(n) - 1)
        save_expenses(expenses)
    elif choice == 5:
        print("Goodbye")
        break
save_expenses(expenses)

