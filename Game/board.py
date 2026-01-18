import os

class Board:
    """Класс для работы с игровой доской"""
    
    def __init__(self):
        self.cells = [' ' for _ in range(9)]
    
    def display(self, current_player=None):
        """Отображает текущее состояние доски"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n" + "="*25)
        print("     КРЕСТИКИ-НОЛИКИ")
        print("="*25 + "\n")
        
        if current_player:
            print(f"Ход игрока: {self._colorize_player(current_player)}\n")
        
        print("    1   2   3")
        print("  +---+---+---+")
        
        for i in range(3):
            row = f"{i+1} |"
            for j in range(3):
                cell = self.cells[i*3 + j]
                row += f" {self._colorize_cell(cell)} |"
            print(row)
            print("  +---+---+---+")
        print()
    
    def _colorize_cell(self, cell):
        """Добавляет цвет к символам клетки"""
        if cell == 'X':
            return '\033[91mX\033[0m'  # Красный
        elif cell == 'O':
            return '\033[94mO\033[0m'  # Синий
        return cell
    
    def _colorize_player(self, player):
        """Добавляет цвет к символу игрока"""
        if player == 'X':
            return '\033[91mX\033[0m (Крестики)'
        return '\033[94mO\033[0m (Нолики)'
    
    def reset(self):
        """Сбрасывает доску в начальное состояние"""
        self.cells = [' ' for _ in range(9)]
    
    def is_cell_empty(self, position):
        """Проверяет, пуста ли клетка"""
        return self.cells[position] == ' '
    
    def place_marker(self, position, marker):
        """Устанавливает маркер в указанную позицию"""
        if 0 <= position < 9 and self.is_cell_empty(position):
            self.cells[position] = marker
            return True
        return False
    
    def get_empty_cells(self):
        """Возвращает список пустых клеток"""
        return [i for i, cell in enumerate(self.cells) if cell == ' ']
    
    def is_full(self):
        """Проверяет, заполнена ли доска"""
        return ' ' not in self.cells