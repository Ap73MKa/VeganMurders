from typing import Any

import pygame as pg

from game.misc.utils import Coord
from game.text import Text


class FpsView(pg.sprite.Sprite):

    def __init__(self, clock, pos: Coord, size=35):
        super().__init__()
        self.__clock = clock
        self.text = Text('FPS: ', pos, size)

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.text.set_text(f'FPS: {int(self.__clock.get_fps())}')

    @property
    def image(self):
        return self.text.image

    @property
    def rect(self):
        return self.text.rect
