from io import BytesIO
from pathlib import Path
from typing import List
from pdf2image import convert_from_path
from PIL import Image
from PIL.PpmImagePlugin import PpmImageFile

from src.paths import poppler_path


def convert_pdf_to_images(path: Path) -> List[PpmImageFile]:
    return convert_from_path(str(path),
                             poppler_path=poppler_path)


def merge_pages(pages: List[PpmImageFile]) -> Image:
    widths, heights = zip(*(i.size for i in pages))
    max_width = max(widths)
    total_height = sum(heights)
    result_image = Image.new('RGB', (max_width, total_height))
    y_offset = 0
    for image in pages:
        result_image.paste(image, (0, y_offset))
        image_height = image.size[1]
        y_offset += image_height
    return result_image


def convert_image_to_bytes_io(image: Image) -> BytesIO:
    bytes_io = BytesIO()
    image.save(bytes_io, 'JPEG')
    bytes_io.seek(0)
    return bytes_io


def convert_pdf_to_image(path: Path) -> BytesIO:
    pages = convert_pdf_to_images(path)
    result_image = merge_pages(pages)
    return convert_image_to_bytes_io(result_image)
