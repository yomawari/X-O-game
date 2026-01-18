class GameValidator:
    """Класс для проверки игровых условий"""
    
    @staticmethod
    def check_winner(board):
        """Проверяет, есть ли победитель на доске"""
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные
            [0, 4, 8], [2, 4, 6]              # Диагональные
        ]
        
        for combo in win_combinations:
            a, b, c = combo
            if (board.cells[a] != ' ' and 
                board.cells[a] == board.cells[b] == board.cells[c]):
                return board.cells[a]  # Возвращаем маркер победителя
        return None
    
    @staticmethod
    def is_game_over(board):
        """Проверяет, закончена ли игра"""
        return GameValidator.check_winner(board) is not None or board.is_full()
    
    @staticmethod
    def parse_input(input_str):
        """Парсит ввод пользователя в координаты"""
        try:
            if ' ' in input_str:
                row, col = input_str.split()
            elif len(input_str) == 2:
                row, col = input_str[0], input_str[1]
            else:
                return None
            
            row = int(row) - 1
            col = int(col) - 1
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row * 3 + col
        except (ValueError, IndexError):
            return None
        return None