from abc import ABCMeta, abstractmethod


class Background(metaclass=ABCMeta):
    @abstractmethod
    def is_video(self):
        pass

    @abstractmethod
    def is_image(self):
        pass

    @abstractmethod
    def file_url(self):
        pass


class VideoBackground(Background):
    def __init__(self, file: str):
        self.file = file

    def is_image(self):
        return False

    def is_video(self):
        return True

    def file_url(self):
        return self.file
