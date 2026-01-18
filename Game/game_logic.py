from .board import Board
from .player import HumanPlayer
from .utils import GameValidator

class TicTacToe:
    """Основной класс игры"""
    
    def __init__(self):
        self.board = Board()
        self.players = [HumanPlayer('X'), HumanPlayer('O')]
        self.current_player_index = 0
        self.winner = None
        self.game_over = False
    
    @property
    def current_player(self):
        """Возвращает текущего игрока"""
        return self.players[self.current_player_index]
    
    def switch_player(self):
        """Переключает текущего игрока"""
        self.current_player_index = (self.current_player_index + 1) % 2
    
    def play_turn(self):
        """Выполняет один ход игры"""
        self.board.display(self.current_player.marker)
        
        position = self.current_player.make_move(self.board)
        
        if position is None:  # Игрок хочет выйти
            self.game_over = True
            return
        
        # Устанавливаем маркер на доске
        self.board.place_marker(position, self.current_player.marker)
        
        # Проверяем условия окончания игры
        self.winner = GameValidator.check_winner(self.board)
        
        if self.winner:
            self.game_over = True
        elif self.board.is_full():
            self.game_over = True
        else:
            self.switch_player()
    
    def play(self):
        """Основной игровой цикл"""
        print("Добро пожаловать в игру Крестики-нолики!")
        print("Ходы вводятся в формате: ряд столбец (например: 1 2)")
        input("Нажмите Enter чтобы начать...")
        
        while not self.game_over:
            self.play_turn()
        
        self.show_game_result()
    
    def show_game_result(self):
        """Показывает результат игры"""
        self.board.display()
        
        if self.winner:
            winner_name = "Крестики (X)" if self.winner == 'X' else "Нолики (O)"
            color = '\033[92m'  # Зеленый
            
            print(color + "="*30 + "\033[0m")
            print(color + f"   Победили {winner_name}!  " + "\033[0m")
            print(color + "="*30 + "\033[0m")
        else:
            print("\033[93m" + "="*30 + "\033[0m")  # Желтый
            print("\033[93m       Ничья!                \033[0m")
            print("\033[93m" + "="*30 + "\033[0m")
    
    def reset(self):
        """Сбрасывает игру в начальное состояние"""
        self.board.reset()
        self.current_player_index = 0
        self.winner = None
        self.game_over = False