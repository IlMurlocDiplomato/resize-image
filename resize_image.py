from PIL import Image
import glob
import sys
import os

def convert_to_jpg(file):
    try:
        img = Image.open(file)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        file_base = os.path.splitext(file)[0]
        new_file = file_base + '.jpg'
        img.save(new_file, 'JPEG')
        return new_file
    except Exception as e:
        print(f"Error converting {file} to JPG:", str(e))
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file(s) or folder>")
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "output")

    paths = sys.argv[1:]

    thumbnail_size_input = input("Enter thumbnail size (leave blank for default 2000): ")
    thumbnail_size = (2000, 2000) if thumbnail_size_input == '' else (int(thumbnail_size_input), int(thumbnail_size_input))

    for path in paths:
        if os.path.isdir(path):
            files = glob.glob(os.path.join(path, '*'))
        else:
            files = [path]

        for file in files:
            if not file.lower().endswith('.jpg'):
                new_file = convert_to_jpg(file)
                if new_file:
                    file = new_file

            try:
                with Image.open(file) as image:
                    image.thumbnail(thumbnail_size)
                    os.makedirs(output_dir, exist_ok=True)
                    output_file = os.path.join(output_dir, os.path.basename(file))
                    image.save(output_file)
                    print(f"Image {file} successfully resized and saved as {output_file}.")
                    print(image.size)
            except Exception as e:
                print(f"An error occurred with file {file}: {str(e)}")

if __name__ == "__main__":
    main()
