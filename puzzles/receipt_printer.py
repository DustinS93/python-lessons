# Concept: f-strings - formatting variables and floats inside strings
def format_lines(desc, amount):
    return f"{desc} - ${amount:.2f}"

expense = [{"desc": "coffee", "amount": 4.99}, {"desc": "bus", "amount": 2.5}, {"desc": "sandwich", "amount": 8.99}]
for e in expense:
    print(format_lines(e["desc"], e["amount"]))
