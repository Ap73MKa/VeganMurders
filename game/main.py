import pygame as pg
from pygame import display, event, time

from game import Config
from game.groups import DebugGroup, GroupManager
from game.misc.utils import Coord
from game.scenes.main import MainScene
from game.sprites.fps import FpsView


class Game:

    def __init__(self):
        self.__screen = display.set_mode((1280, 720))

        self.__delta = 0
        self.__game_over = False
        self.__clock = time.Clock()

        self.__all_groups = GroupManager(self.__load_groups())
        self.__scene = MainScene()

    # region Private

    def __load_groups(self):
        yield DebugGroup(
            FpsView(self.__clock, Coord(0, 0))
        )

    def __event(self) -> None:
        for e in event.get():
            self.__game_over = e.type == pg.QUIT

    def __draw(self) -> None:
        src = self.__scene.draw()
        self.__screen.blit(src, (0, 0))
        self.__all_groups.draw(self.__screen)
        display.flip()

    def __update(self):
        self.__scene.update(delta=self.__delta)
        self.__all_groups.update()

    # endregion

    # region Public

    def run(self) -> None:
        while not self.__game_over:
            self.__event()
            self.__update()
            self.__draw()
            self.__delta = self.__clock.tick_busy_loop(Config.FPS) / 1000
        pg.quit()

    # endregion
