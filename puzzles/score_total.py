# Concept: accumulator pattern - summing a value across a list of dicts
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 74},
    {"name": "Priya", "score": 95},
]

total = 0

for scores in students:
    total = total + scores["score"]

print(f"Total score: {total}")
