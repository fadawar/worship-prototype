import os

from PyQt5.QtQuick import QQuickItem

from ..screen.screen import Screen
from .model import SongsList, SongDetail


class LyricsModule:
    def __init__(self, model: SongsList, root_item: QQuickItem, loader_name: str, preview_screen: Screen):
        self.model = model
        self.preview_screen = preview_screen
        self.gui = None
        self._selectedSong = None
        self.wire_gui(root_item, loader_name)

    def wire_gui(self, root_item: QQuickItem, loader_name: str):
        self.gui = root_item.createObjects(os.path.join(os.path.dirname(__file__), 'LyricsModule.qml'), loader_name)
        self.gui.songSelected.connect(self.show_song)
        self.gui.verseSelected.connect(self.show_verse)
        self.gui.setProperty('allSongsModel', self.model)

    def show_song(self, index):
        print("Showing song #{}".format(index))
        self._selectedSong = self.model.song_by_index(index)
        self.gui.setProperty('songDetailModel', SongDetail(self._selectedSong))

    def show_verse(self, index):
        self.preview_screen.show_text(str(self._selectedSong.verses[index]))
