import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

from .background import VideoBackground, BackgroundsModule, DirModel, BackgroundsModel
from .lyrics import LyricsModule, SongsList
from .screen import DefaultScreen
from .config import SONGS_DIR, BG_DIR


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
    # preview.show_background(VideoBackground(os.path.join(os.path.dirname(__file__), '../echo.mp4')))
    # preview_live = DefaultScreen()
    # live = DefaultScreen()
    modules = [
        LyricsModule(SongsList(), root, 'lyricsModule', preview),
        BackgroundsModule(root, 'backgroundsModule', DirModel(BG_DIR), BackgroundsModel(), preview),
    ]

    sys.exit(app.exec_())
