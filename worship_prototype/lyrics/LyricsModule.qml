import QtQuick 2.0
import QtQuick.Controls 1.4

Rectangle {
    id: root
    color: "transparent"

    signal songSelected(int index)
    signal verseSelected(int index)

    property alias allSongsModel: allSongsView.model
    property alias songDetailModel: songDetailView.model

    SplitView {
        orientation: Qt.Horizontal
        anchors.fill: parent

        // List of songs
        ScrollView {
            width: parent.width * 0.5

            ListView {
                id: allSongsView
                anchors.fill: parent
                spacing: 1
                clip: true

                delegate: Rectangle {
                    width: parent.width
                    height: titleText.height

                    Text {
                        id: titleText
                        text: title
                        width: parent.width
                        wrapMode: Text.Wrap
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: { root.songSelected(index) }
                    }
                }
            }
        }

        // Detail of song (all verses)
        ScrollView {
            width: parent.width * 0.5

            ListView {
                id: songDetailView
                anchors.fill: parent
                clip: true
                spacing: 1

                delegate: Rectangle {
                    width: parent.width
                    height: verseText.height

                    Text {
                        id: verseText
                        text: verse
                        width: parent.width
                        wrapMode: Text.Wrap
                    }
                    MouseArea {
                        anchors.fill: parent
                        onClicked: { root.verseSelected(index) }
                    }
                }
            }
        }
    }


}
