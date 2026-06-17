# Concept: error handling - pick a number within a range


try:
    user_input = int(input("Pick a number: ")) 
    if user_input > 0 and user_input <= 10:
        print("You picked " + str(user_input))
    else:
        print("Out of range")
except ValueError:
    print("Needs to be a number between 1-10")