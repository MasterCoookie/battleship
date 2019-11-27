'''A game of battleships created with help of numpy.'''

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
        if (end_index[0] - start_index[0]) != size and (end_index[1] - start_index[1]) != size:
            return False

        if end_index[0] != start_index[0] and end_index[1] != start_index[1]:
            return False

        if start_index[0] > 10 or end_index[0] > 11 - size:
            return False

        if start_index[1] > 10 or end_index[1] > 11 - size:
            return False

        if np.any(self.board[start_index[0]:end_index[0] + 2,
                             start_index[1]:end_index[1] + 2] == 1):
            return False

        if np.any(self.board[start_index[0] - 1:end_index[0] + 2,
                             start_index[1] - 1:end_index[1] + 2] == 1):
            return False

        # if np.any(self.board[start_index[0] - 1:end_index[0] - 1, start_index[1] - 1:end_index[1] - 1] == 1):
        #     return False

        # if np.any(self.board[start_index[0] - 1:end_index[0] + 1, start_index[1] - 1:end_index[1] + 1] == 1):
        #     return False

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

    def add_ship_location(self, location):
        '''Saves ship location so ships state can be checked after its been hit.'''
        self.fleet.append(location)

    def get_ship_state(self, ship_type):
        '''Ship_type -> int representing ship type (see ship names).
        Returns False if ship is still operational and True if it sank.'''
        ship_location = self.fleet[ship_type]
        ship_nodes = self.player_board.board[ship_location[0][0]:ship_location[1][0] + 1,
                                             ship_location[0][1]:ship_location[1][1] + 1]
        if np.all(ship_nodes == 3):
            return False
        return True

    @property
    def defeat(self):
        '''Returns True if player lost or False if hes still alive.'''
        if np.any(self.player_board.board == 1):
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
        return (index, int(player_input[1:]) - 1)
    return False

    

# grid = Grid(False)
# p1 = Player(grid, 'MasterCookie')
# print(p1.player_board.add_ship(2, (9, 0), (9, 1)))
# print(p1.player_board.add_ship(3, (6, 3), (8, 3)))
# p1.add_ship_location(((9, 0), (9, 1)))
# print(p1.player_board.board)
# print(p1.player_board.fire_at((7, 4)))
# print(p1.player_board.fire_at((9, 0)))
# print(p1.player_board.fire_at((9, 1)))
# print(p1.player_board.board)
# print(p1.defeat)
print(convert_input(input()))
