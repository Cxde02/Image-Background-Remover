import os
from rembg import remove
from PIL import Image

input_folder = 'C:/Users/user/Documents/Python VSCode/BG'
output_folder = 'C:/Users/user/Documents/Python VSCode/NOBG'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    # Check if the item is a file and has a valid image extension
    if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.avif')):
        input_path = file_path
        output_path = os.path.join(output_folder, f'removed_bg_{os.path.splitext(filename)[0]}.png')

        # Open the image
        input_image = Image.open(input_path)

        # Convert the image to RGBA mode if it doesn't have an alpha channel
        if input_image.mode != 'RGBA':
            input_image = input_image.convert('RGBA')

        # Remove the background
        output_image = remove(input_image)

        # Save the output image with a new name in the output folder as PNG
        output_image.save(output_path, 'PNG')

        print(f"Background removed for {filename} and saved as {output_path}")
