import os

from PyQt5.QtQuick import QQuickItem

from ..screen.screen import Screen
from .model import SongsListModel


class LyricsModule:
    def __init__(self, model: SongsListModel, root_item: QQuickItem, preview_screen: Screen):
        self.model = model
        self.preview_screen = preview_screen
        self.wire_gui(root_item)

    def wire_gui(self, root_item: QQuickItem):
        rect = root_item.createObjects(os.path.join(os.path.dirname(__file__), 'view.qml'), 'songsList')
        rect.clicked.connect(self.show_song)
        rect.setProperty('songListModel', self.model.songs)

    def show_song(self, index):
        print("Showing song #{}".format(index))
        self.preview_screen.show_text(self.model.songs[index])
