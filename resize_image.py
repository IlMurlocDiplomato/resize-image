from PIL import Image
import glob
import sys
import os

def convert_to_jpg(file):
    """
    Convert a file to JPG format.
    """
    try:
        # Open the image file
        img = Image.open(file)

        # Convert to RGB mode (if necessary)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Change the file extension to .jpg
        file_base = os.path.splitext(file)[0]
        new_file = file_base + '.jpg'

        # Save as JPG
        img.save(new_file, 'JPEG')

        return new_file
    except Exception as e:
        print(f"Error converting {file} to JPG:", str(e))
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file(s) or folder>")
        sys.exit(1)

    # Get the absolute path of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "output")

    paths = sys.argv[1:]

    for path in paths:
        if os.path.isdir(path):
            # If it's a directory, get all files inside
            files = glob.glob(os.path.join(path, '*'))
        else:
            # If it's a file, just use that file
            files = [path]

        for file in files:
            if not file.lower().endswith('.jpg'):
                # If the file is not a JPEG, convert it to JPEG
                new_file = convert_to_jpg(file)
                if new_file:
                    file = new_file

            try:
                # Open the image file (read-only)
                with Image.open(file) as image:
                    # Resize to thumbnail
                    image.thumbnail((2000, 2000))

                    # Create output directory if it doesn't exist
                    os.makedirs(output_dir, exist_ok=True)

                    # Save the resized image to output directory
                    output_file = os.path.join(output_dir, os.path.basename(file))
                    image.save(output_file)
                    print(f"Image {file} successfully resized and saved as {output_file}.")
                    print(image.size)
            except Exception as e:
                print(f"An error occurred with file {file}: {str(e)}")

if __name__ == "__main__":
    main()

