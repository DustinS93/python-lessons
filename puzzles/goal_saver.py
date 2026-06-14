# Concept: reading and writing file
def save_goal(goal):
    with open('goal.txt', 'w') as f:
        f.write(goal)

def load_goal():
    with open('goal.txt', 'r') as f:
        contents = f.read()
    return contents.strip()
    


goal = input("Write a goal: ")
save_goal(goal)
file = load_goal()
print(file)