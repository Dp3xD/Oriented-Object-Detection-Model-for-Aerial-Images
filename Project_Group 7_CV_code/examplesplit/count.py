import os

def compare_substring_with_files(substring, folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)
        c = 0
        c_0 = []
        c_1_5 = []
        c_6_10 = []
        c_11_15 = []
        c_16_20 = []
        c_21_25 = []
        c_26_30 = []
        c_31_35 = []
        c_36_40 = []
        c_41_45 = []
        c_46_50 = []
        nc_0 = 0
        nc_1_5 = 0
        nc_6_10 = 0
        nc_11_15 = 0
        nc_16_20 = 0
        nc_21_25 = 0
        nc_26_30 = 0
        nc_31_35 = 0
        nc_36_40 = 0
        nc_41_45 = 0
        nc_46_50 = 0
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
                    elif 31 <= s <= 35:
                        nc_31_35+=1
                        c_31_35.append(file_name)
                    elif 36 <= s <= 40:
                        nc_36_40+=1
                        c_36_40.append(file_name)
                    elif 41 <= s <= 45:
                        nc_41_45+=1
                        c_41_45.append(file_name)
                    elif 46 <= s <= 50:
                        nc_46_50+=1
                        c_46_50.append(file_name)
            print(c)
            print("frames with 0 objects:",nc_0)
            print(c_0)
            print("frames with 1-5 objects:",nc_1_5)
            print(c_1_5)
            print("frames with 6-10 objects:",nc_6_10)
            print(c_6_10)
            print("frames with 11-15 objects:",nc_11_15)
            print(c_11_15)
            print("frames with 16-20 objects:",nc_16_20)
            print(c_16_20)
            print("frames with 21-25 objects:",nc_21_25)
            print(c_21_25)
            print("frames with 26-30 objects:",nc_26_30)
            print(c_26_30)
            print("frames with 31-35 objects:",nc_31_35)
            print(c_31_35)
            print("frames with 36-40 objects:",nc_36_40)
            print(c_36_40)
            print("frames with 41-45 objects:",nc_41_45)
            print(c_41_45)
            print("frames with 46-50 objects:",nc_46_50)
            print(c_46_50)
            with open("frames.txt", "w") as f:
                f.write("frames with 0 objects:",nc_0)
                f.write(f"{c_0}")
                f.write("frames with 1-5 objects:",nc_1_5)
                f.write(f"{c_1_5}")
                f.write("frames with 6-10 objects:",nc_6_10)
                f.write(f"{c_6_10}")
                f.write("frames with 11-15 objects:",nc_11_15)
                f.write(f"{c_11_15}")
                f.write("frames with 16-20 objects:",nc_16_20)
                f.write(f"{c_16_20}")
                f.write("frames with 21-25 objects:",nc_21_25)
                f.write(f"{c_21_25}")
                f.write("frames with 26-30 objects:",nc_26_30)
                f.write(f"{c_26_30}")
                f.write("frames with 31-35 objects:",nc_31_35)
                f.write(f"{c_31_35}")
                f.write("frames with 36-40 objects:",nc_36_40)
                f.write(f"{c_36_40}")
                f.write("frames with 41-45 objects:",nc_41_45)
                f.write(f"{c_41_45}")
                f.write("frames with 46-50 objects:",nc_46_50)
                f.write(f"{c_46_50}")
                


            
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")

# Example usage:
substring_to_compare = "example"
folder_to_search = "./labelTxt"  # Replace this with the path to your folder
compare_substring_with_files(substring_to_compare, folder_to_search)