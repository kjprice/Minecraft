import unittest

import cv2
import numpy as np
from numpy.typing import ArrayLike

class ResizeImage():
    image = None

    def __init__(self, image: ArrayLike) -> None:
        self.image = image
    
    def by_ratio(self, resize_ratio: float):
        height, width, _ = self.image.shape
        new_dimensions = (
            int(height * resize_ratio),
            int(width * resize_ratio)
        )
        return self.resize(new_dimensions)
    
    def by_max_height(self, max_height: int):
        height, _, _ = self.image.shape

        return self.by_ratio(max_height / height)

    def resize(self, new_dimensions):
        # Use particular dimensions for cv2 to recognize
        reversed_new_dimensions = new_dimensions[::-1]
        resized_image = cv2.resize(self.image, reversed_new_dimensions, interpolation = cv2.INTER_AREA)

        return resized_image


class CommonImageToolsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.img_simple = np.zeros((100, 50, 3))
        self.img_full = np.zeros((1682, 3548, 3))
        return super().setUp()
    def test_resize_image_by_ratio(self):
        resized_image = ResizeImage(self.img_full).by_ratio(.05)
        self.assertEqual(resized_image.shape, (84,177,3))
    
    def test_resize_image_max_height(self):
        resized_image = ResizeImage(self.img_simple).by_max_height(50)
        self.assertEqual(resized_image.shape, (50, 25,3))
