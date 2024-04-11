import os

def replace_substrings_in_files(substring_pairs, folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)
        for file_name in files:
            # Check if the file is a text file (ends with .txt)
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder_path, file_name)
                print(f"Replacing substrings in file: {file_path}")
                
                # Read the contents of the file
                with open(file_path, 'r') as file:
                    file_contents = file.read()

                # Perform the substring replacements
                modified_contents = file_contents
                for substring_pair in substring_pairs:
                    old_substring, new_substring = substring_pair
                    modified_contents = modified_contents.replace(old_substring, new_substring)

                # Write the modified contents back to the file
                with open(file_path, 'w') as file:
                    file.write(modified_contents)

                print("Substrings replaced successfully.")
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")

# Example usage:
substring_replacements = [("motor", "2_wheeler"), ("awning-tricycle", "3_wheeler"), ("tricycle", "3_wheeler"),("car", "cars"),("van", "cars"),("truck", "heavy_vehicle"),("bus", "heavy_vehicle")]
folder_to_search = "./labelTxt"  # Replace this with the path to your folder
replace_substrings_in_files(substring_replacements, folder_to_search)
