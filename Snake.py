import sys
import time

from ObjectsClasses import imageButton, Fruit
from Sprites import SnakeHero
from settingsSnake import *

# важно вызвать до pygame.init()
pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

# Set window object and size
sc = pg.display.set_mode((W, H))
pg.display.set_caption('SnakeSnake')

# Расположение кнопок
x_pos_btn_for_main_menu = W / 2 - (252 / 2)
width_btn_main_menu, height_btn_main_menu = 252, 74

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


def create_snake_hero(size_rect, snake_images_path):  # функция для создания нашей головы змеи
    # необходимо сделать не прямоугольники, а словарь с изображением положения тела
    # Это будем объектом Surface, что потребует метода blit

    hero = SnakeHero(x=20 * size_rect, y=13 * size_rect, width=size_rect, height=size_rect,
                     direction=None, speed=size_rect, score=GAME_SCORE, images_path=snake_images_path)

    return hero


def game_menu():  # Функция для отображения окна игры после нажатия кнопки Game
    snake_hero = create_snake_hero(size_rect, snake_images_path)
    direct = 0

    # grid game lines
    grid = create_grid_lines()

    # random goal rect
    goal_rect = random_goal_rect(grid, snake_hero.coordinates_body_rects)

    # create Fruit
    apple = Fruit(goal_rect[0], goal_rect[1], goal_rect[2], goal_rect[3], grid, "images/Apple.png",
                  "sounds/eatApple.mp3")

    running = True
    while running:
        # чтобы наша змейка не убежала сразу за экран, необходимо замедлить работу игры
        time.sleep(0.4)
        sc.fill(GROW_COLOR)

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

        # Проверка на достижения цели. Съели мы фрукт или нет?
        apple.check_snake_hero(snake_hero, snake_hero.coordinates_body_rects)

        # Проверяем не врезались ли мы в края, если да, то выводим надпись и выходим
        if snake_hero.check_bounds_out(W, H):
            sc.fill(BLACK_COLOR)
            draw_text(text=f'GAME OVER!', size_font=72,
                      center_coordinats=(W // 2, H // 2 - 50), color=RED_COLOR, screen=sc)
            draw_text(text=f'Your score: {snake_hero.score}!', size_font=72,
                      center_coordinats=(W // 2, H // 2), color=RED_COLOR, screen=sc)
            pg.display.update()
            running = False
            time.sleep(4)

        # ПОсле всех проверок и обновлений, рисуем все изменения
        apple.draw(sc)
        # pg.draw.rect(sc, GREEN_COLOR, snake_hero.rect)
        snake_hero.draw(sc)

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

