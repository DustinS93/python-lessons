# Concept: functions calling functions — passing a return value as an argument to another function
def bill_splitter(total, people):
    return total / people

def format_share(amount):
    return "Each person owes $ " + str(amount)


print(format_share(bill_splitter(100, 4)))
