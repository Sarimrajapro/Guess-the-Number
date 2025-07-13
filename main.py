import random
n = random.randint(1, 100)
a = -1
guesses = 0
while a != n:
    a = int(input("Guess the number (between 1 and 100): "))
    guesses += 1
    if a < n:
        print("Too low!")
    elif a > n:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number {n} in {guesses} tries.🙏")