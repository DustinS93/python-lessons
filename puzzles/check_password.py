# Concept: return inside a for loop - exits the function immediately when a condition is met
def check_password():
    valid_passwords = ['python', 'code', 'secret']
    user_input = input("Enter password: ")
    for item in valid_passwords:
        if item == user_input:
            return "Access Granted"
        return "Access Denied"

print(check_password())