from AppSettings import *


class SnakeHero(pg.sprite.Sprite):
    '''
    direction all body snake
    head: 'up', 'down', 'left', 'right'

    body: 'vertical', 'horizontal', 'twist_downleft', 'twist_downright', 'tiwst_upleft', 'twist_upright'

    tail: 'tail_up', 'tail_down', 'tail_left', 'tail_right',
    '''

    def __init__(self, x, y, width, height, direction, speed, score, images_path: dict):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.__direction = direction
        self.speed = speed
        self.score = score
        self.add_body = False

        self.__dict_direction = {'up': 1, 'down': 3, 'left': 2, 'right': 4}

        self.snake_images = {k: pg.transform.scale(pg.image.load(v).convert_alpha(), (width, height)) for k, v in
                             images_path.items()}
        # head snake
        self.head = self.snake_images['up']
        self.rect_head = self.head.get_rect(topleft=(x, y))
        print(f'rect head: {self.rect_head}')

        # tail snake
        self.tail = self.snake_images['tail_up']
        self.rect_tail = self.tail.get_rect(
            topleft=(self.rect_head.x, self.rect_head.y + 2 * self.height))

        self.body = [{'name': 'HEAD', 'image': self.head, 'coordinates': self.rect_head, 'direction': self.__direction},
                     {'name': 'element_0', 'image': self.snake_images['vertical'],
                      'coordinates': self.snake_images['vertical'].get_rect(
                          topleft=(self.rect_head.x, self.rect_head.y + self.height)),
                      'direction': 'vertical'},
                     {'name': 'TAIL', 'image': self.tail, 'coordinates': self.rect_tail, 'direction': 'tail_up'}]

        self.length_body = len(self.body)

        # словарь для будущих проверок координат тела змеи
        self.coordinates_body_rects = {i: element['coordinates'] for i, element in enumerate(self.body)}

    def eat_fruit(self) -> None:
        self.score += 1
        self.add_body = True

    def update(self, new_direction: str) -> None:
        if new_direction == 0:
            return

        if self.__direction == None:
            self.__direction = new_direction
        elif self.__direction != new_direction and \
                self.__dict_direction[new_direction] % 2 != self.__dict_direction[self.__direction] % 2:
            self.__direction = new_direction

        # создадим переменную для количества проходов цикла, до того, как прибавится новый элемент, чтобы его не считать
        len_body = self.length_body - 1

        # Если мы должны увеличиться, то скопируем еще не измененный блок тела, чтобы потом присвоить эти координаты
        if self.add_body:
            tmp_add_body = self.body[-2].copy()
            add_body_image = self.snake_images[f'{tmp_add_body["direction"]}']
            add_body_rect = add_body_image.get_rect(topleft=(int(tmp_add_body['coordinates'][0]),
                                                             int(tmp_add_body['coordinates'][1])))

            new_body_element = {'name': f'element_{self.score}',
                                'image': add_body_image,
                                'coordinates': add_body_rect,
                                'direction': tmp_add_body["direction"]}

            self.body.insert(-2, new_body_element)
            self.length_body += 1

        # update head first
        tmp = self.body[0]['coordinates'].copy()

        self.body[0]['image'] = self.snake_images[self.__direction]
        self.move_head(self.body[0]['coordinates'])

        # for tail
        direct_second = self.body[-2]['direction']

        for index in range(1, len_body):
            # get elements
            prev_element = self.body[index - 1]['coordinates'].copy()
            element = self.body[index]['coordinates'].copy()

            # если координаты изменятся, то элемент сдвинется
            parameters = self.move_body_snake(prev_element, tmp, element)

            # update current element
            self.body[index]['image'] = self.snake_images[parameters['direction']]
            self.body[index]['direction'] = parameters['direction']
            self.body[index]['coordinates'].move_ip(parameters['x'], parameters['y'])
            tmp = element

        if not self.add_body:
            # update tail snake
            element = self.body[-1]['coordinates'].copy()

            # если координаты изменятся, то и хвость сдвинется
            parameters = self.move_tail_snake(tmp, element, direct_second)

            self.body[-1]['image'] = self.snake_images[parameters['direction']]
            self.body[-1]['direction'] = parameters['direction']
            self.body[-1]['coordinates'].move_ip(parameters['x'], parameters['y'])
        else:
            self.add_body = False

        self.coordinates_body_rects = {i: element['coordinates'] for i, element in enumerate(self.body)}

    def move_head(self, rect) -> None:
        if self.__direction == 'up':
            rect.move_ip(0, -self.speed)
        elif self.__direction == 'down':
            rect.move_ip(0, self.speed)
        elif self.__direction == 'left':
            rect.move_ip(-self.speed, 0)
        elif self.__direction == 'right':
            rect.move_ip(self.speed, 0)

    def move_tail_snake(self, tmp: pg.Rect, element: pg.Rect, direct_second: str) -> dict:
        # return direct tail skane for image on screen
        # 'tail_up', 'tail_down', 'tail_left', 'tail_right',
        prev_tmp_0 = int(tmp[0]) - int(element[0])
        prev_tmp_1 = int(tmp[1]) - int(element[1])

        # Мы проверяем предыдущий элемент на смещение и куда он был направлен, в зависимости от этого выбираем направление хвоста
        # Если элемент был сверху, проверяем на поворот и вертикальность
        if prev_tmp_0 == 0 and prev_tmp_1 == -40:
            if direct_second == 'twist_downright':
                direct = 'tail_right'
            elif direct_second == 'twist_downleft':
                direct = 'tail_left'
            elif direct_second == 'vertical':
                direct = 'tail_up'
        # Если элемент был снизу, проверяем на поворот и вертикальность
        elif prev_tmp_0 == 0 and prev_tmp_1 == 40:
            if direct_second == 'twist_upright':
                direct = 'tail_right'
            elif direct_second == 'twist_upleft':
                direct = 'tail_left'
            elif direct_second == 'vertical':
                direct = 'tail_down'
        # Если элемент был слева, проверяем на поворот и горизонтальность
        elif prev_tmp_0 == -40 and prev_tmp_1 == 0:
            if direct_second == 'twist_upright':
                direct = 'tail_up'
            elif direct_second == 'twist_downright':
                direct = 'tail_down'
            elif direct_second == 'horizontal':
                direct = 'tail_left'
        # Если элемент был справа, проверяем на поворот и горизонтальность
        elif prev_tmp_0 == 40 and prev_tmp_1 == 0:
            if direct_second == 'twist_upleft':
                direct = 'tail_up'
            elif direct_second == 'twist_downleft':
                direct = 'tail_down'
            elif direct_second == 'horizontal':
                direct = 'tail_right'

        else:
            direct = 'tail_up'

        return {"direction": direct, "x": prev_tmp_0, "y": prev_tmp_1}

    def move_body_snake(self, prev_element: str, tmp: str, element: str) -> dict:
        prev_tmp_0 = int(tmp[0]) - int(prev_element[0])  # считаем x корд для головы, которая уже сместилась
        prev_tmp_1 = int(tmp[1]) - int(prev_element[1])  # считаем y корд для головы, которая уже сместилась

        next_tmp_0 = int(tmp[0]) - int(element[0])  # считаем x корд для текущего блока тела, которую нужно сместить
        next_tmp_1 = int(tmp[1]) - int(element[1])  # считаем y корд для текущего блока тела, которую нужно сместить

        # return direct image for body element
        # up-right Движение СПРАВА-ВВЕРХ и СВЕРХУ-ВПРАВО
        if (prev_tmp_0 == 0 and prev_tmp_1 == 40) and (next_tmp_0 == -40 and next_tmp_1 == 0):
            direct = 'twist_upright'
        elif (prev_tmp_0 == -40 and prev_tmp_1 == 0) and (next_tmp_0 == 0 and next_tmp_1 == 40):
            direct = 'twist_upright'

        # down-right Движение СНИЗУ-ВПРАВО и СПРАВА-ВНИЗ
        elif (prev_tmp_0 == 0 and prev_tmp_1 == -40) and (next_tmp_0 == -40 and next_tmp_1 == 0):
            direct = 'twist_downright'
        elif (prev_tmp_0 == -40 and prev_tmp_1 == 0) and (next_tmp_0 == 0 and next_tmp_1 == -40):
            direct = 'twist_downright'

        # up-left Движение СВЕРХУ-ВЛЕВО и СЛЕВА-ВВЕРХ
        elif (prev_tmp_0 == 0 and prev_tmp_1 == 40) and (next_tmp_0 == 40 and next_tmp_1 == 0):
            direct = 'twist_upleft'
        elif (prev_tmp_0 == 40 and prev_tmp_1 == 0) and (next_tmp_0 == 0 and next_tmp_1 == 40):
            direct = 'twist_upleft'

        # down-left Движение СНИЗУ-ВЛЕВО и СЛЕВА-ВНИЗ
        elif (prev_tmp_0 == 0 and prev_tmp_1 == -40) and (next_tmp_0 == 40 and next_tmp_1 == 0):
            direct = 'twist_downleft'
        elif (prev_tmp_0 == 40 and prev_tmp_1 == 0) and (next_tmp_0 == 0 and next_tmp_1 == -40):
            direct = 'twist_downleft'

        # horizontal
        elif ((prev_tmp_0 == -40 or prev_tmp_0 == 40) and prev_tmp_1 == 0) and (
                (next_tmp_0 == -40 or next_tmp_0 == 40) and next_tmp_1 == 0):
            direct = 'horizontal'

        # vertical
        elif (prev_tmp_0 == 0 and (prev_tmp_1 == -40 or prev_tmp_1 == 40)) and (
                next_tmp_0 == 0 and (next_tmp_1 == -40 or next_tmp_1 == 40)):
            direct = 'vertical'

        else:
            direct = 'vertical'

        return {"direction": direct, "x": next_tmp_0, "y": next_tmp_1}

    def check_bounds_out(self, W, H) -> None:
        # Если вышли за границы, то убиваем объект змеи и возвращаем истину на окончании игры
        if self.rect_head.x > W - self.speed or self.rect_head.x < 0 or self.rect_head.y > H - self.speed or self.rect_head.y < 0:
            self.kill()
            return True

        # Если пересекли тело головой, то возвращается истина, убиваем объект и заканчиваем.
        # Проверяем пересечение начиная с 3 элемента, потому что голова никогда не сможет пересечь следующий за ней блок
        elif self.rect_head.collidelist([element['coordinates'] for element in self.body[2:]]) != -1:
            self.kill()
            return True

        # Иначе продолжаем
        else:
            return False

    def draw(self, screen) -> None:
        for element_snake in self.body:
            screen.blit(element_snake['image'], element_snake['coordinates'].topleft)

