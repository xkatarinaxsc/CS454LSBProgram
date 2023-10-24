import unittest
from PIL import Image
from src import Main


class TestImageFormat(unittest.TestCase):

    def test_is_bmp(self):
        with Image.open('../images/converted_image.bmp') as img:  # Change the path to the location of your BMP image
            self.assertEqual(img.format, 'BMP')

class BinaryConversions(unittest.TestCase):

    def test_string_to_binary_1(self):
        msg_text = "Testing this method out!"
        expected_binary = '01010100011001010111001101110100011010010110111001100111001000000111010001101000011010010' \
                          '11100110010000001101101011001010111010001101000011011110110010000100000011011110111010101' \
                          '1101000010000100100100010010000111000100110111001100110100111101110000'
        self.assertEqual(Main.convert_string_to_binary(msg_text), expected_binary)

    def test_string_to_binary_2(self):
        msg_text = "The cat ran over the wall to chase the squirrel"
        expected_binary = '0101010001101000011001010010000001100011011000010111010000100000011100100110000101101110001' \
                          '0000001101111011101100110010101110010001000000111010001101000011001010010000001110111011000' \
                          '0101101100011011000010000001110100011011110010000001100011011010000110000101110011011001010' \
                          '0100000011101000110100001100101001000000111001101110001011101010110100101110010011100100110' \
                          '01010110110000100100010010000111000100110111001100110100111101110000'
        self.assertEqual(Main.convert_string_to_binary(msg_text), expected_binary)

    def test_string_to_binary_empty(self):
        msg_text = ""
        expected_binary = '00100100010010000111000100110111001100110100111101110000'
        self.assertEqual(Main.convert_string_to_binary(msg_text), expected_binary)

    def test_binary_to_string(self):
        binary_string = '0101010001101000011001010010000001100011011000010111010000100000011100100110000101101110001' \
                          '0000001101111011101100110010101110010001000000111010001101000011001010010000001110111011000' \
                          '0101101100011011000010000001110100011011110010000001100011011010000110000101110011011001010' \
                          '0100000011101000110100001100101001000000111001101110001011101010110100101110010011100100110' \
                          '01010110110000100100010010000111000100110111001100110100111101110000'
        expected_string = "The cat ran over the wall to chase the squirrel$Hq73Op"
        self.assertEqual(Main.convert_binary_to_string(binary_string), expected_string)

    def test_binary_to_string(self):
        binary_string = '01010100011001010111001101110100011010010110111001100111001000000111010001101000011010010' \
                          '11100110010000001101101011001010111010001101000011011110110010000100000011011110111010101' \
                          '1101000010000100100100010010000111000100110111001100110100111101110000'
        expected_string = "Testing this method out!$Hq73Op"
        self.assertEqual(Main.convert_binary_to_string(binary_string), expected_string)



if __name__ == '__main__':
    unittest.main()
