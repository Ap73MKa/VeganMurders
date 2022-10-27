import pygame as pg
from pygame import display, event, time

from game import Config
from game.groups import DebugGroup, GroupManager
from game.misc.utils import Coord
from game.scenes.main import MainScene
from game.sprites.fps import FpsView


class Game:

    def __init__(self):
        pg.init()
        self.screen = display.set_mode((1280, 720))
        self.__game_over = False
        self.delta = 0
        self.__clock = time.Clock()

        self.__all_groups = GroupManager(
            DebugGroup(
                FpsView(self.__clock, Coord(0, 0))
            )
        )
        self.scene = MainScene()

    def event(self) -> None:
        for e in event.get():
            self.__game_over = e.type == pg.QUIT

    def draw(self) -> None:
        self.screen.blit(self.scene.draw(), (0, 0))
        self.__all_groups.draw(self.screen)
        display.flip()

    def update(self):
        self.scene.update(delta=self.delta)
        self.__all_groups.update()

    def run(self) -> None:
        while not self.__game_over:
            self.event()
            self.update()
            self.draw()
            self.delta = self.__clock.tick_busy_loop(Config.FPS) / 1000
        pg.quit()
