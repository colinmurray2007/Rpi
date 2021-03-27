import gpiozero
import picamera
import datetime as dt
from signal import pause

button1 = gpiozero.Button(PUT GPIO PORT NUMBER HERE)
button2 = gpiozero.Button(PUT GPIO PORT NUMBER HERE)
camera = picamera.PiCamera()

def capture():
    camera.resolution = (1920, 1080)
#    camera.iso = 100
#    camera.annotate_background = picamera.Color('black')
#    camera.annotate_text = dt.datetime.now().strftime("%A, %d-%b %H:%M")
    camera.capture('/home/pi/' + dt.datetime.now().strftime("%d%m%y_%H%M") + '.jpg')
    camera.close()

button1.when_pressed = capture
button2.when_pressed = camera.start_preview
button2.when_released = camera.stop_preview

pause()