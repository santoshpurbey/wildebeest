from functools import partial
from typing import DefaultDict

import cv2 as cv
import numpy as np
from creevey import PathOrStr
from creevey.ops.image.image_transforms import convert_to_grayscale
from creevey.ops.helpers.report import report_output


def calculate_mean_brightness(image: np.array) -> float:
    """
    Calculate mean image brightness

    Brightness is calculated by converting to grayscale if necessary and
    then taking the mean pixel value. Assumes image is grayscale, RGB,
    or RGBA.
    """
    return convert_to_grayscale(image).mean()


def calculate_dhash(image: np.array, sqrt_hash_size: int = 8, **kwargs) -> np.array:
    """
    Calculate difference hash of image.

    As a rule of thumb, hashes from two images should typically have a
    Hamming distance less than 10 if and only if those images are
    "duplicates", with some robustness to sources of noise such as
    resizing and JPEG artifacts, where the Hamming distance between two
    hashes `a` and `b` is computed as follows.

    ```
    bin(int(a) ^ int(b)).count("1")
    ```

    Assumes image is grayscale, RGB, or RGBA.

    Source
    ------
    Adrian Rosebrock, "Building an Image Hashing Search Engine with
    VP-Trees and OpenCV", *PyImageSearch*,
    https://www.pyimagesearch.com/2019/08/26/building-an-image-hashing-search-engine-with-vp-trees-and-opencv/,
    accessed on 18 October 2019.

    Parameters
    ----------
    image
    sqrt_hash_size
        Side length of 2D array used to compute hash, so that hash will
        be up to `sqrt_hash_size`^2 bits long.
    """
    im_mod = convert_to_grayscale(image)
    im_mod = cv.resize(im_mod, (sqrt_hash_size + 1, sqrt_hash_size))
    diff = im_mod[:, 1:] > im_mod[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


report_dhash = partial(report_output, func=calculate_dhash, key='dhash')
