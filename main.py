import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

from apps.previewscreen.controller import PreviewScreen
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
    preview_screen = PreviewScreen(root)
    modules = [
        SongsListController(SongsListModel(), root, preview_screen),
    ]

    sys.exit(app.exec_())
