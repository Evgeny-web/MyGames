import pygame as pg
import random

W, H = 1280, 720

# constant colors
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (255, 0, 0)
BLACK_COLOR = (0, 0, 0)
MAIN_MENU_COLOR = (125, 120, 140)
GROW_COLOR = (125, 125, 125)

# bg images
bg_main_menu = pg.image.load('images/bg_main_menu.jpg')
bg_main_menu = pg.transform.scale(bg_main_menu, (W, H))
rect_bg_main_menu = bg_main_menu.get_rect()

bg_settings_menu = pg.image.load('images/bg_settings.jpg')
bg_settings_menu = pg.transform.scale(bg_settings_menu, (W, H))
rect_bg_settings_menu = bg_settings_menu.get_rect()

# Create values for game
GAME_SCORE = 0
size_rect = 40
FPS = 60


def draw_text(text, size_font, center_coordinats, color, screen):
    font = pg.font.Font(None, size_font)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center_coordinats)
    screen.blit(text_surface, text_rect)


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
