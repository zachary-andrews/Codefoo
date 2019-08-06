import collections

class LRUCache:
    def __init__(self, size: int) -> None:
        self.size = size
        self.array = collections.deque(maxlen=size)
    
    def put(self, key: int, value: int) -> None:
        tuple = (key,value)
        self.array.append(tuple)

    def get(self, key: int) -> int:
        for count, tuple in enumerate(self.array):
            if tuple[0] == key:
                self.array.remove(tuple)
                self.array.append(tuple)
                return tuple[1]
            else:
                return -1