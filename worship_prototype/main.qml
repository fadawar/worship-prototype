import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

Item {
    id: root
    width: 900; height: 500

    SplitView {
        orientation: Qt.Horizontal
        anchors.fill: parent

        // Lyrics & backgrounds
        SplitView {
            orientation: Qt.Vertical
            width: parent.width * (2/3)

            // Lyrics
            Rectangle {
                width: parent.width
                height: parent.height * 0.5
                color: "#6FA545"

                Loader {
                    id: lyricsModule
                    anchors.fill: parent
                }
            }

            // Backgrounds
            Rectangle {
                width: parent.width
                height: parent.height * 0.5
                color: "#d8ddff"

                Loader {
                    id: backgroundsModule
                    anchors.fill: parent
                }
            }
        }

        // Screens
        Rectangle {
            Layout.minimumWidth: 100
            width: parent.width * (1/3)
            color: "#C9E5AB"

            Loader {
                id: previewScreen
                anchors.centerIn: parent
                width: 250     // ratio 4:3
                height: width * 0.75
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
