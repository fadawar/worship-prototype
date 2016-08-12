import glob

from PyQt5.QtCore import QAbstractListModel, QVariant, Qt
from PyQt5.QtCore import QThread

from ..config import SONGS_DIR
from .openlyrics import Song


class SongsList(QAbstractListModel):
    TitleRole = Qt.UserRole + 1
    _roles = {TitleRole: b'title'}

    def __init__(self):
        super().__init__()
        self._songs = []
        self.worker = LoadSongsThread(self._songs)
        self.load_songs_async()

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._songs)

    def data(self, index, role=None):
        if role == self.TitleRole:
            return self._songs[index.row()].props.titles[0].text
        return QVariant()

    def roleNames(self):
        return self._roles

    def song_by_index(self, index: int):
        return self._songs[index]

    def load_songs_async(self):
        self.worker.finished.connect(lambda: self.endResetModel())
        self.beginResetModel()
        self.worker.start()


class LoadSongsThread(QThread):
    def __init__(self, songs: list, parent=None):
        super().__init__(parent)
        self.songs = songs

    def run(self):
        self.load_songs_from(SONGS_DIR)

    def load_songs_from(self, directory: str):
        files = glob.glob("{}*.xml".format(directory))
        for file in files:
            self.songs.append(Song(file))
