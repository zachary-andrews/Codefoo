import collections
from collections import Counter
two=0
three=0
f2 = open("./input.txt", 'r')
for line in f2.readlines():
    c=Counter(line)
    updateset = set(c.values())
    updateset.remove(1)
    if 2 in updateset:
        two = two+1
    if 3 in updateset:
        three = three+1
    print two,three
print two*three