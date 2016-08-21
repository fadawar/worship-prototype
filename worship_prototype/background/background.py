import os
from abc import ABC, abstractmethod

from .thumbnail import Thumbnail, VideoThumbnail, ImageThumbnail


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
        self._path = path
        self._thumb = VideoThumbnail(self._path)

    def name(self) -> str:
        return os.path.basename(self._path)

    def thumbnail(self):
        return self._thumb

    def is_image(self):
        return False

    def is_video(self):
        return True

    def file_url(self):
        return self._path


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


