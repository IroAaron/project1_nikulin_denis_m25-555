from .constants import ROOMS
from .constants import DIRECTIONS

from .utils import describe_current_room
from .utils import solve_puzzle
from .utils import attempt_open_treasure
from .utils import change_room_desc_after_item_taken

global_game_state = {}

def action_show_inventory(argue):
    inventory = global_game_state['player_inventory']
    print(f"Ваши предметы: {inventory}") if len(inventory) > 0 else print("Инвентарь пуст")

def action_move_player(direction):
    if direction is None:
        print("Вы не выбрали вторым аргументом направление, куда хотите пойти")
        return  

    available_directions = ROOMS[global_game_state['current_room']]['exits']
    if direction in DIRECTIONS:
        if direction in available_directions:
            global_game_state['current_room'] = ROOMS[global_game_state['current_room']]['exits'][direction]
            return 'new_room'
        else:
            print("Нельзя пойти в этом направлении")
    else:
        print("Такого направления не существует")
    
def try_take_item(item):
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
        take_item(item)
        available_items.remove(item)
        change_room_desc_after_item_taken(global_game_state['current_room'], item, global_game_state)
    else:
        print("Этого предмета в комнате нет")

def take_item(item):
    print(f"Вы подняли предмет {item}")
    global_game_state['player_inventory'].append(item)

def use_item(item):
    match item:
        case 'torch':
            print("Стало светлее")
        case 'sword':
            print("Вы чувствуете себя увереннее")
        case 'bronze box':
            if('rusty_key' in global_game_state['player_inventory']):
                print("Вы открываете шкатулку и там... Пусто")
            else:
                print("Вы нашли ржавый ключ!")
                take_item('rusty_key')
        case _:
            print("Без понятия, что с этим делать")

def describe_room(argue):
    describe_current_room(global_game_state)

def try_solve_puzzle(argue):
    if global_game_state['current_room'] == 'treasure_room':
        attempt_open_treasure(global_game_state)
        return
    
    solve_puzzle(global_game_state)

def action_quit_game(argue):
    return 'quit'

available_actions = {
    'go' : action_move_player,
    'look' : describe_room,
    'take' : try_take_item,
    'use' : use_item,
    'inventory' : action_show_inventory,
    'solve' : try_solve_puzzle,
    'quit' : action_quit_game
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
    action_name = action_name.split()
    
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