# CS454 Group Project

from PIL import Image
import numpy as np
import os


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

    try:
        image = Image.open("../images/converted_image.bmp")
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    if size_check(image, bin_msg) == 1:
        print("What do you want to save the stego image as?")
        encoded_img_name = input(" : ")
        hide_secret_message(bin_msg, image, encoded_img_name)
        print("Success! ")

    else:
        print("ERROR: Message too long, please try again")



# Decryption Menu Option
def menu_option_2():
    print("File name for the stego image you want to decrypt: ")
    file_name = input("File Name: ")

    # Building the path of the stego image
    stego_image_path = "../images/" + file_name

    if os.path.exists(stego_image_path):
        # Extracting the hidden message
        hidden_message = extract_encrypted_message(stego_image_path)
        print("The hidden message is:", hidden_message)
    else:
        print(f"ERROR: {file_name} does not exist in folder, check you have spelled the name correctly and the image is "
              f"saved within the folder")




# LSB implementation to hide message within image
def hide_secret_message(bin_msg, bmp_img, encoded_img_name):
    try:

        # converts the bmp image into an array
        # pixel_array = np.array(list(bmp_img.getdata()))
        width, height = bmp_img.size

        # file and user inputted name for stego image saving
        image_directory = "../images/" + encoded_img_name + ".bmp"

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

                bmp_img.putpixel((w, h), tuple(pixel))

        bmp_img.save(image_directory)

    except (IOError, KeyError) as e:
        print(f"Error saving the image: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Extract the hidden message
def extract_encrypted_message(stego_image_path):
    # Open the stego-image
    with Image.open(stego_image_path) as img:
        pixel_array = np.array(list(img.getdata()))
        width, height = img.size

        # Extract the LSBs of the pixel channels to get binary message
        binary_message = ''
        for w in range(width):
            for h in range(height):

                r, g, b = img.getpixel((w, h))
                binary_message += bin(r)[-1] + bin(g)[-1] + bin(b)[-1]

        # Convert the binary message to text
        hidden_message_including_delimiter = convert_binary_to_string(binary_message)

        # Extract the actual hidden message by removing the delimiter
        delimiter = "$Hq73Op"
        if delimiter in hidden_message_including_delimiter:
            hidden_message = hidden_message_including_delimiter.split(delimiter)[0]
            return hidden_message
        else:
            return "No hidden message found or the delimiter is missing."


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
    total_pixels = width * height * 3

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
            #test_method()
            menu_option_1()
        elif choice == "2":
            menu_option_2()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please input 1, 2 or 3")

