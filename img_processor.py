import logging
import os
from functions import ocr, categorize, process_image

logging.basicConfig(filename='app.log', level=logging.INFO)

images_folder = '/path/images'

def main():
    for filename in os.listdir(images_folder):
        image_path = os.path.join(images_folder, filename)
        process_image(image_path)

if __name__ == '__main__':
    main()
    