import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
README = (this_directory / "README.md").read_text()

setuptools.setup(
    name="exif_toolkit",
    version='0.1.0',
    description='A set of tools for reading, modifying, and deleting exif data from images.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/scottbarnesg/exif_toolkit',
    packages=setuptools.find_packages(),
    install_requires=["Pillow", "exif"],
    tests_require=["pytest"]
)