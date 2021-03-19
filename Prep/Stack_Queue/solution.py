class stack:
    def __init__(self):  
        self.queue = []  
    def push(self, adder: int) -> int:
        self.queue.append(adder)
    def peek(self):
        return(self.queue[0])
    def pop(self) -> int:
        return(self.queue.pop(0))
    def empty(self):
        if len(self.queue) >0:
            return False
        else:
            return True 