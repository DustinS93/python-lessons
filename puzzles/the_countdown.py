# Concept: for loop counter pattern — decrementing a variable inside a for loop
def countdown(metals):
    number = len(metals)
    for i in metals:
        print(str(number) + ". " + i)
        number = number - 1

metals = ['gold', 'silver', 'bronze', 'tin', 'copper', 'brass']
countdown(metals)