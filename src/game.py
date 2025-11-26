from src.game_board import GameBoard
from src.players import HumanPlayer, AIPlayer

class Game:
    def __init__(self, player1: Player, player2: Player, n: int, k: int):
        self.board = GameBoard(n, k)
        self.players = [player1, player2]
        self.current_player_index = 0

    def start(self):
        while not self.board.is_full():
            print(self.board)
            current_player = self.players[self.current_player_index]
            move = current_player.get_move(self.board)
            self.board.make_move(move[0], move[1], current_player.symbol)
            
            if self.board.check_win(current_player.symbol):
                print(f"\nПобедил {current_player.symbol}!")
                print(self.board)
                return
            
            self.current_player_index = 1 - self.current_player_index
        
        print("Ничья!")
        print(self.board)