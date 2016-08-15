import os

from PyQt5.QtCore import QAbstractItemModel
from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import Qt


class DirModel(QAbstractItemModel):
    def __init__(self, background_dir: str):
        super().__init__()
        self._dir = CachedDirectory(Directory(background_dir, 0, None))

    def rowCount(self, parent=None, *args, **kwargs):
        if not parent.isValid():
            return len(self._dir.directories())
        node = parent.internalPointer()
        return len(node.directories())

    def columnCount(self, parent=None, *args, **kwargs):
        return 1    # there is only one column - name of the directory

    def index(self, row, column, parent=None, *args, **kwargs):
        if not parent.isValid():
            return self.createIndex(row, column, self._dir.directories()[row])
        parent_node = parent.internalPointer()
        return self.createIndex(row, column, parent_node.directories()[row])

    def data(self, index: QModelIndex, role=None):
        if index.isValid() and role == Qt.DisplayRole:
            node = index.internalPointer()
            return node.name()
        return QVariant()

    def parent(self, index=None):
        if not index.isValid():
            return QModelIndex()
        node = index.internalPointer()
        if node.parent() is None:
            return QModelIndex()
        return self.createIndex(node.parent().row(), 0, node.parent())


class Directory:
    def __init__(self, path, row, parent):
        self._path = path
        self._row = row
        self._parent = parent

    def directories(self):
        dirs = []
        for row, path in enumerate(next(os.walk(self._path))[1]):
            dirs.append(Directory(os.path.join(self._path, path), row, self))
        return dirs

    def name(self):
        return os.path.basename(self._path)

    def parent(self):
        return self._parent

    def row(self):
        return self._row


class CachedDirectory:
    def __init__(self, directory: Directory):
        self._dir = directory
        self._files = None
        self._directories = None
        self._name = None

    def directories(self):
        if not self._directories:
            self._directories = [CachedDirectory(x) for x in self._dir.directories()]
        return self._directories

    def name(self):
        if not self._name:
            self._name = self._dir.name()
        return self._name

    def parent(self):
        return self._dir.parent()

    def row(self):
        return self._dir.row()
