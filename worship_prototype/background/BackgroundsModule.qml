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
        width: parent.width * 0.5
        height: parent.height
        color: "#49e03e"

        GridView {
            id: bgThumbs
            anchors.fill: parent
            anchors.margins: 5

            clip: true
            model: 100
            cellWidth: 83
            cellHeight: 63

            delegate: Item {
                width: bgThumbs.cellWidth
                height: bgThumbs.cellHeight

                Rectangle {
                    anchors.fill: parent
                    anchors.margins: 3
                    color: "yellow"
                    Text {
                        anchors.centerIn: parent
                        text: index
                    }
                }
            }
        }
    }
}
