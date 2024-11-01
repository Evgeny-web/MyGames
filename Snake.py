import random
import sys

from ObjectsClasses import imageButton
from Sprites import Ball, Ball2v, SnakeHero
from settingsSnake import *

# pg.init()
# pg.time.set_timer(pg.USEREVENT, 2000)  # 2000 указываются в мс, т.е. 2с (таймер события)

# Set window object and size
sc = pg.display.set_mode((W, H))
pg.display.set_caption('SnakeSnake')

# Создание кнопок
x_pos_btn_for_main_menu = W / 2 - (252 / 2)
width_btn_main_menu, height_btn_main_menu = 252, 74

game_btn = imageButton(x_pos_btn_for_main_menu, 250, width_btn_main_menu,
                       height_btn_main_menu, 'Game', 'images/red_button.png',
                       'images/red_hover_button.png', 'sounds/click.mp3')

settings_btn = imageButton(x_pos_btn_for_main_menu, 350, width_btn_main_menu,
                           height_btn_main_menu, 'Settings', 'images/red_button.png',
                           'images/red_hover_button.png', 'sounds/click.mp3')

exit_btn = imageButton(x_pos_btn_for_main_menu, 450, width_btn_main_menu,
                       height_btn_main_menu, 'Exit', 'images/red_button.png',
                       'images/red_hover_button.png', 'sounds/click.mp3')

array_btn = [game_btn, settings_btn, exit_btn]

# fps window
clock = pg.time.Clock()


def draw_display_lines_for_snake():
    sc.fill(BLACK_COLOR)
    container_rects_background = []
    for x in range(0, W, speed):
        for j in range(0, H, speed):
            rec = pg.draw.rect(sc, BLUE_COLOR, (x, j, speed, speed), 1)
            container_rects_background.append(rec)

    return container_rects_background


def draw_main_menu_text():
    container_rects_background = draw_display_lines_for_snake()
    sc.blit(main_menu, pos_main_menu)
    sc.blit(main_menu_play_button, pos_main_menu_play_button)
    sc.blit(main_menu_quit_button, pos_main_menu_quit_button)
    sc.blit(menu_text, pos_menu_text)

    return container_rects_background


def random_position_snake():
    pass


def create_snake_hero(container_rects_bg):
    pass


# Create main menu for game with buttons: play, settings, quit
main_menu = pg.Surface((300, 450))
pos_main_menu = main_menu.get_rect(center=(W // 2, H // 2))

# add color our main menu
main_menu.fill(MAIN_MENU_COLOR)

# positions buttons
pos_main_menu_play_button = main_menu_play_button.get_rect(
    topleft=(pos_main_menu.x + 100, pos_main_menu.y + 100))
pos_main_menu_quit_button = main_menu_quit_button.get_rect(
    bottomleft=(pos_main_menu.bottomleft[0] + 100, pos_main_menu.bottomleft[1] - 100))

# position text menu
pos_menu_text = menu_text.get_rect(
    topleft=(pos_main_menu.x + 100, pos_main_menu.y + 25))


def main_menu():
    running = True
    while running:
        sc.fill(BLACK_COLOR)

        draw_text(text='Main Menu', size_font=72, center_coordinats=(W / 2, 150),
                  color=WHITE_COLOR, screen=sc)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            if event.type == pg.USEREVENT and event.button == game_btn:
                print(f"Enter first btn")
            if event.type == pg.USEREVENT and event.button == exit_btn:
                running = False
                pg.quit()
                sys.exit()

            for btn in array_btn:
                btn.handle_event(event)

        for btn in array_btn:
            btn.check_hover(pg.mouse.get_pos())
            btn.draw(sc)

        pg.display.update()

        clock.tick(FPS)


if __name__ == "__main__":
    main_menu()

'''
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                if FlagMainMenu:
                    FlagMainMenu = False
                else:
                    FlagMainMenu = True

    if FlagMainMenu == True:
        draw_main_menu_text()

        if pg.mouse.get_focused() and pos_main_menu_quit_button.collidepoint(pg.mouse.get_pos()):
            btns = pg.mouse.get_pressed()
            if btns[0]:  # нажата левая кнопка мыши
                exit()

        elif pg.mouse.get_focused() and pos_main_menu_play_button.collidepoint(pg.mouse.get_pos()):
            btns = pg.mouse.get_pressed()
            if btns[0]:
                FlagMainMenu = False

    else:

        container_rects_background = draw_display_lines_for_snake()



    pg.display.update()

    clock.tick(FPS)

'''
