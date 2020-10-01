import datetime
import json
import random
from functions import *

score_list = get_score_list()

while True:
    selection = input("Would you like to A) Play a new game, B) See the best scores, C) quit?")

    if selection == "A":
        play_game()
    elif selection == "B":
        for score_list in get_score_list():
            print(str(score_list["attempts"]) + " attemps, date: " + score_list.get("date"))
    else:
        score_list = sort_list(score_list)
        print("Top scores are: ")
        for list_item in score_list[:3]:
            print("- Attempts: " + str(list_item["attempts"]) + " Date: " + list_item["date"])