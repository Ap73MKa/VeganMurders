from os import path as pth
from typing import Final


class PathManager:
    ROOT: Final = pth.dirname(pth.dirname(pth.dirname(pth.abspath(__file__))))
    ASSET: Final = pth.join(ROOT, 'assets')
    IMAGE: Final = pth.join(ASSET, 'images')
    SOUND: Final = pth.join(ROOT, 'sounds')

    @classmethod
    def get(cls, path: str) -> str:
        return pth.join(cls.ROOT, path)

    @classmethod
    def get_asset(cls, path: str) -> str:
        return pth.join(cls.ASSET, path)

    @classmethod
    def get_image(cls, path: str) -> str:
        return pth.join(cls.IMAGE, path)

    @classmethod
    def get_sound(cls, path: str) -> str:
        return pth.join(cls.SOUND, path)