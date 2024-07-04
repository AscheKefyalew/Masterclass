import random
def guess_the_number():
    secret_number = random.randint(1, 10)
    print("can you guess the number?")
    guess = int(input("Enter your guess: "))
    match guess:
        case _ if guess == secret_number:
            print("congratulations asche you guessed correct")
        case _ if guess > secret_number:
            print("opps you guessed higher")
        case _ if guess < secret_number:
            print("opps you guessed lower")
    play_again = input("Do you want play again? (yes/no)")
    if play_again == "yes":
        guess_the_number()
    else:
        print("thank you for playing")
guess_the_number()