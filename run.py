import pygame as pg
from game import Game
from loguru import logger


def init():
    pg.init()
    pg.display.init()
    pg.font.init()
    pg.mixer.init()


def main():
    init()
    game = Game()

    logger.info('Game start')
    game.run()
    logger.info('Game stop')


if __name__ == '__main__':
    main()
