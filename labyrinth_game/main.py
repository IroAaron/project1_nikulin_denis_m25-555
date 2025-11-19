#!/usr/bin/env python3

from labyrinth_game import player_actions, utils

game_state = {
    'coins': 0, # Деньги игрока
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0 # Количество шагов
  }

def main():
    print("Добро пожаловать в Лабиринт сокровищ!\n")  
    utils.describe_current_room(game_state)
    
    while(True):
        print('')
        print("Выберите любое действие из доступных:")
        player_actions.show_available_actions()
        player_action = input('Ваше действие: ')
        print('')
        command = player_actions.get_input(game_state, player_action)

        if command == 'new_room':
           utils.describe_current_room(game_state)
           game_state['steps_taken'] += 1
           utils.random_event(game_state)

        if command == 'quit' or game_state['game_over']:
          print("Выход из игры.")
          break
