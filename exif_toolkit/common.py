from PIL import Image, ExifTags, ImageOps


def load_image(filename: str) -> Image.Image:
    return Image.open(filename)


def read_exif(image: Image.Image) -> Image.Exif:
    return image.getexif()


def parse_exif(exif: Image.Exif) -> dict:
    exif_data = {}
    if exif is None:
        return exif_data
    for key, val in exif.items():
        if key in ExifTags.TAGS:
            exif_data[ExifTags.TAGS[key]] = val
    return exif_data


def apply_transforms(img: Image.Image) -> Image.Image:
    return ImageOps.exif_transpose(img)


def get_exif_key_by_value(value: str) -> int:
    for exif_key, exif_value in ExifTags.TAGS.items():
        if value == exif_value:
            return exif_key
    raise ValueError("Invalid EXIF value provided")