import os

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
SONGS_DIR = os.path.join(BASE_DIR, 'songs/')
BG_DIR = os.path.join(BASE_DIR, 'backgrounds/')

THUMB_SIZE = (80, 60)
THUMB_PATTERN = ".{}.thumb.jpg"
IMAGE_PATTERN = "^(?!\.).*\.(jpg|png|gif)$"
