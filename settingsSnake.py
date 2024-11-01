import pygame as pg

pg.init()

W, H = 1280, 720

# constant colors
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (255, 0, 0)
BLACK_COLOR = (0, 0, 0)
MAIN_MENU_COLOR = (125, 120, 140)

# Size buttons constant
size_button_main_menu = (100, 75)

# Flag constant for programm
FlagMainMenu = False

FPS = 60

# Create values for game
game_score = 0
speed = 40

# Create shrift and many buttons
# shrift
shrift = pg.font.SysFont('arial', 14)

# buttons
main_menu_play_button = shrift.render("PLAY", 1, RED_COLOR,
                                      GREEN_COLOR)  # кнопка игры. Пишем текст, ставим сглаживание(1), цвет шрифта, цвет фона
main_menu_quit_button = shrift.render("EXIT", 1, RED_COLOR, GREEN_COLOR)  # Кнопка выхода

# scale our buttons
main_menu_play_button = pg.transform.scale(main_menu_play_button, size_button_main_menu)
main_menu_quit_button = pg.transform.scale(main_menu_quit_button, size_button_main_menu)

# Text main menu
menu_text = shrift.render("MENU", 1, RED_COLOR, None)
menu_text = pg.transform.scale(menu_text, size_button_main_menu)


def draw_text(text, size_font, center_coordinats, color, screen):
    font = pg.font.Font(None, size_font)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center_coordinats)
    screen.blit(text_surface, text_rect)

#
# # button play in main menu
# play_button = pg.Surface(size_button_main_menu)
# pos_play_button = play_button.get_rect(topleft=(pos_main_menu.x + 100, pos_main_menu.y + 50))
# play_button.fill(GREEN_COLOR)
# print(f"pos main menu bottomleft: {pos_main_menu.bottomleft}")
#
# # button quit in main menu
# quit_button = pg.Surface(size_button_main_menu)
# pos_quit_button = quit_button.get_rect(bottomleft=(pos_main_menu.bottomleft[0] + 100, pos_main_menu.bottomleft[1] + 100))
# quit_button.fill(GREEN_COLOR)
