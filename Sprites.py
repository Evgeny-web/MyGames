import pygame as pg


class SnakeHero(pg.sprite.Sprite):
    def __init__(self, x, y, rect, direction, speed, score):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.rect = rect
        self.direction = direction
        self.speed = speed
        self.score = score

    def update(self, new_direction):
        if new_direction == 0:
            return

        if self.direction != new_direction:
            self.direction = new_direction

        if self.direction == 'up':
            self.rect.move_ip(0, -self.speed)
        elif self.direction == 'down':
            self.rect.move_ip(0, self.speed)
        elif self.direction == 'left':
            self.rect.move_ip(-self.speed, 0)
        elif self.direction == 'right':
            self.rect.move_ip(self.speed, 0)

    def check_bounds_out(self):
        if self.rect.x > 1240 or self.rect.x < 0 or self.rect.y > 680 or self.rect.y < 0:
            return True
        else:
            return False


class SnakeBody(pg.sprite.Sprite):
    def __init__(self, x, y, rect, direction, speed, indx, group):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.rect = rect
        self.pos_rect = rect.get_rect()
        self.direction = direction
        self.speed = speed
        self.indx = indx
        self.group = group

    def update(self, ):
        if self.direction == 'up':
            self.x += 0
            self.y -= self.speed
        elif self.direction == 'down':
            self.x += 0
            self.y += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
            self.y += 0
        elif self.direction == 'right':
            self.x += self.speed
            self.y += 0


class Ball(pg.sprite.Sprite):
    def __init__(self, x, speed, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.rect.y = 0


class Ball2v(pg.sprite.Sprite):
    '''
    это 2 версия класса Ball, в которой реализованно добавление в группы
    создание многочисленных объектов со случайным x
    а также удаление при касании земли
    '''

    def __init__(self, x, speed, surf, score, group):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.score = score
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill()
