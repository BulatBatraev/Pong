import pygame as pg


class Player(pg.sprite.Sprite):
    width = 30
    height = 100
    color = (0, 0, 150)
    speed_y = 5

    def __init__(self, display_width, display_height):
        super().__init__()
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width/8, display_height/2)
        self.display_width = display_width
        self.display_height = display_height

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s] and self.rect.y + self.rect.height <= self.display_height:
            self.rect.y += self.speed_y
        if keys[pg.K_w] and self.rect.y >= 0:
            self.rect.y += self.speed_y * -1


class Ball(pg.sprite.Sprite):
    width = 30
    height = 30
    color = (200, 0, 0)
    speed_x = 5
    speed_y = 5
    game_over = False

    def __init__(self, display_width, display_height):
        super().__init__()
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width/2, display_height/2)
        self.display_width = display_width
        self.display_height = display_height
        self.player = Player(self.display_width, self.display_height)

    def update(self, player_x, player_y):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x == 0 or self.rect.x + self.rect.width == self.display_width:
            self.speed_x *= -1
        if self.rect.y == 0 or self.rect.y + self.rect.height == self.display_height:
            self.speed_y *= -1
        if self.rect.x == player_x + self.player.rect.width and self.rect.y + self.rect.height > player_y\
                and self.rect.y < player_y + self.player.rect.height:
            self.speed_x *= -1
        if self.rect.x == 5:
            self.game_over = True


