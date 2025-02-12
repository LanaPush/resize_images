from PIL import Image, ImageOps
from pathlib import Path
import argparse



def parameters():
    parser = argparse.ArgumentParser(description="Resize you image in a specified directory. Enter a format, width, height, input_path and output_path")
    parser.add_argument("format", type=str, help="enter the right format, for example: *.jpg.")
    parser.add_argument("width", type=int, help="The width to resize the images.")
    parser.add_argument("height", type=int, help="The height to resize the images.")
    parser.add_argument("input_path", type=Path, help="The input directory.")
    parser.add_argument("output_path", type=Path, help="Enter the output directory.")

    args = parser.parse_args()
    user_image_format = args.format
    image_max_width = args.width
    image_max_height = args.height
    folder_input = Path.home() / args.input_path
    folder_output = Path.home() /args.output_path

    folder_output.mkdir(parents=True, exist_ok=True)

    return folder_input, user_image_format, image_max_width, image_max_height, folder_output




def resize_image():
    folder_input, user_image_format, image_max_width, image_max_height, folder_output = parameters()
    foto_folder = list(folder_input.glob(user_image_format))

    # open image
    for i, image_path in enumerate(foto_folder, start=1):
        with Image.open(image_path) as im:
            im = ImageOps.exif_transpose(im)
            
            original_width, original_height = im.size

            max_width = image_max_width
            max_height = image_max_height

        # Calculate the scaling factor to maintain aspect ratio
            scale = min(max_width/original_width, max_height/original_height)

            new_width = int(original_width * scale)
            new_height = int(original_height * scale)

        # resize image
            resized_image = im.resize((new_width, new_height), Image.LANCZOS)

        #new image
            output_path = folder_output / f"resized_image_{i}{image_path.suffix}"

            resized_image.save(output_path)
            print("Saved")

if __name__ == "__main__":
    resize_image()









