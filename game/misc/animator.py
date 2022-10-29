import pygame as pg
from pygame.sprite import Sprite


class Animator(Sprite):

    def __init__(self, images: list[pg.Surface], time_out: int = 125, repeat: bool = True):
        super().__init__()
        self.__time_out: int = time_out
        self.__repeat: bool = repeat
        self.images = images

        self.__animate_timer = 0
        self.current_index = 0
        self.__anim_finished = False
        self.__run = True

    # region Public

    @property
    def image(self) -> pg.Surface:
        return self.images[int(self.current_index)]

    @property
    def rect(self):
        return self.image.get_rect()

    @property
    def is_finished(self) -> bool:
        return self.__anim_finished

    def stop(self) -> None:
        self.__run = False

    def start(self) -> None:
        self.__run = True

    def reset(self) -> None:
        self.current_index = 0

    def update(self, *args, **kwargs) -> None:
        delta = 1
        if d := kwargs['delta']:
            delta = d
        if self.__run:
            self.current_index += 5.5 * delta
            self._image_swap()

    # endregion

    # region Private

    def _image_swap(self, *args, **kwargs) -> None:
        print(self.current_index)
        if int(self.current_index) == len(self.images) - 1 and not self.__repeat:
            self.stop()
            self.__anim_finished = True
            return
        self.current_index %= len(self.images)

    # endregion

