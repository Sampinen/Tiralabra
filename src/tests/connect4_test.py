#pylint: skip-file
import unittest
from connect4 import ConnectFour
class TestConnect4(unittest.TestCase):
    def setUp(self):
        self.game = ConnectFour()
        self.board = self.game.board
        self.played =self.game.played
        self.columnorder = self.game.columnorder

    def test_play_piece(self):
        self.assertEqual(self.board[1][1],"  ")
        self.game.play(1,"X ",self.board,self.played)
        self.assertEqual(self.board[1][1],"X ")

    def test_check_win_returns_false_if_the_board_is_empty(self):
        self.assertEqual(self.game.check_win_cell(1,1,"X",self.board), False)

    def test_check_win_returns_true_with_hortizontal_win(self):
        self.game.play(1,"X",self.board,self.played)
        self.game.play(2, "X",self.board,self.played)
        self.game.play(3,"X",self.board,self.played)
        self.game.play(4,"X",self.board,self.played)
        self.assertEqual(self.game.check_win_cell(1,1,"X",self.board), True)

    def test_check_win_returns_true_with_vertical_win(self):
        self.game.play(1,"X",self.board,self.played)
        self.game.play(1,"X",self.board,self.played)
        self.game.play(1,"X",self.board,self.played)
        self.game.play(1,"X",self.board,self.played)
        self.assertEqual(self.game.check_win_cell(4,1,"X",self.board),True)

    def test_check_win_returns_true_with_diagnoal_up_win(self):
        self.game.play(1,"X",self.board,self.played)

        self.game.play(2,"Y",self.board,self.played)
        self.game.play(2,"X",self.board,self.played)

        self.game.play(3,"Z",self.board,self.played)
        self.game.play(3,"Z",self.board,self.played)
        self.game.play(3,"X",self.board,self.played)

        self.game.play(4,"Å",self.board,self.played)
        self.game.play(4,"Å",self.board,self.played)
        self.game.play(4,"Å",self.board,self.played)
        self.game.play(4,"X", self.board,self.played)

        self.assertEqual(self.game.check_win_cell(1,1,"X",self.board),True)

    def test_check_win_returns_true_with_diagnoal_down_win(self):
        self.game.play(1,"Å",self.board,self.played)
        self.game.play(1,"Å",self.board,self.played)
        self.game.play(1,"Å",self.board,self.played)
        self.game.play(1,"X",self.board,self.played)

        self.game.play(2,"Z",self.board,self.played)
        self.game.play(2,"Z",self.board,self.played)
        self.game.play(2,"X",self.board,self.played)

        self.game.play(3,"Y",self.board,self.played)
        self.game.play(3,"X",self.board,self.played)

        self.game.play(4,"X",self.board,self.played)

        self.assertEqual(self.game.check_win_cell(4,1,"X",self.board),True)

    def test_get_valid_columns_removes_full_columns(self):
        self.assertEqual(1 in self.columnorder, True)
        self.game.play(1,"Å",self.board,self.played)
        self.game.play(1,"Å",self.board,self.played)
        self.game.play(1,"Å",self.board,self.played)
        self.game.play(1,"X",self.board,self.played)
        self.game.play(1,"Å",self.board,self.played)
        self.game.play(1,"Å",self.board,self.played)
        self.game.get_valid_columns(self.played,self.columnorder)
        self.assertEqual(1 in self.columnorder, False)