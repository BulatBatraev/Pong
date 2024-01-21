import pygame as pg


class Player(pg.sprite.Sprite):
    width = 30
    height = 100
    color = (0, 0, 150)
    speed_y = 5

    def __init__(self, center_x, center_y, display_width, display_height):
        super().__init__()
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.center = (center_x, center_y)
        self.display_width = display_width
        self.display_height = display_height


    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s]:

