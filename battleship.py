'''A game of battleships created with help of numpy.'''

import numpy as np

# class Node:
#     def __init__(self, ship):
#         self.ship = ship

#     shot = False

class Grid:
    def __init__(self, bot):
        '''bot -> true for AI player
        
        The board is a 2d arr, where 0s indicate water, 1s ships, 2s misses and 3s hits.'''
        self.bot = bot
        self.board = np.zeros((10, 10))
    
    def add_ship(self, size, start_index, end_index):
        if (end_index[0] - start_index[0]) != size and (end_index[1] - start_index[1]) != size:
            return False

        if end_index[0] != start_index[0] and end_index[1] != start_index[1]:
            return False

        if start_index[0] > 10 or end_index[0] > 11 - size:
            return False
        
        if start_index[1] > 10 or end_index[1] > 11 - size:
            return False

        if np.any(self.board[start_index[0]:end_index[0] + 2, start_index[1]:end_index[1] + 2] == 1):
            return False
        
        if np.any(self.board[start_index[0] - 1:end_index[0] + 2, start_index[1] - 1:end_index[1] + 2] == 1):
            return False
        
        # if np.any(self.board[start_index[0] - 1:end_index[0] - 1, start_index[1] - 1:end_index[1] - 1] == 1):
        #     return False

        # if np.any(self.board[start_index[0] - 1:end_index[0] + 1, start_index[1] - 1:end_index[1] + 1] == 1):
        #     return False
      
        self.board[start_index[0]:end_index[0] + 1, start_index[1]:end_index[1] + 1] = 1


p1 = Grid(False)
print(p1.add_ship(2, (6, 3), (8, 3)))
print(p1.add_ship(2, (9, 1), (9, 3)))
print(p1.board)