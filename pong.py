import pygame as pg
from sprites import Player
from sprites import Ball


def main():
    width = 800
    height = 600
    fps = 60
    pg.init()
    display = pg.display.set_mode((width, height))
    pg.display.set_caption("Pong")
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    player = Player(width, height)
    ball = Ball(width, height)
    all_sprites.add(player)
    all_sprites.add(ball)

    run = True
    while run:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        all_sprites.update()
        display.fill((255, 255, 255))
        all_sprites.draw(display)
        pg.display.flip()


if __name__ == "__main__":
    main()
    pg.quit()
