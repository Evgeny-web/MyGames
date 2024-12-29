import psycopg2.pool

from AppSettings import *
from utils.settingsMainmenu import *
from apps.Snake import game_menu


def settings_menu():
    """
    Функция отображения настроек приложения.
    Здесь будут реализовываться возможности изменения интерфейса.
    :return:
    """
    running = True
    while running:
        # sc.fill(BLACK_COLOR)
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


# Главное меню нашего приложения
def main_menu(connection_pool: psycopg2.pool.SimpleConnectionPool):
    """
    Главная исполняемая функция приложения.
    Отсюда идет вся логика приложения
    :param connection_pool: Пул соединений для БД
    """
    running = True
    # set display name
    pg.display.set_caption(CAPTION_APP)

    while running:
        # sc.fill(BLACK_COLOR)
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
