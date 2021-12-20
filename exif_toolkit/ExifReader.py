import os

import exif
import plum.exceptions

file_types = [".jpeg", ".jpg", ".png", ".tiff"]
filename_modifier = "_clean"


class ExifReader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_exif(self) -> dict:
        with open(self.filepath, 'rb') as image_file:
            try:
                exif_data = exif.Image(image_file)
                return exif_data.get_all()
            except plum.exceptions.UnpackError:
                print("Failed to load image: " + self.filepath)


class BulkExifReader:
    def __init__(self, directory: str):
        self.directory = directory

    def get_exif(self) -> dict:
        exif_data = {}
        files = self.find_files(self.directory)
        for file in files:
            exif_reader = ExifReader(file.path)
            data = exif_reader.get_exif()
            exif_data[file.path] = data
        return exif_data

    @staticmethod
    def find_files(directory: str) -> list:
        files = []
        for entry in os.scandir(directory):
            if entry.is_file() and any(file_type in entry.name for file_type in file_types):
                files.append(entry)
        return files

    @staticmethod
    def print_exif_data(exif_data: dict):
        for file_path, exif in exif_data.items():
            print(str(file_path) + ": " + str(exif))
