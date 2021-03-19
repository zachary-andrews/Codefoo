from boardUtils import boardUtils
class game:
    def solve(self,startingBoard):
        self.board = boardUtils(list(startingBoard))
        moves = []
        while self.board.move_available():
            moves.append(self.board.make_move())
        return " ".join(map(str, moves)) if self.board.check_win() else "no solution"
