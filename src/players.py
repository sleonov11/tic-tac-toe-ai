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
        self.opponent_symbol = "O" if symbol == 'X' else "X"
        self.nodes_visited = 0
        self.prune_count = 0

    def get_move(self, board) -> tuple[int, int]:
        self.nodes_visited = 0
        self.prune_count = 0

        _, best_move = self._minimax(
            board.clone(),
            0,
            True,
            float('-inf'),
            float('inf')
        )
        print(f"ИИ ({self.symbol}): проанализировано узлов = {self.nodes_visited}, отсечений = {self.prune_count}")

        return best_move
    
    def _evaluate_board(self, board):
        """Оценочная функция: +10 за победу ИИ, -10 за победу противника, 0 иначе"""
        if board.check_win(self.symbol):
            return 10
        if board.check_win(self.opponent_symbol):
            return -10
        return 0
    
    def _minimax(self, board, depth:int, is_maximizing:bool, alpha:float, beta:float):
        self.nodes_visited += 1

        score = self._evaluate_board(board)
        if score != 0 or board.is_full():
            return score, None
        
        MAX_DEPTH = 10
        if depth >= MAX_DEPTH:
            return self._evaluate_board(board), None
        
        best_move = None

        if is_maximizing:
            best_value = -float('inf')
            for move in board.get_available_moves():
                new_board =  board.clone()
                new_board.make_move(move[0], move[1], self.symbol)
                val, _ = self._minimax(new_board, depth+1, False, alpha, beta)
                
                if val > best_value:
                    best_value = val
                    best_move = move
                alpha = max(alpha, best_value)
                if alpha >= beta:
                    self.prune_count += 1
                    break # отсечение
            return best_value, best_move
        
        else:
            best_value = float('inf')
            for move in board.get_available_moves():
                new_board =  board.clone()
                new_board.make_move(move[0], move[1], self.opponent_symbol)
                val, _ = self._minimax(new_board, depth+1, True, alpha, beta)
                
                if val < best_value:
                    best_value = val
                    best_move = move
                beta = min(beta, best_value)
                if alpha >= beta:
                    self.prune_count += 1
                    break
            return best_value, best_move




