import unittest
from src.game_board import GameBoard
from src.players import HumanPlayer, AIPlayer

class TestIntegration(unittest.TestCase):
    
    def test_ai_never_loses_3x3(self):
        """Тест: ИИ никогда не проигрывает на поле 3x3"""
        # Симулируем игру человека против ИИ
        board = GameBoard(3, 3)
        human = HumanPlayer('X')
        ai = AIPlayer('O')
        
        # Ход человека в угол
        board.make_move(0, 0, 'X')
        # Ход ИИ
        move = ai.get_move(board)
        board.make_move(move[0], move[1], 'O')
        
        # Ход человека для создания "вилки"
        board.make_move(2, 2, 'X')
        # Ход ИИ должен заблокировать угрозу
        move = ai.get_move(board)
        
        # Проверяем, что ИИ не проиграл после этих ходов
        self.assertFalse(board.check_win('X'))

if __name__ == '__main__':
    unittest.main()