import QtQuick 2.0
import QtQuick.Controls 1.4
import QtMultimedia 5.0

Video {
    id: root
    width : 400
    height : 300
    source: "../../echo.mp4"
    muted: true
    focus: true
    Keys.onSpacePressed: video.playbackState == MediaPlayer.PlayingState ? video.pause() : video.play()
    Keys.onLeftPressed: video.seek(video.position - 5000)
    Keys.onRightPressed: video.seek(video.position + 5000)

    MouseArea {
        anchors.fill: parent
        onClicked: {
            root.play()
        }
    }
}
