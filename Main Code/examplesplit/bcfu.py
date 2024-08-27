import os

def compare_substring_with_files(substring, folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)
        
        c_0 = []
        c_1_5 = []
        c_6_10 = []
        c_11_15 = []
        c_16_20 = []
        c_21_25 = []
        c_26_30 = []
        nc_0 = 0
        nc_1_5 = 0
        nc_6_10 = 0
        nc_11_15 = 0
        nc_16_20 = 0
        nc_21_25 = 0
        nc_26_30 = 0
        c = 0
        for file_name in files:
            c+=1
            # Check if the file is a text file (ends with .txt)
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder_path, file_name)
                print(f"Checking file: {file_path}")
                # Open and read the file
                with open(file_path, 'r') as file:
                    s = 0
                    for line in file:
                        s+=1
                        # Remove trailing newline character
                        line = line.strip()
                        # Check if the substring exists in the line
                    if s == 0:
                        nc_0+=1
                        c_0.append(file_name)
                    elif 1 <= s <= 5:
                        nc_1_5+=1
                        c_1_5.append(file_name)
                    elif 6 <= s <= 10:
                        nc_6_10+=1
                        c_6_10.append(file_name)
                    elif 11 <= s <= 15:
                        nc_11_15+=1
                        c_11_15.append(file_name)
                    elif 16 <= s <= 20:
                        nc_16_20+=1
                        c_16_20.append(file_name)
                    elif 21 <= s <= 25:
                        nc_21_25+=1
                        c_21_25.append(file_name)
                    elif 26 <= s <= 30:
                        nc_26_30+=1
                        c_26_30.append(file_name)
            print(c)
        print("frames with 0 objects:",nc_0)
        print("frames with 1-5 objects:",nc_1_5)
        print("frames with 6-10 objects:",nc_6_10)
        print("frames with 11-15 objects:",nc_11_15)
        print("frames with 16-20 objects:",nc_16_20)
        print("frames with 21-25 objects:",nc_21_25)
        print("frames with 26-30 objects:",nc_26_30)
        with open("frames1.txt", "w") as f:
            f.write(f"\nframes with 0 objects:{nc_0}\n")
            f.write(f"\nframes with 1-5 objects:{nc_1_5}\n")
            f.write(f"\nframes with 6-10 objects:{nc_6_10}\n")
            f.write(f"\nframes with 11-15 objects:{nc_11_15}\n")
            f.write(f"\nframes with 16-20 objects:{nc_16_20}\n")
            f.write(f"\nframes with 21-25 objects:{nc_21_25}\n")
            f.write(f"\nframes with 26-30 objects:{nc_26_30}\n")

            
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")

# Example usage:
substring_to_compare = "example"
folder_to_search = "./labelTxt"  # Replace this with the path to your folder
compare_substring_with_files(substring_to_compare, folder_to_search)