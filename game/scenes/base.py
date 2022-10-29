from typing import Iterable

import pygame as pg
from pygame import time
from pygame._sprite import AbstractGroup
from pygame.surface import Surface

from game.groups import GroupManager
from game.settings import Config


class BaseScene:

    def __init__(self):
        self._screen = pg.Surface(Config.RESOLUTION)
        self._start_time = time.get_ticks() / 1000

        self._all_groups = GroupManager()

        self._setup_objects()

        if groups := self._load_groups():
            self._all_groups.add(*groups)

    # region Public

    @property
    def screen(self):
        return self._screen

    def update(self, *args, **kwargs):
        self._all_groups.update(*args, **kwargs)

    def draw(self) -> Surface:
        self._screen.fill('yellow')
        self._all_groups.draw(self._screen)
        return self._screen

    def on_enter(self) -> None:
        pass

    def on_exit(self) -> None:
        pass

    # endregion

    # region Private

    def _setup_objects(self) -> None:
        raise NotImplementedError

    def _load_groups(self) -> Iterable[AbstractGroup] | None:
        raise NotImplementedError

    # endregion
