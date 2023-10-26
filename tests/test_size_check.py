import unittest
from PIL import Image
import numpy as np
from src import Main


class TestSizeCheck(unittest.TestCase):
    def test_message_fits_in_image(self):
        width, height = 100, 100
        test_img = Image.new("RGB", (width, height))
        bin_msg = "01010101" * (width * height // 8)
        result = Main.size_check(test_img, bin_msg)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
