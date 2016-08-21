FROM fadawar/docker-pyqt5-qml-qtmultimedia

RUN apt-get install -y \
        python3-pip \
        ffmpeg

RUN pip3 install ffmpy Pillow
