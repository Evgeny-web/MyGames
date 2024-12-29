from AppSettings import *
from utils.ObjectsClasses import *

# Расположение кнопок
x_pos_enter_btn = W / 2 - 252 / 2
width_enter_btn, height_enter_btn = 252, 74

# bg images
bg_main_menu = pg.image.load('images/bg_main_menu.jpg')
bg_main_menu = pg.transform.scale(bg_main_menu, (W, H))
rect_bg_main_menu = bg_main_menu.get_rect()

# buttons for create nickname
enter_btn = imageButton(x_pos_enter_btn, 400, width_enter_btn,
                        height_enter_btn, 'Create', 'images/red_button.png',
                        'images/red_hover_button.png', 'sounds/click.mp3')

# exit_btn = imageButton(x_pos_enter_btn, 500, width_enter_btn,
#                        height_enter_btn, 'Exit', 'images/red_button.png',
#                        'images/red_hover_button.png', 'sounds/click.mp3')

input_text_rect = TextInput(x_pos_enter_btn, 300, width_enter_btn,
                            height_enter_btn, 'Enter nickname', user_data_path)

array_btn_and_input = [enter_btn, input_text_rect]


# НАСТРОЙКИ ДЛЯ SHOW_RESULT_NAME

# добавим фон поверхности
bg_create_nickname = pg.image.load('images/bg_create_nickname.jpg')
rect_bg_create_nickname = bg_create_nickname.get_rect()

next_btn = imageButton(x_pos_enter_btn, 400, width_enter_btn,
                       height_enter_btn, 'OK', 'images/red_button.png',
                       'images/red_hover_button.png', 'sounds/click.mp3')

