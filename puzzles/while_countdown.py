# Concept: while loop - running a loop based on a condition instead of a fixed list
def count_down(number):
    while number > 0:
        print(number)
        number = number - 1
    print("Blast Off!")    

number = input("What do you want to count down from? ")
count_down(int(number))
