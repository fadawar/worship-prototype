from PyQt5.QtCore import QUrl, QRect
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView


def suc(index):
    print("Ide to {}".format(index))

if __name__ == '__main__':
    import os
    import sys

    app = QGuiApplication(sys.argv)

    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(
        QUrl.fromLocalFile(
            os.path.join(os.path.dirname(__file__), 'main.qml')
        )
    )

    view.show()

    root = view.rootObject()

    dataList = ["Item 1", "Item 2", "Item 3", "Item 4"]

    rect = root.createSpriteObjects()
    rect.clicked.connect(suc)
    rect.setProperty('songListModel', dataList)

    sys.exit(app.exec_())
