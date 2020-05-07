import game

def test_to_coords():
    assert game.to_coords(game.square) == {
        (0, 0),
        (0, 1),
        (1, 1),
        (1, 0)
    }
