import random
secret_num = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Guess the secret number between 1 and 100: "))
    attempts += 1
    if guess < secret_num:
        print("Too low! Try again.")
    elif guess > secret_num:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the secret number {secret_num} in {attempts} attempts.")
        break