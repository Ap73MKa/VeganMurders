from os import getenv
from typing import Final


class Config:
    FPS: Final = 60
    RESOLUTION: Final = 1920, 1080
    DEBUG: Final = bool(getenv('DEBUG', ''))