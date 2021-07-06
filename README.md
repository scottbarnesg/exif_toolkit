# Exif Toolkit

A set of tools for reading, modifying, and deleting exif data from images.

## Reading Exif Data

#### From a single image:
```
exif_reader = ExifReader("/path/to/file.jpg")
exif_data = exif_reader.get_exif()
```

#### From all image files in a directory:

```
exif_bulk_reader = BulkExifReader("/path/to/directory")
exif_data = exif_bulk_reader.get_exif()
exif_bulk_reader.print_exif_data(exif_data)
```

## Deleting Exif Data

#### From a single image:

```
exif_reader = ExifCleaner("/path/to/file.jpg")
exif_reader.clean_exif()
```

#### From all images in a directory
```
bulk_exif_cleaner = BulkExifCleaner("/path/to/directory")
bulk_exif_cleaner.clean_exif()
```

## Modifying Exif Data

```
exif_generator = ExifGenerator("/path/to/file.jpg")
exif_generator.load_exif()
modified_exif_key = 'Make'
modified_exif_value = 'Samsung'
exif_generator.set_exif_value(modified_exif_key, modified_exif_value)
exif_generator.save_image_with_exif()
```