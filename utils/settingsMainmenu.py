from AppSettings import *
from utils.ObjectsClasses import *

# Расположение кнопок
x_pos_btn_for_main_menu = W / 2 - (252 / 2)
width_btn_main_menu, height_btn_main_menu = 252, 74

# bg images
# main menu
bg_main_menu = pg.image.load('images/bg_main_menu.jpg')
bg_main_menu = pg.transform.scale(bg_main_menu, (W, H))
rect_bg_main_menu = bg_main_menu.get_rect()

# settings menu
bg_settings_menu = pg.image.load('images/bg_settings.jpg')
bg_settings_menu = pg.transform.scale(bg_settings_menu, (W, H))
rect_bg_settings_menu = bg_settings_menu.get_rect()

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