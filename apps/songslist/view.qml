import QtQuick 2.0
import QtQuick.Controls 1.5

Rectangle {
    id: root
    signal clicked(int index)

    property alias songListModel: songListView.model

    color: "red"
    width: 100
    height: 100

    Text {
        text: "submodule"
    }

    ListView {
        id: songListView
        anchors.fill: parent
        spacing: 2
        clip: true

        delegate: Rectangle {
            height: 25
            width: 75
            Text { text: index + ' ' + modelData }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                   root.clicked(index)
                }
            }
        }
    }
}
