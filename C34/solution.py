import random

class ID:
    def create_ids(self,number_of_ids):
        ids = []
        id_counter = 1
        if number_of_ids > 1000:
            return -1
        for x in range(number_of_ids):
            ids.extend([id_counter])
            id_counter += 1
        return ids


