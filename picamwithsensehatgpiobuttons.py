import gpiozero
import picamera
import datetime as dt
import sense_hat
from time import sleep
from signal import pause

button1 = gpiozero.Button(PUT GPIO PORT NUMBER HERE)
button2 = gpiozero.Button(PUT GPIO PORT NUMBER HERE)

camera = picamera.PiCamera()
sense = sense_hat.SenseHat()

#### SenseHat setup & LED Matrix Graphic

sense.clear()
sense.low_light = True

E = [0, 0, 0]
O = [255, 140, 0]

CPU = [
E, E, E, E, E, E, E, E,
E, O, E, O, E, O, E, E,
E, O, O, O, O, O, O, E,
E, O, O, O, O, O, O, E,
E, O, O, O, O, O, O, E,
E, O, O, O, O, O, O, E,
E, O, E, O, E, O, E, E,
E, E, E, E, E, E, E, E
]

t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

t = round(t, 1)
p = round(p, 1)
h = round(h, 1)

temp = "{0}'C".format(t)
press = "{0}mB".format(p)
hum = "{0}%".format(h)

#### The Program

def capture():
    camera.resolution = (1920, 1080)
#    camera.iso = 100
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = dt.datetime.now().strftime("%A, %d-%b %H:%M") + temp + press + hum
    camera.capture('/home/pi/' + dt.datetime.now().strftime("%d%m%y_%H%M") + '.jpg')
    camera.close()
	sense.set_pixels(CPU)
	sleep(2)
	sense.clear()

button1.when_pressed = capture
button2.when_pressed = camera.start_preview
button2.when_released = camera.stop_preview

pause()