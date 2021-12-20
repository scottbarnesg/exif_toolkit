from typing import Dict

import exif


file_types = [".jpeg", ".jpg", ".png", ".tiff"]
filename_modifier = "_modified_exif"


class ExifGenerator:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.img = None
        self.exif_data = None

    def load_exif(self):
        with open(self.filepath, 'rb') as image_file:
            self.exif_data = exif.Image(image_file)

    def get_exif(self) -> Dict[str, any]:
        return self.exif_data.get_all()

    def set_exif_value(self, key, value):
        self.exif_data.set(key, value)

    def save_image_with_exif(self):
        with open(self.get_modified_filepath(), 'wb') as new_image_file:
            new_image_file.write(self.exif_data.get_file())

    def get_modified_filepath(self) -> str:
        for file_type in file_types:
            if file_type in self.filepath:
                return self.filepath.replace(file_type, filename_modifier + file_type)
        raise TypeError("Unsupported filetype")
