import sys
import math
class tree:
    def make_tree(size):
        row_len = 2*size+1
        for i in range(size):
            num_stars = 2*(i+1)-1
            print("."*math.trunc((row_len-num_stars)/2)+"*"*num_stars+"."*math.trunc((row_len-num_stars)/2))
        print("."*math.trunc((row_len)/2)+"*"+"."*math.trunc((row_len)/2))        
    
    if __name__ == "__main__":
        make_tree(1)
        print ""
        make_tree(3)
        print ""
        make_tree(5)
        print ""
        make_tree(12)