from typing import Any

import pygame as pg
from pygame.sprite import Sprite

from game.misc import load_image


class Player(Sprite):

    def __init__(self):
        super().__init__()
        self.image = load_image('player.png', alpha=True)
        self.image = pg.transform.scale(self.image, (150, 200))
        self.rect = self.image.get_rect(topleft=(350, 400))

    def update(self, *args: Any, **kwargs: Any) -> None:
        step = 3
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.rect.x += step
        if keys[pg.K_LEFT]:
            self.rect.x -= step
        if keys[pg.K_UP]:
            self.rect.y -= step
        if keys[pg.K_DOWN]:
            self.rect.y += step