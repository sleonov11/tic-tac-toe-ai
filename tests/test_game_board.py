import unittest
from src.game_board import GameBoard

class TestGameBoard(unittest.TestCase):
    
    def test_win_horizontal(self):
        board = GameBoard(3, 3)
        board.make_move(0, 0, 'X')
        board.make_move(0, 1, 'X')
        board.make_move(0, 2, 'X')
        self.assertTrue(board.check_win('X'))
        
    def test_win_vertical(self):
        board = GameBoard(3, 3)
        board.make_move(0, 0, 'O')
        board.make_move(1, 0, 'O')
        board.make_move(2, 0, 'O')
        self.assertTrue(board.check_win('O'))
        
    def test_win_diagonal(self):
        board = GameBoard(3, 3)
        board.make_move(0, 0, 'X')
        board.make_move(1, 1, 'X')
        board.make_move(2, 2, 'X')
        self.assertTrue(board.check_win('X'))
        
    def test_no_win(self):
        board = GameBoard(3, 3)
        board.make_move(0, 0, 'X')
        board.make_move(0, 1, 'X')
        self.assertFalse(board.check_win('X'))
        
    def test_clone_board(self):
        board = GameBoard(3, 3)
        board.make_move(0, 0, 'X')
        clone = board.clone()
        clone.make_move(0, 1, 'O')
        self.assertNotEqual(board._board[0][1], clone._board[0][1])
        
    def test_available_moves(self):
        board = GameBoard(3, 3)
        board.make_move(0, 0, 'X')
        moves = board.get_available_moves()
        self.assertEqual(len(moves), 8)
        self.assertNotIn((0, 0), moves)

if __name__ == '__main__':
    unittest.main()