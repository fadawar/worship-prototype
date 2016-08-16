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

Video thumbnail with ffmpeg
---------------------------
```
ffmpeg -y -i echo.mp4 -vf  "thumbnail,scale=80:60" -frames:v 1 thumb.png
```
http://superuser.com/questions/538112/meaningful-thumbnails-for-a-video-using-ffmpeg