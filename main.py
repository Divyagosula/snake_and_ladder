from player import Player
from board import Board
import random


class Real:
    @staticmethod
    def welcome():
        print("Welcome to the game!!")
        number_of_players = int(input("How many players are going to play : "))
        return number_of_players

    def players_information(self, number_of_players):
        number_of_players = number_of_players
        for i in range(number_of_players):
            print("Details of the player", i + 1)
            name = input("enter the name of player : ")
            sex = input("enter the sex of player : ")
            cone_color = input("enter the selected color of cone : ")
            obj = Player(name, sex, cone_color)
            obj.list_of_players(obj, i + 1)

    @staticmethod
    def start():
        print("Let's start the game!!!")
        win = True
        player_number = 1
        while win:
            print("Player", player_number, " roll the dice")
            number = random.randint(1, 6)
            print("the number is ", number)
            current_value = Board.position_on_board(player_number, number)
            if current_value:
                print("Congrats you win the gram")
                win = False

            else:
                if number == 6:
                    continue
                else:
                    if player_number == number_of_players:
                        player_number = 1
                    else:
                        player_number = player_number + 1


game = Real()
board = Board()
number_of_players = game.welcome()
game.players_information(number_of_players)
Player.playerslist_jsonfile()
Board.snake_and_ladder_and_players_list()
game.start()

