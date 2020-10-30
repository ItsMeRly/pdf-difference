from io import BytesIO
from pathlib import Path

from src.convert_pdf_to_image import convert_pdf_to_image
from src.paths import project_path


def save(bytes_io: BytesIO, file_path: Path) -> None:
    directory = file_path.parent
    directory.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(bytes_io.read())


image = convert_pdf_to_image(r'C:\path\to\file.pdf')
save(image, project_path / 'output' / 'merged pdf.jpg')
