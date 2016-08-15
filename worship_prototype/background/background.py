import os
from abc import ABC, abstractmethod

from PIL import Image

from ..config import THUMB_PATTERN, THUMB_SIZE


class Background(ABC):
    @abstractmethod
    def is_video(self) -> bool:
        pass

    @abstractmethod
    def is_image(self) -> bool:
        pass

    @abstractmethod
    def file_url(self) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def thumbnail(self) -> 'Thumbnail':
        """Returns path to thumbnail"""
        pass


class VideoBackground(Background):
    def __init__(self, path: str):
        self.file = path

    def name(self) -> str:
        pass

    def thumbnail(self):
        pass

    def is_image(self):
        return False

    def is_video(self):
        return True

    def file_url(self):
        return self.file


class ImageBackground(Background):
    def __init__(self, path):
        self._path = path
        self._thumb = ImageThumbnail(self._path)

    def is_video(self) -> bool:
        return False

    def is_image(self) -> bool:
        return True

    def name(self) -> str:
        return os.path.basename(self._path)

    def file_url(self) -> str:
        return self._path

    def thumbnail(self) -> str:
        return self._thumb


class Thumbnail(ABC):
    @abstractmethod
    def file_path(self):
        pass


class ImageThumbnail(Thumbnail):
    def __init__(self, source_image):
        self._source = source_image
        if not self.is_created():
            self._create()

    def is_created(self):
        return os.path.exists(self.file_path())

    def _create(self):
        im = Image.open(self._source)
        im.thumbnail(THUMB_SIZE)
        im.save(self.file_path(), "JPEG")

    def file_path(self):
        name = os.path.basename(self._source)
        path = os.path.dirname(self._source)
        return os.path.join(path, THUMB_PATTERN.format(name))
