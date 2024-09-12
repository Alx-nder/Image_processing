# A code to determine if an image is taken with an infrared camera or a regular camera.
import cv2
import os

path_to_folder=input("Enter the path to the folder containing the images: ")
path_to_folder=path_to_folder.replace("\\","/")
path_to_folder=path_to_folder+"\\\\"

# List all files in the given path
files = [f for f in os.listdir(path_to_folder) if os.path.isfile(os.path.join(path_to_folder, f))]

# Read each image file
for file in files:
    image = cv2.imread(os.path.join(path_to_folder, file))

    # validation by standard error
    if image[0].std(axis=1).std() == image[1].std(axis=1).std() ==image[2].std(axis=1).std():
        print(f"Image: {file} --- Night")
        input("Press any key to continue...")

    else:
        print(f"Image: {file} --- Day")
        input("Press any key to continue...")