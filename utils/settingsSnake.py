from AppSettings import *
from utils.Sprites import SnakeHero

size_rect = 40

# snake game
bg_snake_game = pg.image.load('images/bg_snake_game_1280x720.jpg')
bg_snake_game = pg.transform.scale(bg_snake_game, (W, H))
rect_bg_snake_game = bg_snake_game.get_rect()

# Словаь изображений змеи
snake_images_path = {'up': 'images/SnakeSprite/snake-head-up.png',
                     'down': 'images/SnakeSprite/snake-head-down.png',
                     'left': 'images/SnakeSprite/snake-head-left.png',
                     'right': 'images/SnakeSprite/snake-head-right.png',
                     'vertical': 'images/SnakeSprite/snake-body-vertical.png',
                     'horizontal': 'images/SnakeSprite/snake-body-horizontal.png',
                     'tail_up': 'images/SnakeSprite/snake-body-tail-up.png',
                     'tail_down': 'images/SnakeSprite/snake-body-tail-down.png',
                     'tail_left': 'images/SnakeSprite/snake-body-tail-left.png',
                     'tail_right': 'images/SnakeSprite/snake-body-tail-right.png',
                     'twist_upleft': 'images/SnakeSprite/snake-body-twist-upleft.png',
                     'twist_upright': 'images/SnakeSprite/snake-body-twist-upright.png',
                     'twist_downleft': 'images/SnakeSprite/snake-body-twist-downleft.png',
                     'twist_downright': 'images/SnakeSprite/snake-body-twist-downright.png'}


def create_snake_hero(size_rect, snake_images_path):  # функция для создания нашей головы змеи
    # необходимо сделать не прямоугольники, а словарь с изображением положения тела
    # Это будем объектом Surface, что потребует метода blit

    hero = SnakeHero(x=20 * size_rect, y=13 * size_rect, width=size_rect, height=size_rect,
                     direction=None, speed=size_rect, score=GAME_SCORE, images_path=snake_images_path)

    return hero


# lines for snake
def create_grid_lines():
    container_rects_background = {}
    for x in range(0, int(W // size_rect)):
        for j in range(0, int(H // size_rect)):
            container_rects_background[f'{x}_{j}'] = pg.Rect(x * size_rect, j * size_rect, size_rect, size_rect)

    return container_rects_background


# Надо будет дополнить, проверку на голову и тело змеи
def random_goal_rect(grid: dict, coordinates_body_rects: dict):
    # Получаем рандомное место для нового фрукта
    x_pos = random.randint(0, int(W // size_rect) - 1)
    y_pos = random.randint(0, int(H // size_rect) - 1)

    # сделаем список с координатами тела змеи
    body_rects = [rect for rect in coordinates_body_rects.values()]

    # создадим объект rect для сравнивания положения
    new_fruit = pg.Rect(x_pos * size_rect, y_pos * size_rect, size_rect, size_rect)

    # теперь подбираем место пока не окажемся в не занятом месте
    while new_fruit in body_rects:
        x_pos = random.randint(0, int(W // size_rect) - 1)
        y_pos = random.randint(0, int(H // size_rect) - 1)

        new_fruit = pg.Rect(x_pos * size_rect, y_pos * size_rect, size_rect, size_rect)

    # переменная с ключем для словаря сетки нашего игрового поля
    rect = f'{x_pos}_{y_pos}'

    # возвращаем объект pg.Rect
    return grid.get(rect)


def get_direct_snake_move(event):
    if event.key == pg.K_UP:
        return 'up'
    elif event.key == pg.K_DOWN:
        return 'down'
    elif event.key == pg.K_LEFT:
        return 'left'
    elif event.key == pg.K_RIGHT:
        return 'right'
