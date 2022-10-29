from pygame import transform
from pygame.surface import Surface


def sprite_slice(image, size: int, scale: int | float = 1):
    if size < 1:
        raise Exception
    frames = []
    res = image.get_width() / size
    for i in range(size):
        frame: Surface = image.subsurface((i * res, 0, res, image.get_height()))
        if scale != 1:
            tmp_size = frame.get_size()
            frame = transform.scale(frame, (tmp_size[0]*scale, tmp_size[1]*scale))
        frames.append(frame)
    return tuple(frames)


def advanced_sprite_slice(image, size: tuple[int, int], scale: int | float = 1):
    frames = []
    res = image.get_width() / size[0], image.get_height() / size[1]
    for i in range(size[0]):
        frame = image.subsurface((0, i * res[1], image.get_width(), res[1]))
        frames.append(sprite_slice(frame, size[0], scale))
    return tuple(frames)
