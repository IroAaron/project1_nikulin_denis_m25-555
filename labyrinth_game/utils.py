import math

from labyrinth_game.constants import (
    BIG_RANDOM_NUMS,
    MAX_DAMAGE_CHANCE,
    MAX_EVENT_CHANCE_NUM,
    ROOMS,
)


def pseudo_random(seed, modulo):
    final_num = math.sin(seed * BIG_RANDOM_NUMS[0]) * BIG_RANDOM_NUMS[1]
    final_num = round((final_num - math.floor(final_num)) * modulo)
    return final_num

def random_event(game_state):
    seed = game_state['steps_taken']
    event_chance = pseudo_random(seed, MAX_EVENT_CHANCE_NUM)  
    if event_chance > 0: 
        return

    event_type = pseudo_random(seed, 2)
    match event_type:
        case 0:
            coins = ROOMS[game_state['current_room']]['coins']
            print(f"Удача! Вы нашли {coins} монет")
            add_coins(game_state, coins)
        case 1:
            print("Вы слышите шорох")
            if 'sword' in game_state['player_inventory']:
                print("Кажется, вы отпугнули нечно, скрывающееся во тьме, своим мечом")
            else:
                attack_chance = pseudo_random(seed, MAX_EVENT_CHANCE_NUM)
                if attack_chance < MAX_DAMAGE_CHANCE:
                    print("Чудище напало на вас. Вам не было чем отбиться")
                    lose_message(game_state)
        case 2:
            current_room = game_state['current_room']
            inventory = game_state['player_inventory']

            if current_room == 'trap_room' and 'torch' not in inventory:
                print("Вы не заметили ловушку!")
                trigger_trap(game_state)


def describe_current_room(game_state):
    current_room_data = ROOMS[game_state['current_room']]
    print(f"== {game_state['current_room'].upper()} ==") 
    print(f"{current_room_data['description']}")
    if len(current_room_data['items']) > 0:
        print("Заметные предметы: ", end='')
        for i in range(0, len(current_room_data['items'])):
            print(f"{current_room_data['items'][i]}", end='')
            if i < len(current_room_data['items']) - 1:
                print(", ", end='')

        print('')
    if current_room_data['puzzle'] is not None: 
        print("Кажется, здесь есть загадка")

def change_room_desc_after_item_taken(room, item, game_state):
    match room:
        case 'entrance':
            if item == 'torch':
                ROOMS[room]['description'] = 'Вы в темном входе лабиринта. ' \
                'Стены покрыты мхом.'
        case 'library':
             if item == 'treasure_key':
                ROOMS[room]['description'] = 'Пыльная библиотека. ' \
                'На полках старые свитки.'
        case 'armory':
            if item == 'sword':
                if 'bronze_box' in ROOMS[room]['items']:
                    ROOMS[room]['description'] = 'Старая оружейная комната. ' \
                    'Рядом с местом, где висел меч — небольшая бронзовая шкатулка.'
                else:
                    ROOMS[room]['description'] = 'Старая оружейная комната.'
            if item == 'bronze_box':
                if 'sword' in ROOMS[room]['items']:
                    ROOMS[room]['description'] = 'Старая оружейная комната. ' \
                    'На стене висит меч.'
                else:
                    ROOMS[room]['description'] = 'Старая оружейная комната.'
        case 'hidden_chamber':
            if item == 'glowing_crystal':
                ROOMS[room]['description'] = 'Скрытая камера с алтарём в центре.'

def solve_puzzle(game_state):
    current_room_data = ROOMS[game_state['current_room']]
    if current_room_data['puzzle'] is None:
        print("Загадок здесь нет.")
        return
    print(current_room_data['puzzle']['text'])
    answer = input("Ваш ответ: ")

    print('')
    if answer in current_room_data['puzzle']['answers']:
        print("Загадка решена!")
        try_add_awards(game_state)
        current_room_data['puzzle'] = None
    else:
        if game_state['current_room'] == 'trap_room':
            trigger_trap(game_state)
        else:
            print("Неверно. Попробуйте снова")

def attempt_open_treasure(game_state):
    if 'treasure_key' in game_state['player_inventory']:
        print("Вы применяете ключ, и замок щелкает. Сундук открыт!")
        game_state['player_inventory'].remove('treasure_key')
        win_message(game_state)
    else:
        answer = input("Сундук заперт. ... Ввести код? (да/нет) ")
        if (answer.lower() == 'Да'.lower()):
            solve_puzzle(game_state)
            if ROOMS['treasure_room']['puzzle'] is None:
                print("Вы отгадали код! Сундук открыт!")
                win_message(game_state)
        elif (answer.lower() == 'Нет'.lower()):
            print("Вы отступаете от сундука.")
        else:
            print("Вы сами не знаете что хотите сделать. Вы отступаете от сундука.")

def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")
    player_inventory = game_state['player_inventory']
    seed = game_state['steps_taken']
    if len(player_inventory) > 0:
        item_to_remove_index = pseudo_random(seed, len(player_inventory))
        removed_item = player_inventory[item_to_remove_index]
        player_inventory.remove(removed_item)
        print(f"Попав в ловушку, вы потеряли предмет {removed_item}")
    else:
        damage_chance = pseudo_random(seed, MAX_EVENT_CHANCE_NUM)
        if damage_chance < MAX_DAMAGE_CHANCE:
            print("К сожалению, вы не уцелели после ловушки...")
            lose_message(game_state)
        else:
            print("На ваше счастье вы уцелели")

def add_coins(game_state, ammount):
    game_state['coins'] += ammount
    print(f"Текущее количество монет: {game_state['coins']}")

def try_add_awards(game_state):
    current_room_data = ROOMS[game_state['current_room']]
    awards = list(current_room_data['puzzle']['awards'].keys())
        
    if len(awards) > 0:
        for award in awards:
            match award:
                case 'coins':
                    coins = current_room_data['puzzle']['awards']['coins']
                    print(f"Найдено {coins} монет. В сумке: {game_state['coins']}")
                    add_coins(game_state, coins)
                case 'items':
                    items = current_room_data['puzzle']['awards']['items']
                    print("Вы нашли: ", end='')
                    for i in range(0, len(items)):
                        print(items[i], end='')
                        if i < len(items) - 1:
                            print(', ', end='')
                case _:
                    print('ОШИБКА НЕ ПОНЯТНАЯ НАГРАДА')
        
    print('')

def win_message(game_state):
    current_room_data = ROOMS[game_state['current_room']]

    current_room_data['items'].remove('treasure_chest')
    print("В сундуке сокровище! Вы победили!")
    game_state['game_over'] = True

def lose_message(game_state):
    print("Вы потерпели поражение. Повезет в следующий раз!")
    game_state['game_over'] = True
