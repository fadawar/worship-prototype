import os
from abc import ABC, abstractmethod

import ffmpy
from PIL import Image

from ..config import THUMB_SIZE, THUMB_PATTERN


class Thumbnail(ABC):
    @abstractmethod
    def file_path(self):
        pass


class ImageThumbnail(Thumbnail):
    def __init__(self, source_image):
        self._source = source_image
        if not self._exists():
            self._create()

    def _exists(self):
        return os.path.exists(self.file_path())

    def _create(self):
        im = Image.open(self._source)
        im.thumbnail(THUMB_SIZE)
        im.save(self.file_path(), "JPEG")

    def file_path(self):
        name = os.path.basename(self._source)
        path = os.path.dirname(self._source)
        return os.path.join(path, THUMB_PATTERN.format(name))


class VideoThumbnail(Thumbnail):
    def __init__(self, source_video):
        self._source = source_video
        if not self._exists():
            self._create()

    def _exists(self):
        return os.path.exists(self.file_path())

    def _create(self):
        ff = ffmpy.FFmpeg(
            inputs={self._source: '-y'},
            outputs={self.file_path(): '-vf  "thumbnail,scale={}:{}" -frames:v 1'.format(
                THUMB_SIZE[0],
                THUMB_SIZE[1],
            )}
        )
        ff.run()

    def file_path(self):
        name = os.path.basename(self._source)
        path = os.path.dirname(self._source)
        return os.path.join(path, THUMB_PATTERN.format(name))
