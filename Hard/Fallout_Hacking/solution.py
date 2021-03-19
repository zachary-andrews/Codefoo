from game import game
from collections import Counter
import copy
import random

class solution:
    def __init__(self):
        difficulty_options = ["easy", "average", "hard"]
        self.difficulty = input("Choose your difficulty (easy, average, hard)? ")

        if self.difficulty not in difficulty_options:
            print("you bot thats not an option")
            exit(1)
        self.Game = game(self.difficulty)

    def start_game(self):
        self.clue_words = self.Game.get_clue_words()

    def print_clue_words(self):
        for word in self.clue_words:
            print(word)

    def chars_per_index(self):
        self.chars = [''] * len(self.clue_words[0])
        for word in self.clue_words:
            for n,letter in enumerate(word):
                self.chars[n] += letter

    def print_chars_per_index(self):
        for n in self.chars:
            print(n)

    def get_guess(self):
        guess = []
        tmpwords = copy.copy(self.clue_words)
        for num in range(0,len(self.clue_words[1])):
            letters=[]
            for word in tmpwords:
                letters.append(word[num])
            counts = Counter(letters)
            least_used_char = random.choice(counts.most_common())
            guess.append(least_used_char[0])
        return "".join(guess)

    def get_passphrase(self):
        return self.Game.get_passphrase()

    def validate(self,word,guess,output):
        count = 0
        for n,l in enumerate(word):
            if l == guess[n]:
                count += 1
        if count != output:
            return False
        else:
            return True

    def solve(self):
        for checks in range(0,4):
            print(self.clue_words)
            #if there is only one option then guess that one
            if len(self.clue_words) == 1:
                guess = self.clue_words[0]
            else:
                #if its your last guess just pick one
                if checks == 3:
                    guess = random.choice(self.clue_words)
                else:
                    guess = self.get_guess()

            output = self.Game.check_one(guess)

            print(guess)
            print(output)

            if output == len(self.clue_words[0]):
                return True
            else:
                for word in self.clue_words:
                    if not self.validate(word,guess,output):
                        self.clue_words.remove(word)
        return False

if __name__ == '__main__':
    Solution = solution()
    Solution.start_game()
    print("--------------")
    if Solution.solve():
        print("Congrats you win! The passphrase was %s"%Solution.get_passphrase())
    else:
        print("Sorry you lost! The passphrase was %s"%Solution.get_passphrase())
