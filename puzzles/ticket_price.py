def ticket_price(age):
    if age <= 12:
        return "$5"
    elif age <= 17:
        return "$8"
    else:
        return "$12"
    
def get_price(age):
    return ("Your ticket price is ") + age

age = int(input("How old are you? "))
print(get_price(ticket_price(age)))