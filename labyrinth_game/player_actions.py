from labyrinth_game import utils
from labyrinth_game.constants import COMMANDS, DIRECTIONS, HELP_SPACES, ROOMS

global_game_state = {}

def action_show_help(argue):
    for command in list(COMMANDS.keys()):
        print(''.ljust(HELP_SPACES, ' '), end='')
        print(f"'{command}' - {COMMANDS[command]}")

def action_show_inventory(argue):
    inventory = global_game_state['player_inventory']

    if len(inventory) > 0:
        print("Ваши предметы: ", end='')
        for i in range(0, len(inventory)):
            print(f"{inventory[i]}", end='')
            if i < len(inventory) - 1:
                print(", ", end='')
        print('')
    else:
        print("Инвентарь пуст")

def action_move_player(direction):
    if direction is None:
        print("Вы не выбрали вторым аргументом направление, куда хотите пойти")
        return  

    available_directions = ROOMS[global_game_state['current_room']]['exits']
    if direction in DIRECTIONS:
        if direction in available_directions:
            next_room = ROOMS[global_game_state['current_room']]['exits'][direction]
            if not ROOMS[next_room]['is_open']:
                if 'rusty_key' in global_game_state['player_inventory']:
                    ROOMS[next_room]['is_open'] = True
                    print(f"Вы использовали rusty_key и успешно открыли {next_room}")
                else:
                    print("Кажется, дверь в комнату заперта. Нужен ключ, чтобы войти")
                    print('')
                    return
            global_game_state['current_room'] = next_room
            return 'new_room'
        else:
            print("Нельзя пойти в этом направлении")
    else:
        print("Такого направления не существует")
    
def action_try_take_item(item):
    available_items = ROOMS[global_game_state['current_room']]['items']

    if len(available_items) == 0:
        print("В комнате нет предметов")
        return
    
    if 'treasure_chest' in available_items:
        print("Вы не можете поднять сундук. Он слишком тяжелый")
        return

    if item is None:
        print("Вы не выбрали вторым аргументом предмет, который хотите подобрать")
        return

    if item in available_items:
        action_take_item(item)
        available_items.remove(item)
        current_room = global_game_state['current_room']
        utils.change_room_desc_after_item_taken(current_room, item, global_game_state)
    else:
        print("Этого предмета в комнате нет")

def action_take_item(item):
    print(f"Вы подняли предмет {item}")
    global_game_state['player_inventory'].append(item)

def action_use_item(item):
    inventory = global_game_state['player_inventory']
    if item not in inventory:
        print(f"У вас нет в инвентаре предмета '{item}'")
        return

    match item:
        case 'torch':
            print("Стало светлее")
        case 'sword':
            print("Вы чувствуете себя увереннее")
        case 'bronze_box':
            if('rusty_key' in global_game_state['player_inventory']):
                print("Вы открываете шкатулку и там... Пусто")
            else:
                print("Вы нашли ржавый ключ!")
                action_take_item('rusty_key')
        case _:
            print("Без понятия, что с этим делать")

def action_describe_room(argue):
    utils.describe_current_room(global_game_state)

def action_try_solve_puzzle(argue):
    if global_game_state['current_room'] == 'treasure_room':
        utils.attempt_open_treasure(global_game_state)
        return
    
    utils.solve_puzzle(global_game_state)

def action_action_quit_game(argue):
    return 'quit'

available_actions = {
    'help' : action_show_help,
    'go' : action_move_player,
    'look' : action_describe_room,
    'take' : action_try_take_item,
    'use' : action_use_item,
    'inventory' : action_show_inventory,
    'solve' : action_try_solve_puzzle,
    'quit' : action_action_quit_game
}

def get_input(game_state, prompt="> "):
    global global_game_state
    global_game_state = game_state
    
    try:
        return try_activate_action(prompt)
    except (KeyboardInterrupt):
        print("\nВыход из игры.")
        return "quit"

def try_activate_action(action_name):
    if action_name == '':
        print("Вы не ввели команду")
        return

    action_name = action_name.split()

    if action_name[0] in DIRECTIONS:
        return available_actions['go'](action_name[0])
    
    if action_name[0] not in list(available_actions.keys()):
        print("Такой команды не существует")
        return
    
    if  len(action_name) > 1:
        return available_actions[action_name[0]](action_name[1])
    else:
        return available_actions[action_name[0]](None)

def show_available_actions():
    print_choices(list(available_actions.keys()))

def print_choices(choices):
    for i in range(0, len(choices)):
        print(choices[i], end='')
        if i < len(choices) - 1:
            print(" | ", end='')

    print('')