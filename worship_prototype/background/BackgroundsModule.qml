import QtQuick 2.0
import QtQuick.Controls 1.4


SplitView {
    id: root
    anchors.fill: parent

    property alias bgTreeModel: bgTree.model
    property alias rootPathIndex: bgTree.rootIndex

    TreeView {
        id: bgTree
        width: parent.width * 0.5
        height: parent.height

        TableViewColumn {
            title: "Directories with backgrounds"
            role: "display"
            resizable: true
        }
    }

    Rectangle {
        id: bgThumbs
        width: parent.width * 0.5
        height: parent.height
        color: "#49e03e"
    }
}
