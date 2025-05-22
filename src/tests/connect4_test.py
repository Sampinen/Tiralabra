#pylint: skip-file
import unittest
from connect4 import ConnectFour
class TestConnect4(unittest.TestCase):
    def setUp(self):
        self.game = ConnectFour()

    def test_check_cell_returns_False_when_cell_is_empty(self):
        self.assertEqual(self.game.check_cell(1,1,"X"),False)

    def test_check_cell_returns_true_when_it_matches_the_players_symbol(self):
        self.game.play(1,"X")
        self.assertEqual(self.game.check_cell(1,1,"X"),True)

    def test_check_win_returns_false_if_the_board_is_empty(self):
        self.assertEqual(self.game.check_win("X"), False)

    def test_check_horizontal_returns_false_if_the_board_is_empty(self):
        self.assertEqual(self.game.check_horizontal(1,1,"X"), False)

    def test_check_horizontal_returns_true_with_hortizontal_win(self):
        self.game.play(1,"X")
        self.game.play(2, "X")
        self.game.play(3,"X")
        self.game.play(4,"X")
        self.assertEqual(self.game.check_horizontal(1,1,"X"), True)

    def test_check_vertical_returns_false_when_board_is_empty(self):
        self.assertEqual(self.game.check_vertical(1,1,"X"),False)