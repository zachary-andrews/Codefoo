import random
import numpy

def flip_cakes(num,cake_stack):
    cake_stack[0:num] = cake_stack[0:num][::-1]
    return cake_stack

def check_stack(cake_stack):
    if all(cake_stack[i] <= cake_stack[i+1] for i in xrange(len(cake_stack)-1)):
        return True
    else:
        flip_cakes(random.randint(0,num_cakes),cake_stack)
num_cakes = 10
cake_stack = [3, 12, 8, 12, 4, 7, 10, 3, 8, 10]

count = 0
cake_stack_list = ''.join(str(e) for e in cake_stack)
while not check_stack(cake_stack):
    #cake_stack_list = cake_stack_list + " -> " + ''.join(str(e) for e in cake_stack)
    count = count + 1 

#print("%d flips: %s"%(count,cake_stack_list))
print("Order up!")
print count
