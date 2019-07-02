import random
import tkinter as tk
import numpy
import copy

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Conways Game of Life")
        
        
    def run(self,rows,cols,alive,color):
        self.cellwidth = 25
        self.cellheight = 25
        self.canvas = tk.Canvas(self, width=25*rows, height=25*cols, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.rect = {}
        self.rows = rows
        self.columns = cols
        self.alive = alive
        self.color = color
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="grey", tags="rect")
        map = numpy.zeros((self.rows,self.columns))
        self.start(map,alive)
        self.redraw(map,1000,color)

    def redraw(self,map,delay,color):
        map = self.play(map)
        size = numpy.size(map,1)
        self.canvas.itemconfig("rect", fill="grey")
        for i in range(0,size):
            for j in range(0,size):
                if map[i][j] == 1: 
                    item_id = self.rect[i,j]
                    self.canvas.itemconfig(item_id, fill=color)

        self.after(delay, lambda: self.redraw(map,delay,color))
    
    def start(self,map,alive):
        starting_alive = alive
        print(starting_alive)
        size = numpy.size(map,1)
        for i in range(starting_alive):
            row = random.randint(0,size-1)
            col = random.randint(0,size-1)
            map[row][col] = 1
    
    def deal_with_it(self,map,coord,neighbors):
        (row,col) = coord
        if map[row][col] == 1:
            if neighbors < 2:
                map[row][col] = 0
            elif neighbors > 3:
                map[row][col] = 0
        else:
            if neighbors == 3:
                map[row][col] = 1
        return map
    
    def play(self,map):
        staticmap = copy.deepcopy(map)
        size = numpy.size(map,1)
        for i in range(0,size):
            for j in range(0,size):
                coords = (i,j)
                neighbors = self.check_neighbors(staticmap,coords)
                map = self.deal_with_it(map,coords,neighbors)
        return map
    
    def check_neighbors(self,map,coord):
        (row,col) = coord
        neighbors = 0
        length = numpy.size(map,1) - 1
        #check top left
        if row-1 >=0 and col-1 >=0:
            if map[row-1][col-1] == 1:
                neighbors += 1
        #check top middle
        if col-1 >= 0:
            if map[row][col-1] == 1:
                neighbors += 1
        #check top right
        if row+1 < length and col-1 >=0:
            if map[row+1][col-1] == 1:
                neighbors += 1
        #check left
        if row-1 >= 0:
            if map[row-1][col] == 1:
                neighbors += 1
        #check right
        if row+1 < length:
            if map[row+1][col] == 1:
                neighbors += 1
        #check bottom left
        if row-1 >=0 and col+1 < length:
            if map[row-1][col+1] == 1:
                neighbors += 1
        #check bottom middle
        if col+1 < length:
            if map[row][col+1] == 1:
                neighbors += 1
        #check top right
        if row+1 < length and col+1 < length:
            if map[row+1][col+1] == 1:
                neighbors += 1
        return neighbors

class Start_Screen(tk.Tk):
    def letsgo(self,size,alive,color):
        rows= size
        cols = size
        app = App()
        self.destroy()
        app.run(rows,cols,alive,color)
        app.mainloop()
        

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Conways Game of Life Setup")

        tk.Label(self, text='Size of Game').grid(row=0) 
        tk.Label(self, text='Number of Starting Squares').grid(row=1)
        tk.Label(self, text='Choose your color').grid(row=2) 

        size = tk.Scale(self, from_=10, to=100, orient='horizontal') 
        size.grid(row=0, column=1) 
        
        start = tk.Scale(self, from_=20, to=200, orient='horizontal') 
        start.grid(row=1, column=1)

        color = tk.Entry(self)
        color.insert(0,"Green")
        color.grid(row=2,column=1)


        button = tk.Button(self, text='Start', width=25, command=lambda: self.letsgo(size.get(),start.get(),color.get()))
        button.grid(row=3,column=1)

        quit = tk.Button(self, text='Quit', width=25, command=self.destroy)
        quit.grid(row=3,column=0)
    
    
if __name__ == "__main__":
    start = Start_Screen()
    start.mainloop()
    