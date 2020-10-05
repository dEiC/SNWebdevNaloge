import json
import os

class Player():
    def __init__(self):
        super().__init__()
        self.first_name = input("Name: "),
        self.last_name = input("Surname: "),
        self.height_cm = int(input("Height: ")),
        self.weight_kg = int(input("Weight: "))

    def save (self):
        players_file = os.path.abspath("players.txt")
        if os.path.exists(players_file):
            file = open("players.txt", "a")
            file.write(json.dumps(self.__dict__))
            file.close()
        else:
            file = open("players.txt", "x")
            file.write(json.dumps(self.__dict__))
            file.close()


class BasketballPlayer(Player):
    def __init__(self, ):
        super().__init__()
        self.points = int(input("Points: ")),
        self.rebounds = int(input("Rebounds: ")),
        self.assists = int(input("Assits: "))

class FootballPlayer(Player):
    def __init__(self, ):
        super().__init__()
        self.goals = int(input("Goals: ")),
        self.yellow_cards = int(input("Yellow cards: ")),
        self.red_cards = int(input("Red cards: "))


dejan = BasketballPlayer()
greenwood = FootballPlayer()
dejan.save()
greenwood.save()