import random

highest = 10
answer = random.randint(1, highest)
print(answer)  #TODO: Remove after testing

print("Please guess the number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:  
    guess = int(input())      

    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   #guess must be greater than answer
            print("Please guess lower")