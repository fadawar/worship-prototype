import os
from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import QUrl
from PyQt5.QtQuick import QQuickItem

from ..background import Background


class Screen(metaclass=ABCMeta):
    """Show lyrics on the background. Background can be image or video."""

    @abstractmethod
    def wire_to_gui(self, root_item: QQuickItem, loader_name: str):
        pass

    @abstractmethod
    def show_text(self, text: str):
        pass

    @abstractmethod
    def show_background(self, background):
        pass


class DefaultScreen(Screen):
    def __init__(self):
        self.gui = None

    def wire_to_gui(self, root_item: QQuickItem, loader_name: str):
        self.gui = root_item.createObjects(os.path.join(os.path.dirname(__file__), 'screen.qml'), loader_name)

    def show_text(self, text: str):
        self.gui.showText(text)

    def show_background(self, background: Background):
        if background.is_video():
            self.gui.showVideoBackground(QUrl.fromLocalFile(background.file_url()))
        elif background.is_image():
            self.gui.showImageBackground(background.file_url())
