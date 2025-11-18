#!/usr/bin/env python3

from .utils import describe_current_room

from .player_actions import show_available_actions
from .player_actions import get_input

game_state = {
    'coins': 0, # Деньги игрока
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0 # Количество шагов
  }

def main():
    print("Добро пожаловать в Лабиринт сокровищ!\n")
    describe_current_room(game_state)
    
    while(True):
        print('')
        print("Выберите любое действие из доступных:")
        show_available_actions()
        player_action = input('Ваше действие: ')
        command = get_input(game_state, player_action)

        if command == 'new_room':
           print('')
           describe_current_room(game_state)
           game_state['steps_taken'] += 1

        if command == 'quit' or game_state['game_over']:
          print("\nВыход из игры.")
          break
