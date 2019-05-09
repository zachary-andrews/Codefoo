from itertools import cycle

class bowling:
    def remove_gutters(self, game):
        return game.replace('-','0')
                
    def combine(self, frames):
        for i in range(10):
            if frames[i][0] == "X":
                if frames[i+1][0] == "X":
                    if frames[i+2][0] == "X":
                        #turky
                        frames[i] = 30
                    else:
                        #strike numby
                        frames[i] = 20 + int(frames[i+2][0],10)
                elif frames[i+1][1] == "/":
                    # numby spare
                    frames[i] = 20
                else:
                    # you goofed
                    frames[i][0] = 10 + int(frames[i+1][0],10) + int(frames[i+1][1],10)
            
            elif frames[i][1] == "/":
                if frames[i+1][0] == 'X':
                    frames[i] = 10 + 10
                else:
                    frames[i] = 10 + int(frames[i+1][0],10)
            else:
                frames[i] = int(frames[i][0],10) + int(frames[i][1],10)
        return frames

    def get_score(self, game):
        frames = self.remove_gutters(game).split(" ")
        score = 0
        combined_frames = self.combine(frames)
        for i in range(10):
            score = score + frames[i]
        return score


