from PIL import Image
import os

def resize_and_convert_to_jpg(input_folder, output_folder, quality=95):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            
            png_image_path = os.path.join(input_folder, filename)
            png_image = Image.open(png_image_path)

            resized_image = png_image.resize((500, 500))

            jpg_image_path = os.path.join(output_folder, filename.replace(".png", ".jpg"))
            resized_image.convert("RGB").save(jpg_image_path, quality=quality, optimize=True)

            print(f"Converted and resized: {filename} to {jpg_image_path} with quality {quality}")

input_folder = "input/folder/path"
output_folder = "output/folder/path"
resize_and_convert_to_jpg(input_folder, output_folder, quality=95)
