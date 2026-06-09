# Concept: using a while loop, append a cart until "done" 

def run_cart():
    cart = []
    item = input("Type item to put in cart: ")
    while item != "done":
        cart.append(item)
        print(cart)
        item = input("Type item to add to cart: ")
    return cart



print(run_cart())


        
