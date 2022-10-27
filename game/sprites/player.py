from typing import Any

import pygame as pg
from pygame.sprite import Sprite

from game import Config
from game.misc import load_image


class Player(Sprite):

    def __init__(self):
        super().__init__()
        self.image = load_image('player.png', alpha=True)
        self.image = pg.transform.scale(self.image, (150, 200))
        self.rect = self.image.get_rect(topleft=(350, 400))
        self.__pos = list(self.rect.topleft)

    def update(self, *args: Any, **kwargs: Any) -> None:
        delta = kwargs['delta']
        keys = pg.key.get_pressed()
        step = 100 * delta
        if keys[pg.K_RIGHT]:
            self.__pos[0] += step
        if keys[pg.K_LEFT]:
            self.__pos[0] -= step
        if keys[pg.K_UP]:
            self.__pos[1] -= step
        if keys[pg.K_DOWN]:
            self.__pos[1] += step

        self.rect.x = round(self.__pos[0])
        self.rect.y = round(self.__pos[1])
