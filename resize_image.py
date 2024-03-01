"""
Author: IlMurlocDiplomato
"""
from PIL import Image, ImageFile
import glob
import sys
import os
from pdf2image import convert_from_path

# Set max size of the image to  500 MB (500 * 1024 * 1024 byte)
Image.MAX_IMAGE_PIXELS = 500 * 1024 * 1024

# Increase the limit file size of temporary file
ImageFile.LOAD_TRUNCATED_IMAGES = True

def convert_to_jpg(file, dpi):
    try:
        # Check if the file is a PDF
        if file.lower().endswith('.pdf'):
            print(f"Converting {file} to JPG...")
            # Convert PDF to images
            pages = convert_from_path(file, dpi)
            converted_files = []

            # Save each page as JPG
            for i, page in enumerate(pages):
                new_file = f"{os.path.splitext(file)[0]}_page{i+1}.jpg"
                page.save(new_file, 'JPEG')
                converted_files.append(new_file)

            print(f"PDF {file} converted to JPG successfully.")
            return converted_files
        else:
            # It's not a PDF file, so it's already an image file
            return [file]
    except Exception as e:
        print(f"Error converting {file} to JPG:", str(e))
        return []

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file(s) or folder>")
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "output")

    paths = sys.argv[1:]

    thumbnail_size_input = input("Enter thumbnail size (leave blank for default 2000): ")
    thumbnail_size = (2000, 2000) if thumbnail_size_input == '' else (int(thumbnail_size_input), int(thumbnail_size_input))

    dpi_input = input("Enter DPI for PDF conversion (leave blank for default 300): ")
    dpi = 300 if dpi_input == '' else int(dpi_input)

    for path in paths:
        if os.path.isdir(path):
            files = glob.glob(os.path.join(path, '*'))
        else:
            files = [path]

        for file in files:
            print(f"Processing file: {file}")
            try:
                new_files = convert_to_jpg(file, dpi)
                for new_file in new_files:
                    with Image.open(new_file) as image:
                        image.thumbnail(thumbnail_size)
                        os.makedirs(output_dir, exist_ok=True)
                        output_file = os.path.join(output_dir, os.path.basename(new_file))
                        image.save(output_file)
                        print(f"Image {new_file} successfully resized and saved as {output_file}.")
                        print(f"New image size: {image.size}")
            except Exception as e:
                print(f"An error occurred with file {file}: {str(e)}")

if __name__ == "__main__":
    main()
