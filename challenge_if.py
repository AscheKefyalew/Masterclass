name = input("What is your name? ")
age = int(input("How old are you? "))

if 18 < age < 31:
    print("Hi {}, welcome to the holiday".format(name))
else:
    print("Sorry {}, you are not allowed to enter".format(name))
