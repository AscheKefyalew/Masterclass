name = input("What is your name: ")
age = int(input("Enter you age {}: ".format(name)))

print()
print("Your age is", age)

print()
if age < 18:
    print(name + "," " you are not eligible to vote.","Please come back in {} years.".format(18 - age))
elif age >= 200:
    print("sorry {}, you die in return of the Jedi.".format(name))
else:
    print(name + "," " you are eligible to vote")

print()