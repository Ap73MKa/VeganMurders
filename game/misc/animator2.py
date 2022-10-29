import pygame as pg
from game.misc.animator import Animator


class SpriteSheetAnimator(Animator):

    def __init__(self, sheet, lines: int = 4, time_out: int = 125, repeat: bool = True):
        self.lines = lines
        if len(sheet) < self.lines:
            raise Exception
        self.__sheet = sheet
        self.__line_index = 0
        super().__init__(self.__sheet[0], time_out, repeat)

    @property
    def image(self) -> pg.Surface:
        return self.__sheet[self.__line_index][int(self.current_index)]

    @property
    def line(self) -> int:
        return self.__line_index

    @line.setter
    def line(self, value: int) -> None:
        if abs(value) > self.lines:
            raise Exception
        self.__line_index = abs(value)

    def reset(self) -> None:
        self.__line_index = 0
        super().reset()