class Game:
    def __init__(self, word):
        self.word = word
        self.guessed = ["_"] * len(word)
        self.attempts = 6

    def guess(self, letter):
        if letter in self.word:
            for i, l in enumerate(self.word):
                if l == letter:
                    self.guessed[i] = letter
            return True
        else:
            self.attempts -= 1
            return False
    
    def is_won(self):
        return "_" not in self.guessed
    
    def is_lost(self):
        return self.attempts <= 0
    
    # def display_hangman(self):
    #     return STAGES[6 - self.attempts]