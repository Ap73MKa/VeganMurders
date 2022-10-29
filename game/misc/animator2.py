import pygame as pg
from pygame.rect import Rect

from game.misc.animator import Animator


class SpriteSheetAnimator(Animator):

    def __init__(self, sheet, lines: int = 4, time_out: int = 125, repeat: bool = True):
        self.lines = lines
        if len(sheet) < self.lines:
            raise Exception
        self.__sheet = sheet
        self.__line_index = 0
        super().__init__(self.__sheet[0], time_out, repeat)

    def get_rect(self, **kwargs) -> Rect:
        return self.current_image.get_rect(**kwargs)

    @property
    def rotate(self) -> int:
        return self.__line_index

    @rotate.setter
    def rotate(self, value: int) -> None:
        if abs(value) > self.lines:
            raise Exception
        self.__line_index = abs(value)

    @property
    def current_image(self) -> pg.Surface:
        return self.__sheet[self.__line_index][self.current_index]
