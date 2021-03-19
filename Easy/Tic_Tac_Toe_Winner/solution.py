import numpy as np
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = np.array([["","",""],["","",""],["","",""]])
        X_move = True
        
        def addMove(move: List[int], player: str): 
            board[move[0]][move[1]] = player
        
        def check() -> str:
            for i in range(len(board)):
                if np.all(board[:,i] == board[:,i][0]) and board[:,i][0] != '':
                    return board[:,i][0]
                elif np.all(board[i,:] == board[i,:][0]) and board[i,:][0] != '':
                    return board[i,:][0]
            diag1 = board.diagonal()
            diag2 = np.fliplr(board).diagonal()
            if np.all(diag1 == diag1[0]) and diag1[0] != '':
                return diag1[0]
            if np.all(diag2 == diag2[0]) and diag2[0] != '':
                return diag2[0]
            
            if np.count_nonzero(board == '') > 0:
                return "Pending"
            return "Draw"

        for move in moves:
            if X_move:
                addMove(move,'X')
            else:
                addMove(move,'O')
            X_move = not X_move
        result = check()
        result = 'A' if result == 'X' else 'B' if result == 'O' else result
        return result