"""Core functions of ttak-pul."""

import numpy as np
from PIL import Image

def resize(path, width):
    """Resize an image to the given width, keeping its aspect ratio.

    Args:
        path (str): Path to the input image file.
        width (int): Target width in pixels. Must be positive.

    Returns:
        PIL.Image.Image: The resized image. The height is computed
        from the original aspect ratio.

    Raises:
        ValueError: If ``width`` is not a positive integer.

    Examples:
        >>> resize("examples/clock.png", 200).size
        (200, 100)
    """
    raise NotImplementedError


def crop(path, box):
    """Crop an image to a rectangle.

    Args:
        path (str): Path to the input image file.
        box (tuple[int, int, int, int]): (left, top, right, bottom) in pixels.

    Returns:
        PIL.Image.Image: The cropped image.

    Examples:
        >>> crop("examples/clock.png", (0, 0, 100, 100)).size
        (100, 100)
    """
    raise NotImplementedError


def grayscale(path, out):
    """Save a grayscale copy of an image. The original file is not changed.

    Args:
        path (str): Path to the input image file.
        out (str): Path of the new grayscale file. Must differ from ``path``.

    Returns:
        str: The path of the file that was written.

    Examples:
        >>> grayscale("examples/clock.png", "clock_gray.png")
        'clock_gray.png'
    """
    if out == path:
        raise ValueError("out must differ from path")
    Image.open(path).convert("L").save(out)
    return out

def mean_brightness(path):
    """Return the mean pixel brightness of an image, from 0.0 to 255.0.

    The image is converted to 8 bit grayscale first, so color images and
    grayscale images give comparable numbers. 0.0 means every pixel is
    black, 255.0 means every pixel is white.

    Args:
        path (str): Path to the input image file. Any format Pillow can
            open (PNG, JPEG, BMP, ...).

    Returns:
        float: Mean of all pixel values after the grayscale conversion.

    Raises:
        FileNotFoundError: If ``path`` does not exist.
        PIL.UnidentifiedImageError: If the file is not an image Pillow can read.

    Examples:
        >>> round(mean_brightness("examples/clock.png"), 1)
        127.5
    """
    pixels = np.asarray(Image.open(path).convert("L"), dtype=np.float64)
    return float(pixels.mean())
