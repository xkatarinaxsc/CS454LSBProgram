import unittest
from PIL import Image


class TestImageFormat(unittest.TestCase):

    def test_is_bmp(self):
        with Image.open('../images/converted_image.bmp') as img:  # Change the path to the location of your BMP image
            self.assertEqual(img.format, 'BMP')


if __name__ == '__main__':
    unittest.main()
