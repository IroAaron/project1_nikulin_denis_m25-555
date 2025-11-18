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
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.', '10'),
        'coins' : 2
    },
    'trap_room': {
        'is_open' : True,
        'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
        'exits': {'west': 'entrance'},
        'items': ['rusty_key'],
        'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг'),
        'coins' : 3
    },
    'library': {
        'is_open' : True,
        'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
        'exits': {'east': 'hall', 'north': 'armory', 'west': 'secret_passage'},
        'items': ['ancient_book', 'treasure_key'],
        'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'резонанс'),
        'coins' : 4
    },
    'armory': {
        'is_open' : True,
        'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
        'exits': {'south': 'library', 'north': 'garden'},
        'items': ['sword', 'bronze_box'],
        'puzzle': None,
        'coins' : 5
    },
    'treasure_room': {
        'is_open' : False,
        'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
        'exits': {'south': 'hall',},
        'items': ['treasure_chest'],
        'puzzle': ('Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага, 2*5= ? )', '10'),
        'coins' : 6  
    },
    'secret_passage': {
        'is_open' : True,
        'description': 'Узкий тайный проход между стенами. В воздухе витает запах старой бумаги. В конце — деревянная дверь с замочной скважиной.',
        'exits': {'east': 'library', 'west': 'hidden_chamber'},
        'items': ['dust_covered_note'],
        'puzzle': ('На стене выцарапано: "Я не живое, но я расту; у меня нет лёгких, но мне нужен воздух; у меня нет рта, но вода меня убивает". Что я?', 'огонь'),
        'coins' : 7
    },
    'hidden_chamber': {
        'is_open' : True,
        'description': 'Скрытая камера с алтарём в центре. На алтаре лежит кристалл, излучающий тусклый свет.',
        'exits': {'east': 'secret_passage'},
        'items': ['glowing_crystal', 'ancient_seal'],
        'puzzle': ('Кристалл пульсирует и шепчет: "Назови число, равное сумме первых четырёх натуральных чисел"', '10'),
        'coins' : 8
    },
    'garden': {
        'is_open' : True,
        'description': 'Заброшенный сад с высохшими растениями. В центре — каменный колодец с ржавой цепью.',
        'exits': {'south': 'armory', 'east': 'observatory'},
        'items': ['withered_flower', 'old_bucket'],
        'puzzle': ('На краю колодца надпись: "Что может заполнить комнату, но не занимает места?"', 'свет'),
        'coins' : 9
    },
    'observatory': {
        'is_open' : True,
        'description': 'Обсерватория с огромным телескопом. На стенах — карты звёздного неба. В углу стоит запертый ящик.',
        'exits': {'west': 'garden'},
        'items': ['star_chart', 'telescope_lens'],
        'puzzle': ('На телескопе выгравировано: "Я вижу далёкое, но сам не двигаюсь. Что я?"', 'телескоп'),
        'coins' : 10
    }
}

DIRECTIONS = ['north', 'south', 'east', 'west']

BIG_RANDOM_NUMS = [12.9898, 43758.5453]
