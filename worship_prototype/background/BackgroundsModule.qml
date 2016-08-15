import QtQuick 2.0
import QtQuick.Controls 1.4


SplitView {
    id: root
    anchors.fill: parent

    property alias bgTreeModel: bgTree.model
    property alias bgThumbsModel: bgThumbs.model
    signal dirActivated(var item)

    TreeView {
        id: bgTree
        width: parent.width * 0.5
        height: parent.height

        TableViewColumn {
            title: "Directories with backgrounds"
            role: "display"
            resizable: true
        }

        onActivated: root.dirActivated(index)
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
            cellWidth: 86
            cellHeight: 76

            delegate: Item {
                width: bgThumbs.cellWidth
                height: bgThumbs.cellHeight

                Item {
                    anchors.fill: parent
                    anchors.margins: 3

                    Image {
                        id: thumb
                        width: 80
                        height: 60
                        source: thumbnail
                    }

                    Text {
                        anchors.top: thumb.bottom
                        anchors.topMargin: 1
                        width: thumb.width
                        elide: Text.ElideRight
                        font.pixelSize: 10
                        text: title
                    }
                }
            }
        }
    }
}
