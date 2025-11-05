class GameBoard:
    
    def __init__(self, n: int, k: int):
        self.n = n
        self.k = k
        if n < 3:
            raise ValueError("Размер поля должен быть не менее 3")
        if not(3 <= k <= n):
            raise ValueError('Значение k должно быть в диапазоне от 3 до n')
        
        self._board = [['.' for _ in range(n)] for _ in range(n)]
        self._move_count = 0

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self._board)
    
    def is_valid_move(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.n and self._board[row][col] == '.'
    
    def is_full(self) -> bool:
        return self._move_count == self.n * self.n

    def make_move(self, row, col, player):
        if player not in ('X', 'O'):
            raise ValueError('Игрок должен быть X или O')
        if self.is_valid_move(row, col):
            self._board[row][col] = player
            self._move_count += 1
            return True
        return False

    def get_cell(self, row, col):
        return self._board[row][col]
    
    def check_win(self, player):
        pass #TODO: Implement win check
            
    
    
