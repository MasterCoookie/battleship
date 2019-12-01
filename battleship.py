'''A game of battleships created with help of numpy.'''

import time
import random
import numpy as np

class Grid:
    '''Players board.'''
    def __init__(self, bot):
        '''bot -> true for AI player
        
        The board is a 2d arr, where 0s indicate water, 1s ships, 2s misses and 3s hits.'''
        self.bot = bot
        self.board = np.zeros((10, 10))
    
    def add_ship(self, size, start_index, end_index):
        '''Adds a ship (1s) in given location.
        Returns True if added correctly or False if there was an error.'''
        size -= 1
        #TEMP
        # self.board[start_index[0]:end_index[0] + 2,
        #                      start_index[1]:end_index[1] + 2] = 5

        # self.board[start_index[0] - 1:end_index[0] + 2,
        #                      start_index[1] - 1:end_index[1] + 2] = 5


        if (end_index[0] - start_index[0]) != size and (end_index[1] - start_index[1]) != size:
            return False

        if end_index[0] != start_index[0] and end_index[1] != start_index[1]:
            return False

        if start_index[0] > 10 or end_index[0] > 10:
            return False

        if start_index[1] > 10 or end_index[1] > 10:
            return False

        if np.any(self.board[start_index[0]:end_index[0] + 2,
                            start_index[1]:end_index[1] + 2] == 1):
            return False

        if np.any(self.board[start_index[0]:end_index[0] + 2,
                            start_index[1] - 1:end_index[1] + 2] == 1):
            return False

        if np.any(self.board[start_index[0] - 1:end_index[0] + 2,
                            start_index[1]:end_index[1] - 1] == 1):
            return False

        if np.any(self.board[start_index[0] - 1:end_index[0],
                            start_index[1]:end_index[1] + 2] == 1):
            return False

        if np.any(self.board[start_index[0] - 1:end_index[0] + 2,
                            start_index[1] - 1:end_index[1] + 2] == 1):
            return False


        self.board[start_index[0]:end_index[0] + 1, start_index[1]:end_index[1] + 1] = 1

        return True

    def fire_at(self, spot):
        '''Shots at a given location (spot param) by incrementing its value by 2.
        Returns True if shot was a hit or False if it was a miss.'''
        if self.board[spot[0], spot[1]] < 2:
            self.board[spot[0], spot[1]] += 2

        if self.board[spot[0], spot[1]] == 3:
            return True
        return False


class Player:
    def __init__(self, board, nickname):
        '''The board aquired form Grid class instance.'''
        self.player_board = board
        self.nickname = nickname
        self.fleet = []
        self.shots_fired = []

    def add_ship_location(self, location):
        '''Saves ship location so ships state can be checked after its been hit.'''
        self.fleet.append(location)

    def get_ship_state(self, hit_location):
        '''Ship_type -> int representing ship type (see ship_names).
        Returns False if ship is still operational and True if it sank.'''
        for ship in self.fleet:
            if hit_location[0] in range(ship[0][0], ship[1][0] + 1):
                if hit_location[1] in range(ship[0][1], ship[1][1] + 1):
                    ship_location = ship
                    break

        ship_nodes = self.player_board.board[ship_location[0][0]:ship_location[1][0] + 1,
                                             ship_location[0][1]:ship_location[1][1] + 1]
        if np.all(ship_nodes == 3):
            return True
        return False

    @property
    def defeat(self):
        '''Returns True if player lost or False if hes still alive.'''
        if np.any(self.player_board.board == 1):
            return False
        return True


    def can_fire_at(self, spot):
        '''Returns True if given spot hasnt been fired at yet.'''
        if spot in self.shots_fired:
            return False
        return True

def convert_input(player_input):
    '''Converts board indexes from A9, C3 etc to tuples
    understandable by the code, aso check if it isnt faulty. Returns False if it is.'''
    if len(player_input) != 2 and player_input[1:] != '10':
        return False

    chars = 'abcdefghij'
    index = chars.find(player_input[0].lower())

    if index == -1:
        return False

    if 1 <= int(player_input[1]) <= 10:
        return (int(player_input[1:]) - 1, index)
    return False

    

# grid = Grid(False)
# p1 = Player(grid, 'MasterCookie')
# p1.player_board.add_ship(2, (2, 7), (2, 8))
# p1.player_board.add_ship(6, (3, 0), (3, 5))
# p1.add_ship_location(((3, 0), (3, 5)))
# print(p1.player_board.board)
# print(p1.get_ship_state((3, 4)))
# print(p1.player_board.add_ship(3, (6, 3), (8, 3)))
# p1.add_ship_location(((9, 0), (9, 1)))
# print(p1.player_board.board)
# print(p1.player_board.fire_at((9, 0)))
# p1.shots_fired.append((9, 0))
# print(p1.can_fire_at((9, 0)))
# print(p1.player_board.fire_at((9, 1)))
# print(p1.shots_fired)
# print(p1.defeat)
# print(convert_input(input()))

print('Hello! Welcome to JK.Battleship 0.1!\nPlease input your player name')
grid_p = Grid(False)
player = Player(grid_p, input())
SHIP_NAMES = ['Destroyer', 'Submarine', 'Cruiser', 'Battleship', 'Carrier']
print('Now, lets set up the board!')
# for idx in range(5):
#     while(True):
#         print(f'Place your {SHIP_NAMES[idx]} ({idx + 2} holes) on the board')
#         print('Input the starting and edning grid coordinate of your ship')
#         coordinate_1 = convert_input(input())
#         coordinate_2 = convert_input(input())
#         if coordinate_1 and coordinate_2 and player.player_board.add_ship(idx + 2, coordinate_1, coordinate_2):
#             break

print("All set! Lets play!")

grid_b = Grid(True)
bot = Player(grid_b, 'AI')

for idx in range(5):
    while(True):
        coordinate_1 = [random.randint(0, 9), random.randint(0, 9)]
        coordinate_2 = coordinate_1.copy()
        axis = random.randint(0, 1)
        if (coordinate_2[axis - 1] < 10 - (idx + 1)):
            coordinate_2[axis - 1] += idx + 1
            print(coordinate_1, coordinate_2)
            if bot.player_board.add_ship(idx + 2, coordinate_1, coordinate_2):
                bot.add_ship_location((coordinate_1, coordinate_2))
                break
        elif(coordinate_2[axis] < 10 - (idx + 1)):
            coordinate_2[axis] += idx + 1
            print(coordinate_1, coordinate_2)
            if bot.player_board.add_ship(idx + 2, coordinate_1, coordinate_2):
                bot.add_ship_location((coordinate_1, coordinate_2))
                break


print(bot.player_board.board)

while not (not player.defeat or bot.defeat):
    print("You go first! Good luck!")
    time.sleep(1)
    player_turn = True
    while player_turn:
        print("Input the coordinates of grid You want to shoot at")
        coordinates = convert_input(input())
        while not player.can_fire_at(coordinates):
            print("Something is wrong with your coordinates!")
            coordinates = convert_input(input())
        player_turn = bot.player_board.fire_at(coordinates)
        time.sleep(1)
        #if player turn is true it means the shot hit
        if player_turn:
            print("Thats a hit!")
            if bot.get_ship_state(coordinates):
                print("This ship sank!")
        else:
            print("Thats a miss!")

            

if bot.defeat:
    print("Congratulations! You win! GG")
else:
    print("You lose! Better luck next time! GG")
