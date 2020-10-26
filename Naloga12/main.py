import datetime
import json
import random
import os, sys
import importlib
from functions import *


score_list = Results.get_score_list()

while True:
    selection = input("Would you like to A) Play a new game, B) See the best scores, C) quit?")

    if selection == "A":
        play_game()
    elif selection == "B":
        score_list = Results.get_score_list()
        score_list = Results.sort_list(score_list)
        print("Top scores are: ")
        for list_item in score_list[:3]:
            print("- Attempts: " + str(list_item["score"]) + " Date: " + list_item["date"])


    else:
        break

