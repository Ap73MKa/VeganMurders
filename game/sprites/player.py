from typing import Any

import pygame as pg
from pygame.sprite import Sprite

from game import Config
from game.misc import load_image
from game.misc.animator2 import SpriteSheetAnimator
from game.misc.sprite_sheet import advanced_sprite_slice


class Player(Sprite):

    def __init__(self):
        super().__init__()
        sprite = load_image('player1.png', alpha=True)
        self.sprite_sheet = advanced_sprite_slice(sprite, (4, 4), 0.5)
        self.animator = SpriteSheetAnimator(self.sprite_sheet)
        self.rect = self.animator.get_rect(topleft=(350, 400))
        self.__pos = list(self.rect.topleft)

    @property
    def image(self):
        return self.animator.current_image

    def update(self, *args: Any, **kwargs: Any) -> None:
        delta = kwargs['delta']
        keys = pg.key.get_pressed()
        step = 100 * delta
        if keys[pg.K_RIGHT]:
            self.__pos[0] += step
        if keys[pg.K_LEFT]:
            self.__pos[0] -= step
        # if keys[pg.K_UP]:
        #     self.__pos[1] -= step
        # if keys[pg.K_DOWN]:
        #     self.__pos[1] += step

        self.rect.x = round(self.__pos[0])
        self.rect.y = round(self.__pos[1])
