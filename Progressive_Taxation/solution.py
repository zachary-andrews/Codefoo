import math
class tax:
    def get(self, tax: int) -> int:
        if tax < 10000:
            return tax
        elif tax < 30000: 
            return math.trunc((tax - 10000)*.10)
        elif tax < 100000:
            return math.trunc((tax-30000)*.25+2000)
        else:
            return math.trunc((tax-100000)*.40+19500)