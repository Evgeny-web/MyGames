import sys
import time
from pathlib import Path
import pygame as pg
import random

# важно вызвать до pygame.init()
pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

W, H = 1280, 720

# Set window object and size
sc = pg.display.set_mode((W, H))

SIZE_FONT_TEXT_INPUT = 32

# constant colors
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (255, 0, 0)
BLACK_COLOR = (0, 0, 0)
MAIN_MENU_COLOR = (125, 120, 140)
GROW_COLOR = (125, 125, 125)

# Path for user data
user_data_path = Path("utils/db_data/user_data.json")

# Create values for game
GAME_SCORE = 0
FPS = 60

CAPTION_APP = "YEM_Application"

# fps window
clock = pg.time.Clock()


def draw_text(text: str, size_font: int, center_coordinats: tuple,
              color: tuple, screen: pg.display):
    """
    Функция для отображения текста на заданной поверхности с заданым размером шрифта,
    координатами текста и уветом.
    :param text: текст, который нужно написать
    :param size_font: Размер шрифта
    :param center_coordinats: Координаты текста
    :param color: Цвет текста
    :param screen: Поверхность отображения
    :return: nothing
    """
    font = pg.font.Font(None, size_font)

    # Разделим текст на строки и получим высоту строки
    lines = text.split("\n")
    line_height = font.get_height()

    # Выводим строки на поверхности поочередно
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(center_coordinats[0],
                                                  center_coordinats[1] + i * line_height))

        screen.blit(text_surface, text_rect)


def check_first_entry(user_data_path: Path, start_nickname_sc):
    """
    Функция для проверки первого запуска приложения.
    Если приложение запускается первый раз, то выполняется окно создания nickname
    :param user_data_path: Путь, где нужно будет сохранить json с никнеймом
    :param start_nickname_sc: Функция реализующая создание никнейма
    :return: nothing
    """

    if not user_data_path.exists():
        start_nickname_sc()
