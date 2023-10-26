# CS454LSBProgram
CS454 Group Project, an implementation of a simple image steganography 
program, allowing you to hide and extract a secret message within image files.

Git Hub Directory - https://github.com/xkatarinaxsc/CS454LSBProgram.git

Created: 15/10/2023

Authors: Katarina Scott, Alexander Quinn

#Installation
Firstly assuming you have already unzipped the file with this project in it,
move the project into your desired directory. From here open your terminal within Pycharm 
OR, if using command prompt, command line prompt (CMD) from the directory and change your 
working directory to the project's root folder. 

To run the project from the Git Bash terminal, navigate to the src folder and open git bash
then use the command "python main.py"


#User Guide 
The set up of the program is that whatever file in the images folder labeled, 
image.jpeg, this image will be used as the cover image for the program. You can 
alter this manually by replacing that image with a new one. 

When opening the program you will have a Main Menu, with three options, to encrypt an 
image, the decrypt an image and to exit the program. 

Menu Option 1 - User will be asked to type in a message to be encrypted into the image, this can 
be a few sentences long. Then the user will be asked to provide a name for the file. If the 
program successfully encrypts the bitmap image with the secret message it will pop out a success
message, if it does not and provides an error it either means there was an issue with 
finding the image or that the message was too long. 

Menu Option 2 - the user will be asked to provide a file name to decrypt (the user will need to
input the extension) if the user inputs the name incorrectly or the file doesnt exist, it will
take the user back to the main menu so they can either check it exists or so they can encrypt an image.

If the user provides an image path that exists, the program will decrypt the image and output 
the secret message to the user before returning to the main menu. 

Menu Option 3 - This exits the program 
