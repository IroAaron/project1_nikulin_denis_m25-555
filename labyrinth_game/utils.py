from .constants import ROOMS

def describe_current_room(game_state):
    current_room_data = ROOMS[game_state['current_room']]
    print('')
    print(f"== {game_state['current_room'].upper()} ==") 
    print(f"{current_room_data['description']}")
    if len(current_room_data['items']) > 0:  print(f"Заметные предметы: {current_room_data['items']}")
    print(current_room_data['exits'])
    if current_room_data['puzzle'] is not None: print("Кажется, здесь есть загадка")

def change_room_desc_after_item_taken(room, item, game_state):
    match room:
        case 'entrance':
            if item == 'torch':
                ROOMS[room]['description'] = 'Вы в темном входе лабиринта. Стены покрыты мхом.'
        case 'library':
             if item == 'treasure_key':
                ROOMS[room]['description'] = 'Пыльная библиотека. На полках старые свитки.'
        case 'armory':
            if item == 'sword':
                if 'bronze_box' in ROOMS[room]['items']:
                    ROOMS[room]['description'] = 'Старая оружейная комната. Рядом с местом, где висел меч — небольшая бронзовая шкатулка.'
                else:
                    ROOMS[room]['description'] = 'Старая оружейная комната.'
            if item == 'bronze_box':
                if 'sword' in ROOMS[room]['items']:
                    ROOMS[room]['description'] = 'Старая оружейная комната. На стене висит меч.'
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
    print(current_room_data['puzzle'][0])
    answer = input("Ваш ответ: ")

    if answer == current_room_data['puzzle'][1]:
        print("Загадка решена!")
        game_state['coins'] += 10
        print(f"Вы нашли 10 монет. Текущий счет: {game_state['coins']} монет")
        current_room_data['puzzle'] = None
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

def win_message(game_state):
    current_room_data = ROOMS[game_state['current_room']]

    current_room_data['items'].remove('treasure_chest')
    print("В сундуке сокровище! Вы победили!")
    game_state['game_over'] = True