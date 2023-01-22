import json


class Snake:
    snake_list = {}

    def __init__(self, startposition, endposition, color):
        self.startposition = startposition
        self.endposition = endposition
        self.color = color

    def add_snake_to_the_list(self):
        self.snake_list[self.startposition] = self.endposition

    @classmethod
    def snakelist(cls):
        print(cls.snake_list)

    @staticmethod
    def snakelist_jsonfile():
        with open("snakelist.json", "w") as outfile:
            json.dump(Snake.snake_list, outfile)


Number_of_snakes = int(input("enter number of snakes are present: "))

for i in range(0, Number_of_snakes):
    print("Enter the snake details")
    startposition = int(input('enter the starting position: '))
    endposition = int(input('enter the end position: '))
    color = input('enter the snake color: ')
    obj = Snake(startposition, endposition, color)
    obj.add_snake_to_the_list()
    print("snake object is created and added to the list")

Snake.snakelist()
Snake.snakelist_jsonfile()

# with open('snakelist.json', 'r') as openfile:
#   # Reading from json file
#    json_object = json.load(openfile)

# print(json_object)
# print(type(json_object))
