import os
import unittest

from exif_toolkit.cleaner import ExifCleaner
from exif_toolkit.reader import ExifReader


class TestExifCleaner(unittest.TestCase):
    def tearDown(self):
        os.remove("test/images/test-gps_clean.jpg")

    def test_clean_image(self):
        # Load image
        file_path = "test/images/test-gps.jpg"
        cleaner = ExifCleaner(file_path)
        # Clean image
        cleaner.clean_exif()
        # Load cleaned image and verify it has no exif data
        clean_file_path = "test/images/test-gps_clean.jpg"
        reader = ExifReader(clean_file_path)
        assert not reader.get_exif()
