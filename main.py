from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlComponent, QQmlEngine
from PyQt5.QtQuick import QQuickView


def suc():
    print("Ide to")

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

    engine = view.engine()
    component = QQmlComponent(engine, QUrl.fromLocalFile(
            os.path.join(os.path.dirname(__file__), 'sub.qml')
        ),
        QQmlComponent.PreferSynchronous)
    component.create()

    # component.setParent(view.rootObject())
    # component.setParentItem(view.rootObject())

    print(component.property("width"))

    # view.setProperty("control", "sub.qml")

    view.show()

    root = view.rootObject()

    rect = root.createSpriteObjects()
    rect.clicked.connect(suc)

    # root.

    # root.setProperty("control", component.rootObject())

    # view.control = component

    sys.exit(app.exec_())
