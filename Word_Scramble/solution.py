class unscramble:

    def get_word(self, scramble):
        wordarr = []
        if len(scramble) %2 != 0:
            scramble = scramble[1:]+scramble[0]
        for i in range(0, len(scramble), 2):
            wordarr.append(scramble[i:i + 2][::-1])
        print(wordarr)
        return ''.join(wordarr)