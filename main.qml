import QtQuick 2.0

Rectangle {
    id: appWindow
    color: "blue"
    width: 500; height: 500

    function createSpriteObjects() {
        var component = Qt.createComponent("sub.qml");
        var sprite = component.createObject(appWindow);
        songList.sourceComponent = component;

        if (sprite == null) {
            // Error Handling
            console.log("Error creating object");
        } else {
            return songList.item;
        }
    }

    Rectangle {
        x: 100
        y: 10
        color: "green"
        width: 200; height: 200;
        Loader {
            id: songList
        }
    }

    Text {
        anchors { bottom: parent.bottom; horizontalCenter: parent.horizontalCenter; bottomMargin: 20 }
        text: "Hello world"
    }
}