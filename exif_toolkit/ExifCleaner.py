import os
from multiprocessing import Process, Pool

import exif
import plum
import PIL
from PIL import Image

from common import apply_transforms

file_types = [".jpeg", ".jpg", ".png", ".tiff"]
filename_modifier = "_clean"


# TODO: Add target_dir, where clean images should be saved to
class ExifCleaner:
    def __init__(self, filepath: str, overwrite_files: bool = False):
        self.filepath = filepath
        self.overwrite_files = overwrite_files
        self.filename_modification = filename_modifier

    def clean_exif(self):
        try:
            img = self.load_image(self.filepath)
            transformed_img = apply_transforms(img)
            cleaned_img = self.remove_exif(transformed_img)
            if not self.verify_clean_file(cleaned_img):
                raise ValueError("Failed to clean image: " + self.filepath)
            cleaned_filepath = self.get_cleaned_filepath()
            self.save_image(cleaned_filepath, cleaned_img)
        except PIL.UnidentifiedImageError:
            print("Unable to load image: " + self.filepath)
            return False
        return True

    @staticmethod
    def load_image(filename: str) -> Image.Image:
        return Image.open(filename)

    @staticmethod
    def remove_exif(img: Image.Image) -> Image.Image:
        clean_image = Image.new(img.mode, img.size)
        clean_image.putdata(list(img.getdata()))
        return clean_image

    def get_cleaned_filepath(self):
        for file_type in file_types:
            if file_type in self.filepath:
                return self.filepath.replace(file_type, "_clean" + file_type)
        raise TypeError("Unsupported filetype")

    @staticmethod
    def verify_clean_file(img: Image.Image) -> bool:
        exif = img.getexif()
        if not exif:
            return True
        return False

    @staticmethod
    def save_image(new_filepath: str, img: Image.Image):
        img.save(new_filepath)


class BulkExifCleaner:
    def __init__(self, directory: str):
        self.directory = directory
        self.filename_modification = filename_modifier
        self.multiprocessing_pool = Pool(processes=4)

    def clean_exif(self):
        files = self.find_files(self.directory)
        total_files = len(files)
        counter = 1
        error_counter = 0
        for index, file in enumerate(files):
            print("(" + str(counter) + " of " + str(total_files) + "): " + "Cleaning file: " + str(file.path), end="... ")
            exif_cleaner = ExifCleaner(file.path)
            success = exif_cleaner.clean_exif()
            if not success:
                error_counter += 1
            else:
                print("Done.")
            counter += 1
        print("Skipped " + str(error_counter) + " of " + str(total_files))

    def find_files(self, directory: str) -> list:
        files = []
        for entry in os.scandir(directory):
            if entry.is_file() and \
                    any(file_type in entry.name for file_type in file_types) and \
                    self.filename_modification not in entry.name:
                files.append(entry)
        return files
