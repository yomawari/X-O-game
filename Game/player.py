class Player:
    """Класс для представления игрока"""
    
    def __init__(self, marker, name=None):
        self.marker = marker  # 'X' или 'O'
        self.name = name or f"Игрок {marker}"
        self.is_computer = False
    
    def __str__(self):
        return self.name
    
    def make_move(self, board):
        """Выполняет ход игрока"""
        pass  # Базовый класс, переопределяется в наследниках


class HumanPlayer(Player):
    """Класс для игрока-человека"""
    
    def make_move(self, board):
        """Запрашивает ход у пользователя"""
        while True:
            try:
                move = input("Введите ряд и столбец (1-3) или 'выход': ").strip()
                
                if move.lower() in ['выход', 'exit', 'quit']:
                    return None
                
                if ' ' in move:
                    row, col = move.split()
                elif len(move) == 2:
                    row, col = move[0], move[1]
                else:
                    raise ValueError
                
                row = int(row) - 1
                col = int(col) - 1
                
                if 0 <= row <= 2 and 0 <= col <= 2:
                    position = row * 3 + col
                    if board.is_cell_empty(position):
                        return position
                    else:
                        print("Эта клетка уже занята! Попробуйте снова.")
                else:
                    print("Пожалуйста, введите числа от 1 до 3.")
                    
            except (ValueError, IndexError):
                print("Неверный ввод! Используйте формат: ряд столбец (например: 2 3)")