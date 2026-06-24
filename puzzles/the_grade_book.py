# Concept: for loop with conditionals — checking each score against a range of grade boundaries
def grade_book(grade_list):
    for score in grade_list:
        if score < 60:
            print(str(score) + " - F")
        elif score < 70:
            print(str(score) + " - D")
        elif score < 80:
            print(str(score) + " - C") 
        elif score < 90:
            print(str(score) + " - B")
        else:
            print(str(score) + " - A")



grades = [66, 77, 88, 99, 97, 75, 89]
grade_book(grades)  