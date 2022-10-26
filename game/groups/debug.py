from typing import Any, List
from pygame._sprite import Group
from pygame.rect import Rect
from pygame.surface import Surface

from game import Config


class DebugGroup(Group):

    def update(self, *args: Any, **kwargs: Any) -> None:
        if Config.DEBUG:
            super().update(*args, **kwargs)

    def draw(self, surface: Surface) -> List[Rect]:
        if Config.DEBUG:
            return super().draw(surface)
        return []
