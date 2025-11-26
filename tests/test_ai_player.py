import unittest
from src.game_board import GameBoard
from src.players import AIPlayer

class TestAIPlayer(unittest.TestCase):
    
    def test_ai_blocks_win(self):
        """Тест: ИИ должен блокировать победу человека"""
        board = GameBoard(3, 3)
        board.make_move(0, 0, 'X')
        board.make_move(0, 1, 'X')
        
        ai = AIPlayer('O')
        move = ai.get_move(board)
        self.assertEqual(move, (0, 2), f"Ожидался ход (0,2), получен {move}")
    
    def test_ai_takes_win(self):
        """Тест: ИИ должен выиграть, если есть возможность"""
        board = GameBoard(3, 3)
        board.make_move(0, 0, 'O')
        board.make_move(0, 1, 'O')
        
        ai = AIPlayer('O')
        move = ai.get_move(board)
        self.assertEqual(move, (0, 2), f"Ожидался ход (0,2), получен {move}")
    
    def test_ai_center_strategy(self):
        """Тест: ИИ должен ходить в центр на пустом поле 3x3"""
        board = GameBoard(3, 3)
        ai = AIPlayer('X')
        move = ai.get_move(board)
        self.assertEqual(move, (1, 1), f"Ожидался ход в центр (1,1), получен {move}")

if __name__ == '__main__':
    unittest.main()