from PyQt5.QtCore import QAbstractListModel, QVariant, Qt

from ..config import SONGS_DIR
from .openlyrics import Song


class SongsList(QAbstractListModel):
    TitleRole = Qt.UserRole + 1
    _roles = {TitleRole: b'title'}

    def __init__(self):
        super().__init__()
        self._songs = []
        self._songs.append(Song(SONGS_DIR + 'song.xml'))

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
