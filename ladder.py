import json

class Ladder:
    ladder_list = {}

    def __init__(self, startposition, endposition, color):
        self.startposition = startposition
        self.endposition = endposition
        self.color = color

    def add_ladder_to_the_list(self):
        self.ladder_list[self.startposition] = self.endposition

    @classmethod
    def ladderlist(cls):
        print(cls.ladder_list)

    @staticmethod
    def ladderlist_jsonfile():
        with open("ladderlist.json", "w") as outfile:
            json.dump(Ladder.ladder_list, outfile)


Number_of_ladders = int(input("enter number of boxes are present: "))

for i in range(0, Number_of_ladders):
    print("Enter the ladder details")
    startposition = int(input('enter the starting position: '))
    endposition = int(input('enter the end position: '))
    color = input('enter the ladder color: ')
    obj = Ladder(startposition, endposition, color)
    obj.add_ladder_to_the_list()
    print("ladder object is created and added to the list")

Ladder.ladderlist()
Ladder.ladderlist_jsonfile()
