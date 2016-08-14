# worship-prototype

Run in docker
-------------
```
docker run -it \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $(pwd):/app \
    -e DISPLAY=$DISPLAY \
    -u myusername \
    --group-add audio \
    --device /dev/snd \
    fadawar/docker-pyqt5-qml-qtmultimedia python3 /app/run.py
```
