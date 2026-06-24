# Concept: conditionals — if/elif/else, passing a return value as an argument to another function
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
    

def format_grade(score, grade):
    return "Your score of " + str(score) + " is a " + grade

print(format_grade(56, get_grade(56)))