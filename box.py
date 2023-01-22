import json


class Box:
    box_list = {}

    def __init__(self, number, color, issnake=False, snake_endnumber=0, isladder=False, ladder_endnumber=0):
        self.number = number
        self.color = color
        self.issnake = issnake
        self.isladder = isladder
        self.snake_endnumber = snake_endnumber
        self.ladder_endnumber = ladder_endnumber

    def issnake_present(self, snakelist, number):
        if str(number) in snakelist.keys():
            self.issnake = True
            self.snake_endnumber = snakelist[str(number)]

    def isladder_present(self, ladderlist, number):
        if str(number) in ladderlist.keys():
            self.isladder = True
            self.ladder_endnumber = ladderlist[str(number)]

    def add_box_tothe_list(self):
        Box.box_list[self.number] = [self.color, self.issnake, self.snake_endnumber, self.isladder, self.ladder_endnumber]

    @staticmethod
    def boxlist_jsonfile():
        with open("boxlist.json", "w") as outfile:
            json.dump(Box.box_list, outfile)


Number_of_boxes = int(input("enter number of boxes are present: "))
with open('snakelist.json', 'r') as openfile:
    # Reading from json file
    snakelist: dict = json.load(openfile)

with open('ladderlist.json', 'r') as openfile:
    # Reading from json file
    ladderlist: dict = json.load(openfile)

for i in range(0, Number_of_boxes):
    number = i + 1
    color = 'white'
    box = Box(number, color)
    box.issnake_present(snakelist, number)
    box.isladder_present(ladderlist, number)
    box.add_box_tothe_list()

print(Box.box_list)
Box.boxlist_jsonfile()
