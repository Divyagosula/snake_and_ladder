import random

current_position = 0
win = 100
snake_position = {14: 4, 28: 10, 47: 18, 43: 1, 51: 31, 63: 39, 68: 33, 77: 26, 83: 58, 90: 70, 93: 66, 95: 53, 99: 90}
ladder_positions = {2: 21, 8: 30, 16: 37, 27: 69, 41: 62, 45: 55, 65: 97, 73: 94}
print("welcome to the snake&ladder game")
print('Hello! lets start the game ')


def calculate_current_position(initialposition, dicevalue):
    currentposition = initialposition + dicevalue
    return currentposition


def calculate_game_over(currentposition):
    if currentposition == win:
        print("You won the game")
        quit()


def calculate_snake(currentposition):
    if currentposition in snake_position.keys():
        currentposition = snake_position[currentposition]
        print('snake got you down!! and you current position is ', currentposition)
    return currentposition


def calculate_ladder(currentposition):
    if currentposition in ladder_positions.keys():
        currentposition = ladder_positions[currentposition]
        print("Hurray you got the ladder!! and your current position is ", currentposition)
    return currentposition


while current_position < win:
    print(current_position)
    input()
    dice_value = random.randint(1, 6)
    print(dice_value)
    current_position = calculate_current_position(current_position, dice_value)
    calculate_game_over(current_position)
    current_position1 = calculate_snake(current_position)
    if current_position1 != current_position:
        current_position = current_position1
        continue
    current_position2 = calculate_ladder(current_position)
    if current_position2 != current_position:
        current_position = current_position2
        continue
