from random import shuffle
import numpy as np

    
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
avrage = 0 
for x in range(0,3):
    stateholder = []
    count = 0
    copy_numbers = [i for i in numbers]

    while copy_numbers not in stateholder:
        stateholder.append([i for i in copy_numbers])
        shuffle(copy_numbers)
        count += 1 
    print "Run %d: %d iterations"%(x,count)
    avrage = avrage + count

print "%d Items, Run average = %d"%(len(numbers),avrage/3)
