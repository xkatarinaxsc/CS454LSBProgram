from PIL import Image
import numpy as np
import pathlib


# Convert image to 24-bit BMP
def convert_to_bmp(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to 24-bit BMP format
        img = img.convert('RGB')

        # Save the converted BMP image
        img.save('../images/converted_image.bmp')


# Encryption Menu Option
def menu_option_1():
    print("Please input the secret message you want to encrypt: ")
    secret_message = input("Message: ")

    # does user pick img? via img path or name?
    convert_to_bmp('../images/image.jpeg')
    bin_msg = convert_string_to_binary(secret_message)
    image = Image.open("../images/converted_image.bmp")


    if size_check(image, bin_msg) == 1:
        print("What do you want to save the stego image as?")
        encoded_img_name = input(" : ")
        hide_secret_message(bin_msg, image, encoded_img_name)

    else:
        print("ERROR: Message too long, please try again")


# Decryption Menu Option
def menu_option_2():
    print("File name for the stego image you want to decrypt: ")
    file_name = input("File Name: ")


# LSB implementation to hide message within image
def hide_secret_message(bin_msg, bmp_img, encoded_img_name):

    # converts the bmp image into an array
    pixel_array = np.array(list(bmp_img.getdata()))
    width, height = bmp_img.size

    # file and user inputted name for stego image saving
    image_directory = "../images/" + encoded_img_name + ".jpeg"

    # loops through each column of each row of pixels within the image
    index = 0
    for w in range(width):
        for h in range(height):
            pixel = list(bmp_img.getpixel((w, h)))

            # Adjusts each R, G, B channel
            for RGB_channel in range(3):
                if index < len(bin_msg):
                    msg_bit = int(bin_msg[index])
                    # Finds the LSB by performing bitwise operation
                    pixel[RGB_channel] &= ~0x1
                    # Bitwise operation OR with 0x1 to change LSB 
                    pixel[RGB_channel] |= msg_bit

                    index += 1
                else:
                    break

        pixel_array = pixel_array.reshape((height, width, 3))
        enc_img = Image.fromarray(np.uint8(pixel_array))

        enc_img.save(image_directory)



        # Converts a text string into a binary string
def convert_string_to_binary(msg_text):
    binary_text = ''
    # Adding a delimiter
    msg_text += "$Hq73Op"

    for char in msg_text:
        binary_char = format(ord(char), '08b')
        binary_text += binary_char


    return binary_text


# Converts a binary string into a text string
def convert_binary_to_string(binary_msg):
    msg_text = ""
    for i in range(0, len(binary_msg), 8):
        temp_bin = binary_msg[i:i + 8]
        decimal_value = int(temp_bin, 2)
        msg_text = msg_text + chr(decimal_value)

    return msg_text


# Check the string will fit into the image
def size_check(bmp_img, bin_msg):
    width, height = bmp_img.size
    total_pixels = width * height

    req_pixels = len(bin_msg)

    if req_pixels < total_pixels:
        return 1
    else:
        return 0



if __name__ == "__main__":

    while True:
        print("\nMenu : ")
        print("1. Encrypt a secret message within an image")
        print("2. Decrypt an image with a secret message hidden in it")
        print("3. Exit Program")

        choice = input(" :  ")

        if choice == "1":
            menu_option_1()
        elif choice == "2":
            menu_option_2()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please input 1, 2 or 3")

