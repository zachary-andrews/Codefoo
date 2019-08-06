import collections

class Flowers:
    def check_sides(self, i):
        right_check = False
        left_check = False
        if self.bed[i-1] >= 0:
            if self.bed[i-1] == 0:
                left_check = True
        if self.bed[i+1] < self.len:
            if self.bed[i+1] == 0:
                right_check = True
        if right_check and left_check:
            self.bed[i] = 1
            return 1 
        else: 
            return 0

    def number_adjacent(self):
        total = 0
        for i in range(self.len):
            if self.bed[i] == 0:
                total += self.check_sides(i)       
        return total

    def check(self, bed, flowers):
        self.bed = bed
        self.flowers = flowers
        self.len = len(bed)
        if self.flowers <= self.number_adjacent():
            return True
        else: 
            return False

    