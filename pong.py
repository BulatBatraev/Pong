import pygame as pg
from sprites import Player


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
    all_sprites.add(player)

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
