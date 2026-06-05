def to_fahrenheit(celcius):
    return (celcius * 9/5) + 32
def format_temp(temp):
    return "The temperature is " + str(temp) + " F"

print(format_temp(to_fahrenheit(37)))
