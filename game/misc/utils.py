from dataclasses import dataclass

from pygame import image
from pygame.mixer import Sound
from pygame.surface import Surface

from game.misc.path import PathManager


def load_image(path: str, alpha: bool = False) -> Surface:
    img = image.load(PathManager.get_image(path))
    return img.convert() if not alpha else img.convert_alpha()


def load_sound(path: str) -> Sound:
    return Sound(PathManager.get_sound(path))


@dataclass
class Coord:
    x: int
    y: int

    def tuple(self) -> tuple[int, int]:
        return self.x, self.y
