import json

from AppSettings import *
from utils.settingsSnake import random_goal_rect


class TextInput():
    def __init__(self, x: int, y: int, width: int, height: int, default_text: str, file_path: Path):
        self.rect = pg.Rect(x, y, width, height)
        self.text_color = BLACK_COLOR
        self.bg_color = WHITE_COLOR
        self.default_text = default_text
        self.text = ""
        self.font = pg.font.Font(None, SIZE_FONT_TEXT_INPUT)
        self.file_path = file_path
        self.active = False

    def check_active(self, mouse_pos):
        # если мышка в поле ввода, то наше поле активно
        if self.rect.collidepoint(mouse_pos):
            self.active = True
        else:
            self.active = False

    def handle_event(self, event, mouse_pos):
        # Если нажата мышь и кнопка 1, то активируем поле ввода по позиции мыши
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.check_active(mouse_pos)

        # если поле ввода активно, то можно менять текст
        if event.type == pg.KEYDOWN and self.active:
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def validate_input_text(self):
        if self.text == self.default_text or self.text == "":
            return False
        elif len(self.text) >= 30:
            return False
        elif not all(char.isalnum() or char.isspace() for char in self.text):
            return False

        return True

    def save_text(self):
        if not self.validate_input_text():
            return False, "Your nickname incorrect. Please enter again. \n You can use only letters and numbers!"
        else:
            result = {"nickname": self.text}
            with open(self.file_path, "w") as file:
                json.dump(result, file, sort_keys=True, indent=2)

            return True, f"Your nickname is {self.text}"

    def draw(self, screen):
        # отрисовка фона ввода
        pg.draw.rect(sc, self.bg_color, self.rect)

        # Определяем текст для отображения
        display_text = self.default_text if not self.active and self.text == "" else self.text

        # Отрисовка текста
        txt_surface = self.font.render(display_text, True, self.text_color)
        txt_rect = txt_surface.get_rect(center=self.rect.center)

        sc.blit(txt_surface, txt_rect)

        # Рисуем рамку при активации состояния
        if self.active:
            pg.draw.rect(sc, RED_COLOR, self.rect, 2)


class imageButton():
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pg.image.load(image_path).convert_alpha()
        self.image = pg.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pg.image.load(hover_image_path).convert_alpha()
            self.hover_image = pg.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.sound = None
        if sound_path:
            self.sound = pg.mixer.Sound(sound_path)

        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pg.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.rect.center))
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pg.event.post(pg.event.Event(pg.USEREVENT, button=self))


class Fruit():
    def __init__(self, x, y, width, height, grid, image_path, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.grid = grid

        self.image = pg.image.load(image_path).convert_alpha()
        self.image = pg.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect(topleft=(x, y))

        self.sound = None
        if sound_path:
            self.sound = pg.mixer.Sound(sound_path)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def check_snake_hero(self, snake_hero, coordinates_body_rects):
        if self.rect.contains(snake_hero.rect_head):
            snake_hero.eat_fruit()
            if self.sound:
                self.sound.play()

            new_rect = random_goal_rect(self.grid, coordinates_body_rects)
            self.rect.topleft = (new_rect[0], new_rect[1])
