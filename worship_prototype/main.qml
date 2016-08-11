import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

Item {
    id: root
    width: 500; height: 500

    SplitView {
        orientation: Qt.Horizontal
        anchors.fill: parent

        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.minimumWidth: 100
            width: parent.width * 0.5
            color: "#6FA545"

            Loader {
                id: songsList
                anchors.fill: parent
            }
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.minimumWidth: 100
            width: parent.width * 0.5
            color: "#C9E5AB"

            Loader {
                id: previewScreen
                anchors.centerIn: parent
                width: 400
                height: 300
            }
        }
    }

    function createObjects(qmlPath, loaderName) {
        var component = Qt.createComponent(qmlPath);
        var target = eval(loaderName);

        if (component.status === Component.Ready) {
            target.sourceComponent = component;
            return target.item;
        } else if (component.status === Component.Error) {
            console.log("Error loading component:", component.errorString());
        } else {
            console.log("Error creating object");
        }
    }
}
