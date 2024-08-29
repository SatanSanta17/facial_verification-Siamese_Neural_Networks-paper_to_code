from PIL import Image
import os
import uuid

def convert_and_rename_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Full path of the input file
        file_path = os.path.join(input_folder, filename)
        
        # Check if the file is an image
        if os.path.isfile(file_path):
            # Open the image file
            with Image.open(file_path) as img:
                # Convert image to RGB if not already in RGB mode
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Generate a unique filename
                unique_filename = str(uuid.uuid4()) + '.jpg'
                output_path = os.path.join(output_folder, unique_filename)
                
                # Save the image in JPG format
                img.save(output_path, 'JPEG')
                print(f'Converted and saved {filename} to {output_path}')

# Usage example
input_folder = 'data/negative'
output_folder = 'data/negativer'
convert_and_rename_images(input_folder, output_folder)
