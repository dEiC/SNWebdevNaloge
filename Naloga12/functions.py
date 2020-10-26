import json
import datetime
import random
import os, sys

class Results():
    def __init__(self, score, player_name, date, score_file):
        self.score = score
        self.player_name = player_name
        self.date = date

    @classmethod
    def get_score_list(cls, self):
        with open("score_list.txt", "r") as score_file:
            score_list = json.loads(score_file.read())
        return score_list

    @classmethod
    def save (cls):


        score_file = os.path.abspath("score_list.txt")
        if os.path.exists(score_file):
            file = open("score_list.txt", "a")
            print(file.__dict__)
            file.write(json.dumps(score_file))
            file.close()
        else:
            file = open("score_list.txt", "x")
            file.write(json.dumps(score_file))
            file.close()
    @classmethod
    def sort_list(cls, score_list):
        return sorted(score_list, key = lambda i: i['score'])

def play_game():
    secret = random.randint(1, 30)
    guess = None
    score = 0
    score_list = []

    while guess != secret:
        score_list = Results.get_score_list()
        guess = int(input("Guess the secret number (between 1 and 30): "))
        score += 1

        if guess == secret:
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(score))
            player_name = input("Please enter your name: ")
            score_list = Results.save(score_list)
            """
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
"""
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


