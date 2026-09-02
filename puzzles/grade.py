# Concept: Using if/elif/else chain to check grades


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = 90
print("--Grading Complete--")
print(f"Score: {score} you got a {grade(score)}")
