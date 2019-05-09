import random

class importID:
    def create_id(self):
        return random.randint(1,1000)
    
    def number_of_ids(self, totalIDs):
        ids = []
        if totalIDs > 1000:
            return -1
        while len(ids) != totalIDs:
            id = self.create_id()
            if id not in ids:
                ids.extend([id])
        return ids
