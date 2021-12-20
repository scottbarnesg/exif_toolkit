import unittest

import pytest

from exif_toolkit.reader import ExifReader


class TestExifReader(unittest.TestCase):
    def test_read_file(self):
        file_path = "test/images/test-gps.jpg"
        reader = ExifReader(file_path)
        assert reader.get_exif()

    def test_read_file_not_found(self):
        file_path = "/bad-path"
        reader = ExifReader(file_path)
        with pytest.raises(FileNotFoundError):
            reader.get_exif()

