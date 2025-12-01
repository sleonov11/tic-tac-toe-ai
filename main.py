from src.players import AIPlayer, HumanPlayer
from src.game import Game

def main():
    try:
        n = int(input("Введите размер поля n (минимум 3): "))
        k = int(input(f"Введите количество подряд для победы k (от 3 до {n}): "))
        if n < 3 or not (3 <= k <= n):
            raise ValueError
    except ValueError:
        print("Некорректные значения. Используем n=3, k=3.")
        n, k = 3, 3

    human = HumanPlayer('X')
    ai = AIPlayer('O', n)
    game = Game(human, ai, n=n, k=k)
    game.start()

if __name__ == "__main__":
    main()