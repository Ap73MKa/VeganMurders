from os import getenv


class Config:
    RESOLUTION = 1920, 1080
    FPS: int = 60
    DEBUG: bool = bool(getenv('DEBUG', ''))
