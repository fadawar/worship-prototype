import os

from PyQt5.QtCore import QModelIndex
from PyQt5.QtQuick import QQuickItem

from .model import DirModel, BackgroundsModel
from ..screen import Screen


class BackgroundsModule:
    def __init__(self,
                 root_item: QQuickItem,
                 loader_name: str,
                 dir_model: DirModel,
                 bg_model: BackgroundsModel,
                 preview: Screen):
        self.dir_model = dir_model
        self.bg_model = bg_model
        self.preview = preview
        self.gui = None
        self.wire_gui(root_item, loader_name)

    def wire_gui(self, root_item: QQuickItem, loader_name: str):
        self.gui = root_item.createObjects(
            os.path.join(os.path.dirname(__file__), 'BackgroundsModule.qml'),
            loader_name)
        self.gui.setProperty('bgTreeModel', self.dir_model)
        self.gui.setProperty('bgThumbsModel', self.bg_model)
        self.gui.dirActivated.connect(self.display_backgrounds_in)
        self.gui.selectedBackground.connect(self.show_background)

    def display_backgrounds_in(self, index: QModelIndex):
        directory = index.internalPointer()
        self.bg_model.find_backgrounds_in(directory)

    def show_background(self, index: int):
        self.preview.show_background(self.bg_model.background_by(index))
