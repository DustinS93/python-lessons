# Concept: list of dicts - accessing and displaying structured data
def display_item(label, cost):
    return f"{label.capitalize()} - ${cost:.2f}"
    
menu_items = [{"name": "burger", "price": 8.99}, {"name": "fries", "price": 5.99}, {"name": "nuggets", "price": 6.99}, {"name": "shake", "price": 6.99}, {"name": "drink", "price": 3.99}]
print("--- Today's Menu ---")
for i in menu_items:
    print(display_item(i["name"], i["price"]))