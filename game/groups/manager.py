from pygame._sprite import Group, AbstractGroup
import pygame as pg
from pygame.surface import Surface


class GroupManager:

    def __init__(self, *groups):
        self.__groups: list[AbstractGroup] = []
        self.add(*groups)

    def add(self, *groups) -> None:
        for group in groups:
            if isinstance(group, AbstractGroup):
                if group not in self.__groups:
                    self.__groups.append(group)
                continue
            try:
                self.add(*group)
            except (TypeError, AttributeError):
                raise ValueError(f"Group manager must contains pygame groups, not {type(group)}")

    def update(self, *args, **kwargs) -> None:
        for group in self.__groups:
            group.update(*args, **kwargs)

    def draw(self, surface: Surface) -> None:
        for group in self.__groups:
            group.draw(surface)
