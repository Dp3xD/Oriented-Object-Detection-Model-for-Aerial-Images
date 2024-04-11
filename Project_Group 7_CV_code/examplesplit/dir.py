from PIL import Image
import os

def convert_jpg_to_png(jpg_path, png_path):
    try:
        # Open the JPG image
        img = Image.open(jpg_path)
        
        # Convert to RGB mode if the image is in CMYK mode
        if img.mode == 'CMYK':
            img = img.convert('RGB')
        
        # Save as PNG
        img.save(png_path, 'PNG')
        print(f"Conversion successful: {jpg_path} converted to {png_path}")
    except Exception as e:
        print(f"Conversion failed: {e}")

def batch_convert_jpg_to_png(input_folder, output_folder):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through all JPG files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            jpg_path = os.path.join(input_folder, filename)
            png_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
            convert_jpg_to_png(jpg_path, png_path)

# Example usage
input_folder = './images'
output_folder = './image '
batch_convert_jpg_to_png(input_folder, output_folder)

