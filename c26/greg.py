from random import shuffle

items = [0, 1, 2, 3, 4]
history = []
iterations = 0
hasSeenBefore = False

items_copy = [i for i in items]

while not hasSeenBefore:
    shuffle(items_copy)

    if items_copy in history:
        hasSeenBefore = True
    else:
        history.append([i for i in items_copy])
        iterations += 1
print history
print iterations
print items_copy