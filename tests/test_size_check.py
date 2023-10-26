# CS454 Group Project
import unittest
from PIL import Image
import numpy as np
from src import Main


class TestSizeCheck(unittest.TestCase):

    def test_req_pixels(self):
        width, height = 100, 100
        test_img = Image.new("RGB", (width, height))
        bin_msg = "01010101"
        result = Main.size_check(test_img, bin_msg)
        self.assertEqual(result, 1)

    def test_no_req_pixels(self):
        width, height = 1, 1
        bmp_img = Image.new("RGB", (width, height))
        bin_msg = "0101010101010101010101"
        result = Main.size_check(bmp_img, bin_msg)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
