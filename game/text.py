from pygame.sprite import DirtySprite
from pygame.font import Font, SysFont
from pygame.surface import Surface

from game.misc.utils import Coord


class Text(DirtySprite):

    def __init__(self, text: str, pos: Coord, size: int = 35,
                 color='white',
                 font: str = None,
                 antialias: bool = True, background=None):
        super().__init__()

        try:
            self._font = Font(font, size)
        except FileNotFoundError:
            self._font = SysFont(font, size)

        self._antialias = antialias
        self._color = color
        self._background = background

        self.image = self.__create_text(text)
        self.rect = self.image.get_rect()

        self.rect.topleft = pos.tuple()

    def set_pos(self, pos):
        self.rect = pos.get(self.rect)

    def set_text(self, text: str) -> None:
        self.image = self.__create_text(text)
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        self.dirty = 1

    def __create_text(self, text: str) -> Surface:
        if not self._background:
            return self._font.render(text, self._antialias, self._color).convert_alpha()
        self.dirty = 1
        return self._font.render(text, self._antialias, self._color, self._background).convert()
