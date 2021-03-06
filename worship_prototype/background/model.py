import os
import re
from typing import List

from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QVariant, Qt
from PyQt5.QtCore import QAbstractListModel

from ..common import Directory, DefaultDirectory, CachedDirectory
from ..config import IMAGE_PATTERN, VIDEO_PATTERN
from .background import Background, ImageBackground, VideoBackground


class DirModel(QAbstractItemModel):
    def __init__(self, background_dir: str):
        super().__init__()
        self._base_dir = CachedDirectory(DefaultDirectory(background_dir, 0, None))

    def rowCount(self, parent: QModelIndex = None, *args, **kwargs):
        if not parent.isValid():
            return len(self._base_dir.directories())
        directory = parent.internalPointer()
        return len(directory.directories())

    def columnCount(self, parent=None, *args, **kwargs):
        return 1    # there is only one column - name of the directory

    def index(self, row, column, parent=None, *args, **kwargs):
        if not parent.isValid():
            return self.createIndex(row, column, self._base_dir.directories()[row])
        parent_dir = parent.internalPointer()
        return self.createIndex(row, column, parent_dir.directories()[row])

    def data(self, index: QModelIndex, role=None):
        if index.isValid() and role == Qt.DisplayRole:
            directory = index.internalPointer()
            return directory.name()
        return QVariant()

    def parent(self, index=None):
        if not index.isValid():
            return QModelIndex()
        directory = index.internalPointer()
        if directory.parent() is None:
            return QModelIndex()
        return self.createIndex(directory.parent().row(), 0, directory.parent())


class BackgroundsModel(QAbstractListModel):
    TitleRole = Qt.UserRole + 1
    ThumbnailRole = Qt.UserRole + 2
    _roles = {TitleRole: b'title', ThumbnailRole: b'thumbnail'}

    def __init__(self):
        super().__init__()
        self._backgrounds = []

    def find_backgrounds_in(self, directory: Directory) -> List[Background]:
        self.beginResetModel()
        self._backgrounds = \
            [ImageBackground(img) for img in self._find_files_in(directory, IMAGE_PATTERN)] + \
            [VideoBackground(vid) for vid in self._find_files_in(directory, VIDEO_PATTERN)]
        self.endResetModel()

    def _find_files_in(self, directory: Directory, pattern):
        files = []
        for x in os.listdir(directory.path()):
            if re.match(pattern, x):
                files.append(os.path.join(directory.path(), x))
        return files

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._backgrounds)

    def data(self, index, role=None):
        if role == self.TitleRole:
            return self._backgrounds[index.row()].name()
        elif role == self.ThumbnailRole:
            return self._backgrounds[index.row()].thumbnail().file_path()
        return QVariant()

    def roleNames(self):
        return self._roles

    def background_by(self, index) -> Background:
        return self._backgrounds[index]
