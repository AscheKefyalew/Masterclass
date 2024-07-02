import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    print("I've chosen a number between 1 and 10. Can you guess it?")

    guess = int(input("Enter your guess: "))
        
    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("Thanks for playing!")

# Start the game
guess_the_number()
