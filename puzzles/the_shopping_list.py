def check_list(shopping_list):
    number = 0
    for i in shopping_list:
        number = number + 1
        print(str(number) + ". " + i)
        # number = number + 1
    
shopping_list = ['eggs', 'milk', 'bread']
print(check_list(shopping_list))
