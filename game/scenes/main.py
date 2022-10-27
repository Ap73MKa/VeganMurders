from pygame._sprite import Group
from game.scenes.base import BaseScene
from game.sprites.enemy import Enemy
from game.sprites.player import Player


class MainScene(BaseScene):

    def _setup_objects(self) -> None:
        self.player = Player()
        self.enemy = Enemy()

        self.player_group = Group(
            Player(),

        )
        self.enemy_group = Group(
            Enemy(),
        )

    def _load_groups(self) -> None:
        yield self.player_group
        yield self.enemy_group

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
