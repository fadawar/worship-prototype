import os

from PyQt5.QtQuick import QQuickItem


class PreviewScreenController:
    def __init__(self, root_item: QQuickItem):
        self.wire_gui(root_item)

    def wire_gui(self, root_item: QQuickItem):
        rect = root_item.createObjects(os.path.join(os.path.dirname(__file__), 'view.qml'), 'previewScreen')
