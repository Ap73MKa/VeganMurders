from typing import Any

import pygame as pg
from pygame.sprite import Sprite
from game.misc import load_image
from game.misc.animator2 import SpriteSheetAnimator
from game.misc.sprite_sheet import advanced_sprite_slice


class Player(Sprite):

    def __init__(self):
        super().__init__()
        sprite = load_image('player1.png', alpha=True)
        sprite_sheet = advanced_sprite_slice(sprite, (4, 4), 0.5)
        self.animator = SpriteSheetAnimator(sprite_sheet)

        self.rect = self.animator.rect
        self.rect.topleft = (50, 50)
        self.__pos = list(self.rect.topleft)

    @property
    def image(self):
        return self.animator.image

    def update(self, *args: Any, **kwargs: Any) -> None:

        delta = kwargs['delta']
        keys = pg.key.get_pressed()
        step = 400 * delta
        if keys[pg.K_RIGHT] or keys[pg.K_LEFT]:
            if keys[pg.K_RIGHT]:
                self.__pos[0] += step
                self.animator.line = 3
            else:
                self.__pos[0] -= step
                self.animator.line = 2
        else:
            self.animator.reset()
        self.animator.update(*args, **kwargs)

        # if keys[pg.K_UP]:
        #     self.__pos[1] -= step
        # if keys[pg.K_DOWN]:
        #     self.__pos[1] += step

        self.rect.x = round(self.__pos[0])
        self.rect.y = round(self.__pos[1])
