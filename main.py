from src.player import Player
from src.game import Game
from src.word_loader import WordLoader
from src.scoreboard import Scoreboard
from src.stages import Stages

loader = WordLoader("data/words.txt")
word = loader.get_random_word()

game = Game(word)
player = Player(input("Your name: "))

while not game.is_won() and not game.is_lost():
    print("Word:", " ".join(game.guessed))
    print("Attempts left: ", game.attempts)
    print(Stages.STAGES[6 - game.attempts])

    letter = input("Guess letter : ")

    if not letter.isalpha():
        print("Invalid input")
        continue

    game.guess(letter)


if game.is_won():
    print("You won!")
    player.add_score(10)
else:
    print("You lost, word was: ", word)

Scoreboard().save(player.name, player.score)