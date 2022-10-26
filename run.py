from game import Game
from loguru import logger


def main():
    logger.info('Game start')
    game = Game()
    game.run()
    logger.info('Game stop')


if __name__ == '__main__':
    main()
