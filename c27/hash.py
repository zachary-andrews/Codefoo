
hashmap = [None] * 25

def get_numbys(key):
    spot = 0
    for char in key:
        spot += ord(char)
    return spot % 25

def open_spot(spot):
    if hashmap[spot] is None:
        return True
    else:
        return False 

def add_to_map(key,value):
    spot = get_numbys(key)
    if open_spot(spot):
        hashmap[spot] = [(key,value)]
    else:
        hashmap[spot].append((key,value))

def get_from_map(key):
    spot = get_numbys(key)
    if hashmap[spot] is None:
        return "could not find input"
    for tup in hashmap[spot]:
        if tup[0] == key:
            return tup[1] 

if __name__ == "__main__":
    add_to_map("key1","hello")
    print hashmap

    add_to_map("key2","check")
    print hashmap

    add_to_map("key2","ksdjfghsdg")
    print hashmap

    add_to_map("key3","R")
    print hashmap

    print get_from_map("key1")
    print get_from_map("key2")
    print get_from_map("key3")
    