import random
import tkinter as tk
import numpy
import copy

class Start_Screen(tk.Tk):
    def letsgo(self,rows,cols,start):
        print(rows,cols,start)
        print("hello")

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Conways Game of Life")

        tk.Label(self, text='Number of Rows').grid(row=0) 
        tk.Label(self, text='Number of Cols').grid(row=1) 
        tk.Label(self, text='Number of Starting Squares').grid(row=2)

        rows = tk.Scale(self, from_=10, to=200, orient='horizontal') 
        rows.grid(row=0, column=1) 

        cols = tk.Scale(self, from_=10, to=200, orient='horizontal') 
        cols.grid(row=1, column=1)
        
        start = tk.Scale(self, from_=10, to=50, orient='horizontal') 
        start.grid(row=2, column=1)

        button = tk.Button(self, text='Start', width=25, command=lambda: self.letsgo(rows.get(),cols.get(),start.get()))
        button.grid(row=3,column=1)

        quit = tk.Button(self, text='Quit', width=25, command=self.destroy)
        quit.grid(row=3,column=0)
    
    
if __name__ == "__main__":
    start = Start_Screen()
    start.mainloop()