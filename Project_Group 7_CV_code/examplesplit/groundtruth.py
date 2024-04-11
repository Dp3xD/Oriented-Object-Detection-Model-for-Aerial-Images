import cv2
import os
import numpy as np

# Function to draw ground truth on the image
def draw_ground_truth(image, ground_truth):
    # Convert image to BGR format
    image_with_gt = image.copy()
    
    # Draw ground truth on the image
    for i in range(0, len(ground_truth), 10):
        points = [(float(ground_truth[i+j]), float(ground_truth[i+j+1])) for j in range(0, 8, 2)]
        class_name = ground_truth[i+8]
        color = (0, 255, 0)  # Default color for bounding boxes
        if class_name == '2_wheeler':
            color = (0, 0, 255)  # Red color for cars
        elif class_name == '3_wheeler':
            color = (255, 0, 0)   # Red color for cars
        elif class_name == 'pedestrian':
            color = (255, 255, 0)   # Red color for cars
        elif class_name == 'heavy_vehicle':
            color = (255, 0, 255)   # Red color for cars
        elif class_name == 'cars':
            color = (0, 255, 255)   # Red color for cars
        elif class_name == 'people':
            color = (255, 255, 255)   # Red color for cars
        elif class_name == 'bicycle':
            color = (0, 255, 0)  # Blue color for persons
        pts = np.array(points, np.float32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image_with_gt, [np.int32(pts)], isClosed=True, color=color, thickness=2)
        
        # Add class name to the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image_with_gt, class_name, (int(points[0][0]), int(points[0][1]) - 10), font, 0.5, color, 2)
            
    return image_with_gt

# Function to read ground truth from txt file
def read_ground_truth(txt_file):
    with open(txt_file, 'r') as file:
        ground_truth = file.read().split()
    return ground_truth

# Folder paths
images_folder = '../datasets/DOTA_devkit/examplesplit/images'
ground_truth_folder = '../datasets/DOTA_devkit/examplesplit/labelTxt'

# Output folder path
output_folder = '../datasets/DOTA_devkit/examplesplit/groundtruth'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image and corresponding ground truth
c = 0
for image_name in os.listdir(images_folder):
    if image_name.endswith('.jpg'):
        c+=1
        print(c)
        image_path = os.path.join(images_folder, image_name)
        txt_path = os.path.join(ground_truth_folder, os.path.splitext(image_name)[0] + '.txt')
        
        # Read the image
        image = cv2.imread(image_path)
        
        # Read ground truth
        ground_truth = read_ground_truth(txt_path)
        
        # Draw ground truth on the image
        image_with_ground_truth = draw_ground_truth(image, ground_truth)
        
        # Save the image with ground truth
        output_path = os.path.join(output_folder, image_name)
        cv2.imwrite(output_path, image_with_ground_truth)

print("Images processed and saved with ground truth.")
