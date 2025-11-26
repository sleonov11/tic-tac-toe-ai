from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, symbol: str):
        if symbol not in ("X", "O"):
            raise ValueError("Символ должен быть 'X' или 'O'")
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board)-> tuple[int, int]:
        pass

class HumanPlayer(Player):
    def get_move(self, board) -> tuple[int, int]:
        while True:
            try:
                user_input = input(f"Игрок {self.symbol}, введите ход (строка столбец):").strip()
                parts = user_input.split()
                if len(parts) != 2:
                    print("Ошибка: введите два числа, разделённых пробелом.")
                    continue
                row, col = int(parts[0]), int(parts[1])
                if not board.is_valid_move(row, col):
                    print("Ошибка: ход недопустим (вне поля или клетка занята).")
                    continue
                return (row, col)
            except ValueError:
                print("Ошибка: введите целые числа.")
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")

class AIPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.oponent_sybbol = "O" if symbol == 'X' else "X"
        self.nodes_visited = 0
        self.prune_count = 0

    def get_move(self, board) -> tuple[int, int]:
        self.nodes_visited = 0
        self.prune_count = 0

        _, best_move = self._minimax(
            board = board.clone()
            depth = 0
            is_maximizing = True
            alpha = float('-inf')
            beta = float('inf')
        )
        print(f"ИИ ({self.symbol}): проанализировано узлов = {self.nodes_visited}, отсечений = {self.prune_count}")

        return best_move
    
    def _minimax(self, board, depth:int, is_maximizing:str, alpha:float, beta:float):
        pass
