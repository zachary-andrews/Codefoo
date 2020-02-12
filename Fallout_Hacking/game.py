import requests
import random

class game:
    def __init__(self,difficulty):
        self.passphrase, self.clue_words = self.create_game(difficulty)


    def get_all_words(self):
        word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = requests.get(word_site)
        return response.content.splitlines()

    def create_game(self,difficulty):
        difficulty_switch = {
            "very easy": 3,
            "easy": 4,
            "average": 5,
            "hard": 7,
            "very hard": 12
        }

        words = self.get_all_words()
        size = difficulty_switch.get(difficulty)
        filtered_words = [word.decode().upper() for word in words if len(word) <= size and len(word) >= size-3]

        passphrase = random.choice(filtered_words)

        same_length_words = [word for word in filtered_words if len(word) == len(passphrase)]
        clue_words = random.choices(same_length_words,k=5)
        clue_words.append(passphrase)
        random.shuffle(clue_words)

        return passphrase,clue_words

    def check(self,guess):
        correct = 0
        for n,c in enumerate(guess):
            if c == self.passphrase[n]:
                correct += 1
        return correct

    def get_length(self):
        return len(self.passphrase)

    def get_clue_words(self):
        return self.clue_words

    def get_passphrase(self):
        print(self.passphrase)

    def play(self):
        print('\n'.join(self.clue_words))
        for x in range(4,0,-1):
            guess = input("Guess? (%d left) "%(x))
            check = self.check(guess)
            if check == len(self.passphrase):
                return(True)
            print("%d/%d Correct"%(check,len(self.passphrase)))
        return(False)

if __name__ == '__main__':
    difficulty_options = ["very easy", "easy", "average", "hard", "very hard"]
    difficulty = input("Choose your difficulty (very easy, easy, average, hard, very hard)? ")
    if difficulty not in difficulty_options:
        print("you bot thats not an option")
        exit(1)

    Game = game(difficulty)
    print("You win!") if Game.play() else print("You Lose. The phrase was %s"%(Game.get_passphrase()))
