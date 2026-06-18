# Concept: float - storing decimal numbers for money
def calculate_tip(bill_amount, tip_amount):
    tip_amount = float(tip_amount) / 100 
    tip = tip_amount * bill_amount
    return tip
bill_amount = float(input("Enter bill total: "))
tip_amount = input("What percent do you wnat to tip?: ")
result = calculate_tip(bill_amount, tip_amount)
print(result)
total_bill = result + bill_amount
print(total_bill)