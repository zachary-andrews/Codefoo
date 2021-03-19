import random
import numpy as np

class Lights:
    def toggle(self,light):
        if light == "on":
            return "off"
        else:
            return "on"   
            
    def setup_board(self, number_of_lights):
        return ["off"] * number_of_lights

    def turn_on_bulb(self,n,board):
        for index in range(len(board)):
            if (index+1) % (n+1)  == 0:
                board[index] = self.toggle(board[index])
        return board

    def count_lights(self, board):
        return board.count("on")

    def solve_lights(self, number_of_lights):
        board = self.setup_board(number_of_lights)
        for n in range(number_of_lights):
            print board
            board = self.turn_on_bulb(n,board)
            
        print board
        return self.count_lights(board)
        