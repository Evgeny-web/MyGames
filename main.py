import pygame as pg

FPS = 60

W, H = 980, 620

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

if __name__ == "__main__":
    pg.init()

    sc = pg.display.set_mode((W, H), pg.RESIZABLE)  # создаем окно нашего приложения
    pg.display.set_caption("My first programm!")  # Задаем окну название, которое мы будем видеть

    # pg.display.set_icon(pg.image.load("{Path}")) # format .bmp Также можно поменять иконку рядом с названием

    clock = pg.time.Clock()

    x = W // 2
    y = H // 2
    # speed = 5
    #
    # move_x = 0
    # move_y = 0

    sp = None

    sc.fill(WHITE)
    pg.display.update()

    pg.mouse.set_visible(False)

    flRunning = True

    while flRunning:
        # получаем события взаимодействия и прописываем для них порядок действий
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit() # завершает полностью программу
                # pg.quit()  # завершает pygame
                # flRunning = False

        sc.fill(WHITE)

        pos = pg.mouse.get_pos()
        if pg.mouse.get_focused():
            pg.draw.circle(sc, BLUE, pos, 3)

        pressed = pg.mouse.get_pressed() # получаем кортеж индексов нажатых кнопок (1, 0, 0) (левая, центр, правая)
        if pressed[0]:
            if sp is None:
                sp = pos

            width = pos[0] - sp[0]
            height = pos[1] - sp[1]

            sc.fill(WHITE)
            pg.draw.rect(sc, RED, (sp[0], sp[1], width, height))

        else:
            sp = None

        pg.display.update()

        clock.tick(FPS)  # 60 fps all time
