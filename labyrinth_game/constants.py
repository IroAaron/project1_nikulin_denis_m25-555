#labyrinth_game/constants.py


ROOMS = {
    'entrance': {
        'is_open' : True,
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None,
        'coins' : 1
    },
    'hall': {
        'is_open' : True,
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': {
            'text': 'На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.', 
            'answers': ['10', 'десять', 'ten'],
            'awards' : {'coins': 2}
            },
        'coins' : 1
    },
    'trap_room': {
        'is_open' : True,
        'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
        'exits': {'west': 'entrance'},
        'items': [],
        'puzzle': {
            'text': 'Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд', 
            'answers': ['шаг шаг шаг', 'шаг, шаг, шаг', 'step step step', 'step, step, step'],
            'awards' : {'coins': 1, 'items': ['rusty_key']}
            },
        'coins' : 1
    },
    'library': {
        'is_open' : True,
        'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
        'exits': {'east': 'hall', 'north': 'armory', 'west': 'secret_passage'},
        'items': ['ancient_book', 'treasure_key'],
        'puzzle': {
            'text': 'В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 
            'answers': ['резонанс', 'resonance'],
            'awards' : {'coins': 4, 'items': ['treasure_key']}
            },
        'coins' : 1
    },
    'armory': {
        'is_open' : True,
        'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
        'exits': {'south': 'library', 'north': 'garden'},
        'items': ['sword', 'bronze_box'],
        'puzzle': None,
        'coins' : 1
    },
    'treasure_room': {
        'is_open' : False,
        'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
        'exits': {'south': 'hall',},
        'items': ['treasure_chest'],
        'puzzle': {
            'text': 'Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага, 2*5= ?', 
            'answers': ['10', 'десять', 'ten'],
            'awards' : {'coins': 100, 'items': ['treasures']}
            },
        'coins' : 1
    },
    'secret_passage': {
        'is_open' : True,
        'description': 'Узкий тайный проход между стенами. В воздухе витает запах старой бумаги. В конце — деревянная дверь с замочной скважиной.',
        'exits': {'east': 'library', 'west': 'hidden_chamber'},
        'items': ['dust_covered_note'],
        'puzzle': {
            'text': 'На стене выцарапано: "Я не живое, но я расту; у меня нет лёгких, но мне нужен воздух; у меня нет рта, но вода меня убивает". Что я?', 
            'answers': ['огонь', 'fire'],
            'awards' : {'items': ['torch']}
            },
        'coins' : 1
    },
    'hidden_chamber': {
        'is_open' : True,
        'description': 'Скрытая камера с алтарём в центре. На алтаре лежит кристалл, излучающий тусклый свет.',
        'exits': {'east': 'secret_passage'},
        'items': ['ancient_seal'],
        'puzzle': {
            'text': 'Кристалл пульсирует и шепчет: "Назови число, равное сумме первых четырёх натуральных чисел"', 
            'answers': ['10', 'десять', 'ten'],
            'awards' : {'items': ['glowing_crystal']}
            },
        'puzzle': ('"', '10'),
        'coins' : 1
    },
    'garden': {
        'is_open' : True,
        'description': 'Заброшенный сад с высохшими растениями. В центре — каменный колодец с ржавой цепью.',
        'exits': {'south': 'armory', 'east': 'observatory'},
        'items': ['withered_flower', 'old_bucket'],
        'puzzle': {
            'text': 'На краю колодца надпись: "Что может заполнить комнату, но не занимает места?"', 
            'answers': ['свет', 'light'],
            'awards' : {'coins': 6,'items': ['torch']}
            },
        'coins' : 1
    },
    'observatory': {
        'is_open' : True,
        'description': 'Обсерватория с огромным телескопом. На стенах — карты звёздного неба. В углу стоит запертый ящик.',
        'exits': {'west': 'garden'},
        'items': ['star_chart'],
        'puzzle': {
            'text': 'На телескопе выгравировано: "Я вижу далёкое, но сам не двигаюсь. Что я?"', 
            'answers': ['телескоп', 'telescope'],
            'awards' : {'items': ['telescope_lens']}
            },
        'coins' : 1
    }
}

DIRECTIONS = ['north', 'south', 'east', 'west']

BIG_RANDOM_NUMS = [12.9898, 43758.5453]

COMMANDS = {
    'help': 'показать список команд и их описание',
    'go': 'перейти в направлении (выбрать направление: north/south/east/west)',
    'look': 'осмотреть комнату',
    'take': 'взять предмет (название пердмета)',
    'use': 'использвовать предмет (название предмета в инвентаре)',
    'inventory': 'посмотреть инвентарь игрока',
    'solve': 'попробовать решить головоломку в комнате',
    'quit': 'закончить игру'
}