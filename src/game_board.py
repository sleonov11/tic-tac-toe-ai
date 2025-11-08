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
        if not (0 <= row < self.n and 0 <= col < self.n):
            raise IndexError(f"Координаты ({row}, {col}) выходят за границы поля {self.n}x{self.n}")
        return self._board[row][col]
    
    def check_win(self, player: str) -> bool:
        if player not in ('X', 'O'):
            raise ValueError("Игрок должен быть 'X' или 'O'")
        for row in range(self.n):
            for col in range(self.n):    
                if self._board[row][col] != player:
                    continue
                if (self._check_direction(row, col, 0, 1, player) or  
                    self._check_direction(row, col, 1, 0, player) or   
                    self._check_direction(row, col, 1, 1, player) or   
                    self._check_direction(row, col, 1, -1, player)):  
                    return True
        return False

    def _check_direction(self, row: int, col: int, dr: int, dc: int, player: str) -> bool:
        count = 1 
        r, c = row + dr, col + dc
        while 0 <= r < self.n and 0 <= c < self.n and self._board[r][c] == player:
            count += 1
            r += dr
            c += dc
        r, c = row - dr, col - dc
        while 0 <= r < self.n and 0 <= c < self.n and self._board[r][c] == player:
            count += 1
            r -= dr
            c -= dc
        return count >= self.k
        
    def clone(self) -> 'GameBoard':
        new_board = GameBoard(self.n, self.k)
        new_board._board = [row[:] for row in self._board]
        new_board._move_count = self._move_count
        return new_board