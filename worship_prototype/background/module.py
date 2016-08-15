import os

from PyQt5.QtCore import QModelIndex
from PyQt5.QtQuick import QQuickItem

from .model import DirModel


class BackgroundsModule:
    def __init__(self, root_item: QQuickItem, loader_name: str, dir_model: DirModel):
        self.dir_model = dir_model
        self.gui = None
        self.wire_gui(root_item, loader_name)

    def wire_gui(self, root_item: QQuickItem, loader_name: str):
        self.gui = root_item.createObjects(
            os.path.join(os.path.dirname(__file__), 'BackgroundsModule.qml'),
            loader_name)
        self.gui.setProperty('bgTreeModel', self.dir_model)
        # self.gui.setProperty('rootPathIndex', self.dir_model.index(0, 0, QModelIndex()))
