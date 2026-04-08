import random

class WordLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_random_word(self):
        with open(self.filepath) as f:
            words = f.read().splitlines()
        return random.choice(words)