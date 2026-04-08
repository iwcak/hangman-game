from src.game import Game


def test_correct_guess():
    game = Game("abc")
    assert game.guess("a") == True


def test_wrong_guess():
    game = Game("abc")
    assert game.guess("x") == False


def test_win():
    game = Game("a")
    game.guess("a")
    assert game.is_won()


def test_loss():
    game = Game("a")
    for _ in range(6):
        game.guess("x")
    assert game.is_lost()

def test_invalid_guess():
    game = Game("abc")
    assert game.guess("2") == False

def test_space_guess():
    game = Game("abc")
    assert game.guess(" ") == False