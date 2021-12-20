import setuptools

setuptools.setup(
    name="exif_toolkit",
    version='0.1.0',
    description='A set of tools for reading, modifying, and deleting exif data from images.',
    url='https://github.com/scottbarnesg/exif_toolkit',
    packages=setuptools.find_packages(),
    install_requires=["Pillow", "exif"],
)