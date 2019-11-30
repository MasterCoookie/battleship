if np.any(self.board[start_index[0]:end_index[0] + 2,
                            start_index[1]:end_index[1] + 2] == 1):
            return False

        if np.any(self.board[start_index[0]:end_index[0] + 2,
                            start_index[1] - 1:end_index[1] + 2] == 1):
            return False

        if np.any(self.board[start_index[0] - 1:end_index[0] + 2,
                            start_index[1] - 1:end_index[1] + 2] == 1):
            return False

        if np.any(self.board[start_index[0] - 1:end_index[0] + 2,
                            start_index[1] - 1:end_index[1] + 2] == 1):
            return False