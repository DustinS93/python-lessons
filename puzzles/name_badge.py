# Concept: store return value of a function in a variable - result = function()
def get_name():
    name = input("Enter your name? ")
    return name
def make_badge(name):
    return "--- Badge: " + name + " ----"



name = get_name()

if len(name) < 1:
    print("Name Required!!!")
else:
    badge = make_badge(name)
    print(badge)

