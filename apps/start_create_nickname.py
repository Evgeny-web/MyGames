from AppSettings import *
from utils.settings_start_create_nickname import *


def start_create_nickname():
    running = True
    result = (False, "Please enter your nickname!\n Use the English to display the name correctly")

    while running:
        sc.blit(bg_main_menu, rect_bg_main_menu)

        if not result[0]:
            draw_text(text=result[1], size_font=52, center_coordinats=(W / 2, 200),
                      color=WHITE_COLOR, screen=sc)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            if event.type == pg.USEREVENT and event.button == enter_btn:
                result = input_text_rect.save_text()

                if result[0] == True:
                    running = show_result_name(sc, result[1])

            enter_btn.handle_event(event)
            input_text_rect.handle_event(event, pg.mouse.get_pos())

        enter_btn.check_hover(pg.mouse.get_pos())
        for btn in array_btn_and_input:
            btn.draw(sc)

        pg.display.update()

        clock.tick(FPS)


def show_result_name(sc, result_text):
    running = True

    while running:
        sc.blit(bg_main_menu, rect_bg_main_menu)

        # Пишем полученный текст на поверхности
        draw_text(result_text, 72,
                  (W/2, 250), WHITE_COLOR, sc)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            if event.type == pg.USEREVENT and event.button == next_btn:
                return False

            next_btn.handle_event(event)

        next_btn.check_hover(pg.mouse.get_pos())
        next_btn.draw(sc)

        pg.display.update()

        clock.tick(FPS)