from PIL import Image
import numpy as np


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
    convert_to_bmp('../images/image.jpeg')

#    binary_text = convert_string_to_binary(secret_message)
#    print(binary_text)
#    decrypt_msg = convert_binary_to_string(binary_text)
#   print(decrypt_msg)


# Decryption Menu Option
def menu_option_2():
    print("File name for the image you want to decrypt: ")
    file_name = input("File Name: ")



def hide_secret_message(bin_msg, bmp_img, encrypted_img_name):
    pixel_array = np.array(list(bmp_img.getdata()))
    total_pixels = pixel_array.size//3










# Converts a text string into a binary string
def convert_string_to_binary(msg_text):
    binary_text = ''
    for char in msg_text:
        binary_char = format(ord(char), '08b')
        binary_text += binary_char

    # Adding a delimiter
    binary_text += "$Hq73Op"

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

