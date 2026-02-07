import shutil
from fastapi import UploadFile
from backend.config import PHOTO_DIR


class StorageService:

    @staticmethod
    def save_image(image: UploadFile | None):

        if not image:
            return None

        file_path = f"{PHOTO_DIR}/{image.filename}"

        with open(file_path, "wb") as pic:
            shutil.copyfileobj(image.file, pic)

        return file_path
