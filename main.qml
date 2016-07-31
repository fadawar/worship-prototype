import QtQuick 2.0

Item {
    id: root
    width: 500; height: 500

    Rectangle {
        x: 100
        y: 10
        color: "green"
        width: 200; height: 200;
        Loader {
            id: songsList
        }
    }

    Text {
        anchors { bottom: parent.bottom; horizontalCenter: parent.horizontalCenter; bottomMargin: 20 }
        text: "Hello world"
    }

    function createObjects(qmlPath) {
        var component = Qt.createComponent(qmlPath);

        if (component.status === Component.Ready) {
            songsList.sourceComponent = component;
            return songsList.item;
        } else if (component.status === Component.Error) {
            console.log("Error loading component:", component.errorString());
        } else {
            console.log("Error creating object");
        }
    }
}