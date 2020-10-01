import json
import datetime
import random

def play_game():
    secret = random.randint(1, 30)
    guess = None
    attempts = 0
    score_list = get_score_list()

    while guess != secret:
        
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

    

def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
    return score_list

def sort_list(score_list):
    return sorted(score_list, key = lambda i: i['attempts'])

