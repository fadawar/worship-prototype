import QtQuick 2.0

Rectangle {
    color: "red"
    width: 100
    height: 100
    signal clicked()
    MouseArea {
        anchors.fill: parent
        onClicked: {
           parent.clicked()  // emit the parent's signal
        }
    }


    Text {
        text: "submodule"
    }
}