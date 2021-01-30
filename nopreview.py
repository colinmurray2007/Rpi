from time import sleep
import picamera
from picamera import PiCamera
import datetime
import sys

now = datetime.datetime.now()

camera = PiCamera()
camera.resolution = (1920, 1080)


#Camera initialize and warm-up
#camera.start_preview()
camera.annotate_text = now.strftime("%A, %d-%b %H:%M")
camera.annotate_background = picamera.Color('black')
#sleep(5)

#Capture, save image and stop camera
camera.capture('/home/pi/HQTL/' + now.strftime("%d-%b-%A, %H:%M") + '.jpg')
#camera.stop_preview()

#exit
sys.exit()