# Project two, Expense tracker Build V0.1
expenses = []
while True:
    print("--- Menu ---")
    print("[1] Add Expense [2] View All [3] View Totals [4] Quit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        expenses.append({"description": input("What did you buy?: "), "category": input("What kind of purchase was this?: "), "amount": float(input("How much did you spend?: "))})
    elif choice == 2:
        number = 0
        for e in expenses:
            number = number + 1
            print(str(number) + ". " + e["description"] + " " + e["category"] + " " + str(e["amount"]))
    elif choice == 3:
        total = {}
        for e in expenses:
            if e["category"] not in total:
                total[e["category"]] = 0
            total[e["category"]] = total[e["category"]] + (e["amount"])
        for t in total.keys():
            print(f"{t.capitalize()}: ${total[t]:.2f}")

    elif choice == 4:
        print("Goodbye")
        break