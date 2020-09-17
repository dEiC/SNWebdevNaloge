secret_number = 45

guess = None

x = 0

print (guess)

while x < 10:
    guess = int(input("Guess the secret number: "))
    x = x + 1

    if guess == secret_number:
        print("Congratulations! You guessed secret number in " + str(x) + " guesses!")
        break
    elif guess != secret_number:
        print("Oh sorry, that is not correct number, try again!")
else: 
    print("You are out of guesses, Sorry!")