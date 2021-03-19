class boardUtils:
    def __init__(self,board):
        self.board = board

    def check_flip(self,index: int):
        if self.board[index] == '1':
            return True
        else:
            return False

    def flop(self,index: int):
        if self.board[index] == '1':
            self.board[index] = '0'
        elif self.board[index] == '0':
            self.board[index] = '1'

    def flip(self,index: int):
        if self.check_flip(index):
            self.board[index] = '.'
            if index-1 >= 0:
                self.flop(index-1)
            if index+1 < len(self.board):
                self.flop(index+1)

    def print(self):
        print(self.board)

    def check_win(self):
            return False if '0' in self.board else True

    def move_available(self):
        return True if '1' in self.board else False

    def check_left(self, index: int) -> int:
        if index-1 >= 0:
            return self.board[index-1]
        else:
            return 2

    def check_right(self, index: int) -> int:
        if index+1 < len(self.board):
            return self.board[index+1]
        else:
            return 2

    def make_move(self) -> int:
        for count,card in enumerate(self.board):
            if self.check_flip(count):
                if self.check_left(count) == '0' and self.check_right(count) == '0':
                    #free flip
                    self.flip(count)
                elif self.check_left(count) == '.' and self.check_right(count) == '.':
                    #anotherfree flip
                    self.flip(count)
                elif self.check_left(count) == '2' and self.check_right(count) == '.':
                    #starting numby flip
                    self.flip(count)
                elif self.check_left(count) == '.' and self.check_right(count) == '2':
                    #ending numby flip
                    self.flip(count)
                elif self.check_right(count) == '0' or self.check_right(count) == '.':
                    #flip from left to right
                    self.flip(count)
                else:
                    #yolo flip
                    self.flip(count)
                return count

                # check edges
