import json


class Player:
    players_list = {}

    def __init__(self, name, sex, cone_color, current_value=0):
        self.name = name
        self.sex = sex
        self.cone_color = cone_color
        self.current_value = current_value

    @staticmethod
    def list_of_players(obj, number):
        Player.players_list[number] = [obj.name, obj.sex, obj.cone_color, obj.current_value]

    @staticmethod
    def playerslist_jsonfile():
        with open("playerslist.json", "w") as outfile:
            json.dump(Player.players_list, outfile)
