import random

highest = 10
answer = random.randint(1, highest)
print(answer)     #TODO: Remove after testing

print("Please guess the number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:   #guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")


                               #OR

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed it correctlty")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it 2")    # added two to identify the answer from the first if or we can use debug
#     else:
#         print("Sorry, you have not guessed it correctlty 2") 
# else:
#     print("You got it")

                              #OR

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:   #guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")




    