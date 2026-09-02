# Concept: Using if/elif/else chain to check grades

# First Version Function + Return
# def grade(score):
#    if score >= 90:
#        return "A"
#    elif score >= 80:
#        return "B"
#    elif score >= 70:
#        return "C"
#    elif score >= 60:
#        return "D"
#    else:
#        return "F"

# score = 90
# print("--Grading Complete--")
# print(f"Score: {score} you got a {grade(score)}")

score = 89

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("--Grading Complete--")
print(f"You Scored: {score} youre grade is {grade}")
