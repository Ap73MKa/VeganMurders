from typing import Any

import pygame as pg
from pygame.sprite import Sprite

from game.misc import load_image


class Enemy(Sprite):

    def __init__(self):
        super().__init__()
        self.image = load_image('enemy.png', alpha=True)
        self.image = pg.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect(topleft=(300, 300))