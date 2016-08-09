import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

from apps.previewscreen.controller import PreviewScreenController
from apps.songslist.model import SongsListModel
from apps.songslist.controller import SongsListController

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    app.setApplicationName("Worship Prototype")

    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(
        QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__), 'main.qml'))
    )
    view.show()

    root = view.rootObject()
    modules = [
        SongsListController(SongsListModel(), root),
        PreviewScreenController(root),
    ]

    sys.exit(app.exec_())
