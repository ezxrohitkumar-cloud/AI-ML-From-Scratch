secret=7
while True:
    guess=int(input("Guess the secret number between 1 and 10: "))
    if guess==secret:
        print("Congratulations! You guessed the secret number.")
        break
    elif guess<secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.") 

        