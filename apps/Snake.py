from AppSettings import *
from utils.settingsSnake import *
from utils.ObjectsClasses import Fruit


def game_menu():  # Функция для отображения окна игры после нажатия кнопки Game
    pg.display.set_caption('Snake Game')

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
        sc.blit(bg_snake_game, rect_bg_snake_game)

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
