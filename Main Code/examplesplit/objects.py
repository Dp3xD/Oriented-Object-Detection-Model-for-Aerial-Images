import os

def compare_substring_with_files(substring, folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)
        pedestrian = 0
        people = 0
        bicycle = 0
        cars = 0
        heavy_vehicle = 0
        wheeler3 = 0
        wheeler2 = 0
        c = 0
        for file_name in files:
            c+=1
            # Check if the file is a text file (ends with .txt)
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder_path, file_name)
                print(f"Checking file: {file_path}")
                # Open and read the file
                with open(file_path, 'r') as file:
                    for line in file:
                        # Remove trailing newline character
                        line = line.strip()
                        # Check if the substring exists in the line
                        if "2_wheeler" in line:
                            wheeler2+=1
                        elif "3_wheeler" in line:
                            wheeler3+=1
                        elif "cars" in line:
                            cars+=1
                        elif "pedestrian" in line:
                            pedestrian+=1
                        elif "people" in line:
                            people+=1
                        elif "heavy_vehicle" in line:
                            heavy_vehicle+=1
                        elif "bicycle" in line:
                            bicycle+=1
            print(c)
        print("pedestrian:",pedestrian)
        print("Cars:",cars)
        print("heavy_vehicle:",heavy_vehicle)
        print("3_wheeler:",wheeler3)
        print("bicycle:",bicycle)
        print("people:",people)
        print("2_wheeler:",wheeler3)
        print("Total:",people+cars+heavy_vehicle+wheeler3+wheeler2+bicycle+pedestrian)
        with open("objects1.txt", "w") as f:
            f.write(f"pedestrian:{pedestrian}\n")
            f.write(f"Car:{cars}\n")
            f.write(f"heavy_vehicle:{heavy_vehicle}\n")
            f.write(f"wheeler3:{wheeler3}\n")
            f.write(f"bicycle:{bicycle}\n")
            f.write(f"wheeler2:{wheeler2}\n")
            f.write(f"people:{people}\n")
            f.write(f"Total:{people+cars+heavy_vehicle+wheeler3+wheeler2+bicycle+pedestrian}\n")
            
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")

# Example usage:
substring_to_compare = "example"
folder_to_search = "./labelTxt"  # Replace this with the path to your folder
compare_substring_with_files(substring_to_compare, folder_to_search)