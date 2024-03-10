import pygame as pg
from sprites import Player
from sprites import Ball
import time


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
    font_name = pg.font.match_font('arial')

    def draw_text(surf, text, size, x, y):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, False, (0, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    run = True
    while run:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        if ball.game_over:
            draw_text(display, "GameOver", 60, width/4, height/2)
            time.sleep(3)
            run = False
        player.update()
        ball.update(player.rect.x, player.rect.y)
        display.fill((255, 255, 255))
        all_sprites.draw(display)
        pg.display.flip()


if __name__ == "__main__":
    main()
    pg.quit()
