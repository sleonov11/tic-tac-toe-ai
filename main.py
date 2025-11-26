from src.game_board import GameBoard
from src.players import HumanPlayer, AIPlayer

def main():
    print("Крестики-нолики с ИИ (минимакс + alpha-beta отсечение)")
    
    # Ввод параметров игры
    try:
        n = int(input("Введите размер поля (минимум 3): "))
        k = int(input(f"Введите количество символов для победы (от 3 до {n}): "))
        if n < 3 or not (3 <= k <= n):
            raise ValueError
    except (ValueError, KeyboardInterrupt):
        print("Некорректные параметры. Используем стандартные: поле 3×3, k=3.")
        n, k = 3, 3

    # Создание игроков
    human = HumanPlayer('X')
    ai = AIPlayer('O')
    board = GameBoard(n, k)
    current_player = human

    print("\nИгра началась! Вводите ходы в формате: строка столбец (например: 1 2)")

    # Основной игровой цикл
    while not board.is_full():
        print("\nТекущее поле:")
        print(board)
        
        move = current_player.get_move(board)
        board.make_move(move[0], move[1], current_player.symbol)
        
        # Проверка победы
        if board.check_win(current_player.symbol):
            print(f"\n Игрок {current_player.symbol} победил!")
            print(board)
            return
        
        # Переключение игрока
        current_player = ai if current_player == human else human
    
    # Ничья
    print("\n Ничья!")
    print(board)

if __name__ == "__main__":
    main()