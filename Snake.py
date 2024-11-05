import sys
import time

from ObjectsClasses import imageButton
from Sprites import Ball, Ball2v, SnakeHero
from settingsSnake import *

pg.init()
# pg.time.set_timer(pg.USEREVENT, 2000)  # 2000 указываются в мс, т.е. 2с (таймер события)

# Set window object and size
sc = pg.display.set_mode((W, H))
pg.display.set_caption('SnakeSnake')

# Создание кнопок
x_pos_btn_for_main_menu = W / 2 - (252 / 2)
width_btn_main_menu, height_btn_main_menu = 252, 74

# buttons for main menu
game_btn = imageButton(x_pos_btn_for_main_menu, 250, width_btn_main_menu,
                       height_btn_main_menu, 'Game', 'images/red_button.png',
                       'images/red_hover_button.png', 'sounds/click.mp3')

settings_btn = imageButton(x_pos_btn_for_main_menu, 350, width_btn_main_menu,
                           height_btn_main_menu, 'Settings', 'images/red_button.png',
                           'images/red_hover_button.png', 'sounds/click.mp3')

exit_btn = imageButton(x_pos_btn_for_main_menu, 450, width_btn_main_menu,
                       height_btn_main_menu, 'Exit', 'images/red_button.png',
                       'images/red_hover_button.png', 'sounds/click.mp3')

array_btn_main_menu = [game_btn, settings_btn, exit_btn]

# buttons for settings

grafics_btn = imageButton(x_pos_btn_for_main_menu, 250, width_btn_main_menu,
                          height_btn_main_menu, 'Grafics', 'images/red_button.png',
                          'images/red_hover_button.png', 'sounds/click.mp3')

control_btn = imageButton(x_pos_btn_for_main_menu, 350, width_btn_main_menu,
                          height_btn_main_menu, 'Control', 'images/red_button.png',
                          'images/red_hover_button.png', 'sounds/click.mp3')

back_btn = imageButton(x_pos_btn_for_main_menu, 450, width_btn_main_menu,
                       height_btn_main_menu, 'Back', 'images/red_button.png',
                       'images/red_hover_button.png', 'sounds/click.mp3')

array_btn_settings = [grafics_btn, control_btn, back_btn]

# fps window
clock = pg.time.Clock()


def create_snake_hero(size_rect):  # функция для создания нашей головы змеи
    snake_rect = pg.Rect(20 * size_rect, 13 * size_rect, size_rect, size_rect)

    hero = SnakeHero(snake_rect[0], snake_rect[1], snake_rect, None, size_rect, GAME_SCORE)

    return hero


def game_menu():  # Функция для отображения окна и игрой после нажатия кнопки Game
    snake_hero = create_snake_hero(size_rect)
    # grid game lines
    grid = create_grid_lines()
    # random goal rect
    goal_rect = random_goal_rect(grid)
    running = True
    direct = 0
    while running:
        # чтобы наша змейка не убежала сразу за экран, необходимо замедлить работу игры
        time.sleep(0.4)
        sc.fill(BLACK_COLOR)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            # Проверяем нажатие кнопки и задаем направление движения
            elif event.type == pg.KEYDOWN:
                direct = get_direct_snake_move(event)

        # Прежде чем все отрисовывать, обновляем данные sanke_hero.rect
        snake_hero.update(direct)
        # for pos, rec in grid.items():
        #     pg.draw.rect(sc, BLUE_COLOR, rec, 1)

        # Проверка на достижения цели. Съели мы фрукт или нет?
        if goal_rect.contains(snake_hero.rect):
            snake_hero.score += 1
            goal_rect = random_goal_rect(grid)


        # Проверяем не врезались ли мы в края, если да, то выводим надпись и выходим
        if snake_hero.check_bounds_out():
            sc.fill(BLACK_COLOR)
            draw_text(text=f'You lose. Exit from 2 seconds.', size_font=72,
                      center_coordinats=(W // 2, H // 2 - 50), color=RED_COLOR, screen=sc)
            draw_text(text=f'Your score: {snake_hero.score}!', size_font=72,
                      center_coordinats=(W // 2, H // 2), color=RED_COLOR, screen=sc)
            pg.display.update()
            running = False
            time.sleep(2)

        # ПОсле всех проверок и обновлений, рисуем все изменения
        pg.draw.rect(sc, RED_COLOR, goal_rect)
        pg.draw.rect(sc, GREEN_COLOR, snake_hero.rect)

        pg.display.update()

        clock.tick(FPS)


def settings_menu():
    running = True
    while running:
        sc.fill(BLACK_COLOR)
        sc.blit(bg_settings_menu, rect_bg_settings_menu)

        draw_text(text='Main Menu', size_font=72, center_coordinats=(W / 2, 150),
                  color=WHITE_COLOR, screen=sc)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            if event.type == pg.USEREVENT and event.button == back_btn:
                running = False

            for btn in array_btn_settings:
                btn.handle_event(event)

        for btn in array_btn_settings:
            btn.check_hover(pg.mouse.get_pos())
            btn.draw(sc)

        pg.display.update()

        clock.tick(FPS)


def main_menu():  # Главное меню нашего приложения
    running = True
    while running:
        sc.fill(BLACK_COLOR)
        sc.blit(bg_main_menu, (rect_bg_main_menu[0] * 1.2, rect_bg_main_menu[1] * 1.2))

        draw_text(text='Main Menu', size_font=72, center_coordinats=(W / 2, 150),
                  color=WHITE_COLOR, screen=sc)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            if event.type == pg.USEREVENT and event.button == game_btn:
                game_menu()

            if event.type == pg.USEREVENT and event.button == settings_btn:
                settings_menu()

            if event.type == pg.USEREVENT and event.button == exit_btn:
                running = False
                pg.quit()
                sys.exit()

            for btn in array_btn_main_menu:
                btn.handle_event(event)

        for btn in array_btn_main_menu:
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
