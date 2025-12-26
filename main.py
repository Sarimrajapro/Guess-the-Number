import random

def guess_the_number_game():
    secret_number = random.randint(1, 50) #----------------- Generate a random number between 1 and 50
    guess_limit = 7
    guesses_taken = 0

    print("Welcome to the 'Guess the Number' game!")
    print(f"I'm thinking of a number between 1 and 100. You have {guess_limit} guesses.")

    while guesses_taken < guess_limit:
        try:
            guess = int(input("Take a guess: "))
            guesses_taken += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Congratulations! You guessed the number in {guesses_taken} guesses!")
                return     #-----------------------------------------------------------------End the game if guess is correct
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"Sorry, you ran out of guesses. The number I was thinking of was {secret_number}.")

guess_the_number_game()
