class game:
    def __init__(self):
        self.length = 0
        self.height = 0
        self.win = False
        self.field = []
        self.set_field()
        self.height = len(self.field)
        self.length = len(self.field[0])
        self.start = (0,0)
        self.set_start()
        self.end = (0,0)
        self.set_end()
        self.x = self.start[0]
        self.y = self.start[1]

    def set_field(self):
        ins = open( "field.txt", "r" )
        for line in ins:
            self.field.append(line.rstrip('\n'))
        ins.close()
    
    def get_field(self):
        return self.field

    def set_start(self):
        for i in self.field:
            if 'M' in i:
                y = self.field.index(i)
                x = self.field[y].index('M')
                self.start= (x,y)
    
    def get_start(self):
        return self.start

    def set_end(self):
        #check the top row
        if '0' in self.field[0]:
            x = self.field[0].index('0')
            self.end = (x,0)
        elif '0' in self.field[-1]:
            x = self.field[self.height].index('0')
            self.end = (x,-1)
        else:
            for y,row in enumerate(self.field):
                if row[0] == '0':
                    self.end = (0,y)
                elif row[-1] == '0':
                    self.end = (self.length-1,y)
            
    def get_end(self):
        return self.end

    def is_mine(self, x: int, y: int):
        if self.field[x][y] == '*':
            return True
        else:
            return False

    def check_south(self):
        if self.y+1 > self.height:
            return False
        if self.field[self.y+1][self.x] == '*':
            return False
        elif self.field[self.y+1][self.x] == '+':
            return False
        else:
            return True

    def check_north(self):
        if self.y-1 < 0:
            return False
        if self.field[self.y-1][self.x] == '*':
            return False
        elif self.field[self.y-1][self.x] == '+':
            return False
        else:
            return True

    def check_east(self):
        if self.x+1 > self.length-1:
            return False
        if self.field[self.y][self.x+1] == '*':
            return False
        elif self.field[self.y][self.x+1] == '+':
            return False
        else:
            return True

    def check_west(self):
        if self.x-1 < 0:
            return False
        if self.field[self.y][self.x-1] == '*':
            return False
        elif self.field[self.y][self.x-1] == '+':
            return False
        else:
            return True

    def get_location(self):
        return (self.x,self.y)

    def move_south(self):
        self.y += 1
        return "S" 
    
    def move_north(self):
        self.y -= 1
        return "N" 
    
    def move_east(self):
        self.x += 1
        return "E"
    
    def move_west(self):
        self.x -= 1
        return "W"

    def winner(self):
        if (self.x,self.y) == self.end:
            return True
        else:
            return False