import QtQuick 2.0
import QtQuick.Controls 1.4

Rectangle {
    id: root
    signal clicked(int index)

    property alias songListModel: songListView.model
    color: "transparent"

    ScrollView {
        anchors.fill: parent

        ListView {
            id: songListView
            anchors.fill: parent
            spacing: 2
            clip: true

            delegate: Rectangle {
                height: 25
                width: 75
                Text { text: index + ' ' + title }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                       root.clicked(index)
                    }
                }
            }
        }
    }
}
