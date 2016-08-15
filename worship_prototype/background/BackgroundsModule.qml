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
        //anchors.fill: parent
        //anchors.margins: 2 * 12 + row.height
        //selection: sel

        TableViewColumn {
            title: "Backgrounds directories"
            role: "display"
            resizable: true
        }

//        onActivated : {
//            var url = fileSystemModel.data(index, FileSystemModel.UrlStringRole)
//            Qt.openUrlExternally(url)
//        }
    }

    Rectangle {
        id: bgThumbs
        width: parent.width * 0.5
        height: parent.height
        color: "#49e03e"
    }
}
