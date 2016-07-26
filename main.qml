import QtQuick 2.0

Rectangle {
    id: appWindow
    color: "blue"
    property alias control : pageLoader.source
    width: 500; height: 200

    function createSpriteObjects() {
        var component = Qt.createComponent("sub.qml");
        var sprite = component.createObject(appWindow, {"x": 100, "y": 100});

        if (sprite == null) {
            // Error Handling
            console.log("Error creating object");
        } else {
            return sprite;
        }
    }

    Loader {
        id: pageLoader
        //source: "sub.qml"
    }

    Text {
        anchors { bottom: parent.bottom; horizontalCenter: parent.horizontalCenter; bottomMargin: 20 }
        text: "Hello world"
    }
}