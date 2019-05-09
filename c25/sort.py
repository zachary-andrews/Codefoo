import random
import numpy
flips = 0
def order_cakes(cake_stack):
        if cake_stack.index(max(cake_stack)) == 0:
            return cut_stack(flip_cakes(len(cake_stack),cake_stack))
        else:
            return cut_stack(flip_cakes(len(cake_stack),flip_cakes(cake_stack.index(max(cake_stack))+1,cake_stack)))

def cut_stack(cake_stack):
    return cake_stack[:-1]

def flip_cakes(num,cake_stack):
    globals()['flips'] = globals()['flips'] + 1
    print cake_stack
    print "flip------"
    cake_stack[0:num] = cake_stack[0:num][::-1]
    return cake_stack

def check_stack(cake_stack):
#     if len(cake_stack) <= 1:
#         return True
    if all(cake_stack[i] <= cake_stack[i+1] for i in xrange(len(cake_stack)-1)):
        return True
    else:
        #print cake_stack
        check_stack(order_cakes(cake_stack))


num_cakes = 3
cake_stack = [3, 12, 8, 12, 4, 7, 10, 3, 8, 10]

check_stack(cake_stack)
print flips

print("Order up!")
