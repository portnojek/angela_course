#if_else_statement

print("Wlcome to the rollercoaster: ")

height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You may get on!")
    age = int(input("How old are you?: "))
    if age < 12:
        print("5 dollars, please")
    elif age > 12 and age < 18:
        print("7 dollars, please")
    else:
        print("12 dollars, please ")
else:
    print("You can't to go!")
