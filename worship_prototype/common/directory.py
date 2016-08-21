import os
from abc import ABC, abstractmethod
from typing import List


class Directory(ABC):
    """Represent directory in file system"""

    @abstractmethod
    def directories(self) -> List['Directory']:
        """Returns subdirectories"""
        pass

    @abstractmethod
    def name(self) -> str:
        """Returns name of directory"""
        pass

    @abstractmethod
    def parent(self) -> 'Directory':
        """Returns parent directory"""
        pass

    @abstractmethod
    def path(self) -> str:
        pass


class RowAwareDirectory(Directory):
    @abstractmethod
    def row(self) -> int:
        pass


class DefaultDirectory(RowAwareDirectory):
    def __init__(self, path: str, row: int, parent: Directory = None):
        self._path = path
        self._row = row
        self._parent = parent

    def directories(self):
        dirs = []
        for row, dir_name in enumerate(next(os.walk(self._path))[1]):
            dirs.append(DefaultDirectory(os.path.join(self._path, dir_name), row, self))
        return dirs

    def name(self):
        return os.path.basename(self._path)

    def parent(self):
        return self._parent

    def row(self):
        return self._row

    def path(self):
        return self._path


class CachedDirectory(RowAwareDirectory):
    def __init__(self, directory: RowAwareDirectory):
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

    def path(self):
        return self._dir.path()
