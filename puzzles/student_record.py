# Concept: dictionary basics - creating, accessing, and updating key-value pairs
def student_record():
    grade = 72
    passed = ''
    if grade > 60:
        passed = True
    else:
        passed = False
    record = {'name': 'Dustin', 'grade': grade, 'passed': passed}
    return record
print(student_record())