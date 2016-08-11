import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

from .screen import DefaultScreen
from .lyrics import LyricsModule, SongsListModel


def run_app():
    app = QGuiApplication(sys.argv)
    app.setApplicationName("Worship Prototype")

    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__), 'main.qml')))
    view.show()

    root = view.rootObject()
    preview = DefaultScreen()
    preview.wire_to_gui(root, 'previewScreen')
    # preview_live = DefaultScreen()
    # live = DefaultScreen()
    modules = [
        LyricsModule(SongsListModel(), root, preview),
    ]

    sys.exit(app.exec_())
