import os

from PyQt5.QtQuick import QQuickItem


class PreviewScreen:
    def __init__(self, root_item: QQuickItem):
        self.gui_item = None
        self.wire_gui(root_item)

    def wire_gui(self, root_item: QQuickItem):
        self.gui_item = root_item.createObjects(os.path.join(os.path.dirname(__file__), 'view.qml'), 'previewScreen')

    def show_text(self, text: str):
        self.gui_item.showText(text)

    def add_video(self, video: str):
        pass

    def add_image(self, image: str):
        pass
