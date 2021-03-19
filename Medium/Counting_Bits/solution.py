class counting_bits:
    def get_bits(self,numby):
        binarry = []
        for i in range(numby+1):
            binarry.append(int((bin(i)[2:]).count('1')))
        return binarry