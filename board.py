import json


class Board:
    snakelist = {}
    ladderlist = {}
    playerslist = {}
    boxlist = {}
    start = 1
    end = 100

    @classmethod
    def snake_and_ladder_and_players_list(cls):
        with open('snakelist.json', 'r') as openfile:
            # Reading from json file
            Board.snakelist = json.load(openfile)

        with open('ladderlist.json', 'r') as openfile:
            # Reading from json file
            Board.ladderlist = json.load(openfile)

        with open('playerslist.json', 'r') as openfile:
            Board.playerslist = json.load(openfile)

        with open('boxlist.json', 'r') as openfile:
            Board.boxlist = json.load(openfile)

    @classmethod
    def position_on_board(cls, player_number, number):
        if number + Board.playerslist[str(player_number)][3] == Board.end:
            print("Wow!! you reached the end, your current score is number ", Board.playerslist[str(player_number)][3])
            return True
        elif number + Board.playerslist[str(player_number)][3] > Board.end:
            return False
        else:
            number = number + Board.playerslist[str(player_number)][3]
            if Board.boxlist[str(number)][2] != 0:
                Board.playerslist[str(player_number)][3] = Board.boxlist[str(number)][2]
                print("oops snake bite you, you went down to ", Board.boxlist[str(number)][2])

            elif Board.boxlist[str(number)][4] != 0:
                Board.playerslist[str(player_number)][3] = Board.boxlist[str(number)][4]
                print("Hurray!! you got the ladder, you went up to the number ", Board.boxlist[str(number)][4])

            else:
                Board.playerslist[str(player_number)][3] = number
                print(" you got neither snake nor ladder, so your current position is ",
                      Board.playerslist[str(player_number)][3])


        return False
