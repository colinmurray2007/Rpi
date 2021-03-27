import picamera
import datetime as dt
import sys

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.iso = 100
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = dt.datetime.now().strftime("%A, %d-%b %H:%M")
    camera.capture('/home/pi/Timelapse/Pictures/' + dt.datetime.now().strftime("%d%m%y_%H%M") + '.jpg')
    camera.close()

sys.exit()

