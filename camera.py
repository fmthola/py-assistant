from picamera import PiCamera
from time import sleep

picture_save_directory='./'

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture(picture_save_directory +'picture.jpg')
camera.stop_preview()
