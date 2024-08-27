import os
import shutil

def copy_and_rename_images(source_folder, destination_folder, image_names_file):
    # Check if both source and destination folders exist
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return
    if not os.path.exists(destination_folder):
        print(f"Destination folder '{destination_folder}' does not exist.")
        return
    
    # Read image names from the text file
    with open(image_names_file, 'r') as file:
        image_names = file.read().splitlines()
    
    # Iterate through the image names array
    for index, image_name in enumerate(image_names, start=1):
        # Construct the full path of the source image with extension
        source_image_path_with_ext = os.path.join(source_folder, image_name)
        
        # Check if the image with extension exists in the source folder
        if not os.path.exists(source_image_path_with_ext+".jpg"):
            print(f"Image '{image_name}' not found in the source folder.")
            continue
        
        # Get the base filename (without extension)
        base_image_name, extension = os.path.splitext(image_name)
        extension = ".jpg"
        
        # Find the image with any extension in the source folder
        source_image_path = None
        for filename in os.listdir(source_folder):
            if os.path.splitext(filename)[0] == base_image_name:
                source_image_path = os.path.join(source_folder, filename)
                break
        
        # If no image with the given name found in source folder
        if source_image_path is None:
            print(f"Image '{image_name}' not found in the source folder.")
            continue
        
        # Construct the new name for the destination image
        new_name = f"gt_{index}_{base_image_name}{extension}"
        
        # Construct the full path of the destination image
        destination_image_path = os.path.join(destination_folder, new_name)
        
        # Copy the image from source to destination and rename
        shutil.copy(source_image_path, destination_image_path)
        print(f"Image '{image_name}' copied and renamed to '{new_name}'.")

# Example usage
source_folder = "./cvyc"
destination_folder = "./groundtruth"
image_names_file = "test1.txt"

copy_and_rename_images(source_folder, destination_folder, image_names_file)
