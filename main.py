#!/usr/bin/env python3
"""
Точка входа в игру Крестики-нолики
"""

from Game.game_logic import TicTacToe

def main():
    """Основная функция игры"""
    print("="*40)
    print("    ИГРА В КРЕСТИКИ-НОЛИКИ")
    print("="*40)
    
    while True:
        game = TicTacToe()
        game.play()
        
        replay = input("\nХотите сыграть еще раз? (да/нет): ").lower()
        if replay not in ['да', 'д', 'yes', 'y', '']:
            print("\nСпасибо за игру! До свидания!")
            break
        print()

if __name__ == "__main__":
    main()