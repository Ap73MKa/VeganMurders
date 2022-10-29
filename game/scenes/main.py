from pygame._sprite import Group
from game.scenes.base import BaseScene
from game.sprites.enemy import Enemy
from game.sprites.player import Player


class MainScene(BaseScene):

    def _setup_objects(self) -> None:
        self.__player = Player()
        self.__enemy = Enemy()

        self.__player_group = Group(
            self.__player,
        )
        self.__enemy_group = Group(
            Enemy(),
        )

    def _load_groups(self):
        yield self.__player_group
        yield self.__enemy_group

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        pass
