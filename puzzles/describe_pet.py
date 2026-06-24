# Concept: print vs return, parameters, default parameters — fallback value when no argument is passed
def describe_pet(name, animal = "dog"): # CALLING MULITPLE ARGUMENTS, DEFAULT COMES SECOND
    return "My pet " + animal + " is named " + name # ACCOUNT FOR SPACES


print(describe_pet("Dustin"))
