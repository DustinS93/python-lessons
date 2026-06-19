# Concept: grouping and accumulating
expenses = [
    {"desc": "pizza", "category": "food", "amount": 11.50},
    {"desc": "taxi", "category": "transport", "amount": 8.00},
    {"desc": "coffee", "category": "food", "amount": 3.75},
    {"desc": "subway", "category": "transport", "amount": 2.50},
    {"desc": "groceries", "category": "food", "amount": 22.00}
]

totals = {"food": 0, "transport": 0}

for e in expenses:
    totals[e["category"]] = totals[e["category"]] + e["amount"]

for t in totals.keys():
    print(f"{t.capitalize()}: ${totals[t]:.2f}")
    
