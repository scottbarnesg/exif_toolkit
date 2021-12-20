import os
import unittest

from exif_toolkit.generator import ExifGenerator
from exif_toolkit.reader import ExifReader


class TestExifGenerator(unittest.TestCase):
    def tearDown(self):
        os.remove("test/images/test-gps_modified_exif.jpg")

    def test_modify_exif_data(self):
        # Load image
        file_path = "test/images/test-gps.jpg"
        generator = ExifGenerator(file_path)
        generator.load_exif()
        # Modify exif data and save
        exif_key = 'make'
        exif_value = 'Samsung'
        generator.set_exif_value(exif_key, exif_value)
        generator.save_image_with_exif()
        # Load modified image and verify data has changed
        modified_file_path = "test/images/test-gps_modified_exif.jpg"
        reader = ExifReader(modified_file_path)
        modified_exif_data = reader.get_exif()
        print(modified_exif_data)
        assert modified_exif_data[exif_key] == exif_value
