# Concept: function prints menu with a while loop that prints selection from user input until the input 'quit'
def menu_select():
    while True:
        print('[1] Say Hello [2] Say Goodbye [3] Quit')
        choose = int(input('Choose an option '))
        if choose == 1:
            print("Hello")
        elif choose == 2:
            print("Goodbye")
        elif choose == 3:
            break
        else:
            print("Invalid choice")
    print('Program closed')

(menu_select())