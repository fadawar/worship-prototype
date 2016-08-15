from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QVariant, Qt
from ..common import DefaultDirectory, CachedDirectory


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
