from copy import deepcopy

board = [[2,1,0],[0,1,1],[1,0,1],[2,0,1]]
width = len(board)
length = len(board[0])

def check_board(static_board):
    for i in range(width):
        for j in range(length):
            if static_board[i][j] == 2:
                rot_oranges(board,i,j)

    
def rot_oranges(board,row,col):
    #check left
    if row-1 >= 0:
        if board[row-1][col] == 1:
            board[row-1][col] = 2
    #check right
    if row+1 < width:
        if board[row+1][col] == 1:
            board[row+1][col] = 2
    #check above
    if col-1 >= 0:
        if board[row][col-1] == 1:
            board[row][col-1] = 2
    
    #check below
    if col+1 < length: 
        if board[row][col+1] == 1:   
            board[row][col+1] = 2

def still_fresh(static_board):
    for i in range(width):
        for j in range(length):
            if static_board[i][j] == 1:
                return True
    return False

if __name__ == "__main__":
    minute = 0
    while(True):
        static_board = deepcopy(board)
        check_board(static_board)
        if static_board == board:
            if still_fresh(static_board):
                print "Couldnt get them all"
                minute = -1
                break
            else:
                print "All Oranges have been rotten"
                break
        minute += 1
        
        
        print board
    print minute