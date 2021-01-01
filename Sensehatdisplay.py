## SenseHat - Needed for interfacing with the HAT itself
from sense_hat import SenseHat
## sleep - needed for programming momentary pauses in the script
from time import sleep
## datetime - needed for fetching the date/time
import datetime
## os - needed for fetching CPU temp
import os
## sys - needed for ending the script
import sys

## Define colours for the display and create icons for CPU, Temperature, Pressure and Humidity

R = [255, 0, 0] 
W = [255, 255, 255]
E = [0, 0, 0]
B = [0, 30, 255]
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

Temp = [
E, E, E, W, W, E, E, E,
E, E, E, W, W, E, E, E,
E, E, E, W, W, E, E, E,
E, E, W, W, W, W, E, E,
E, W, W, R, R, W, W, E,
E, W, W, R, R, W, W, E,
E, E, W, W, W, W, E, E,
E, E, E, W, W, E, E, E
]

Pressure = [
B, B, B, B, B, B, B, B,
E, B, E, E, B, E, E, B,
E, E, E, E, E, E, E, E,
E, E, E, E, E, E, E, E,
E, E, E, R, R, E, E, E,
E, E, R, R, R, R, E, E,
E, R, R, R, R, R, R, E,
R, R, R, R, R, R, R, R
]

Humidity = [
E, E, E, B, B, E, E, E,
E, E, E, B, B, E, E, E,
E, E, B, B, B, B, E, E,
E, B, B, B, B, B, B, E,
E, B, B, B, B, B, B, E,
E, B, B, B, B, B, B, E,
E, E, B, B, B, B, E, E,
E, E, E, B, B, E, E, E
]

## Fetch CPU temperature
def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

## Call SenseHat, clear the screen and set to low light mode
sense = SenseHat()
sense.clear()
sense.low_light = True

## Put the current date/time in a variable called 'now'
now = datetime.datetime.now()

## Fetch sensor readings and assign them to variables
t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

## Make the sensor readings more readable (down to 1 decimal place)
t = round(t, 1)
p = round(p, 1)
h = round(h, 1)

## Putting the (Day, Month, Date) and (Time) along with sensor readings (CPU)(t)(p)(h) in separate variables
msg1 = now.strftime("%A, %B %d")
msg2 = now.strftime("%-I:%M%p")
msg3 = measure_temp()
msg4 = "{0}'C".format(t)
msg5 = "{0}mB".format(p)
msg6 = "{0}%".format(h)

## Display the Day, Month, Date and Time along with sensor readings (and companion icons)
sense.show_message(msg1, scroll_speed=0.05)
sleep(1)
sense.show_message(msg2, scroll_speed=0.05)
sleep(1)
sense.set_pixels(CPU)
sleep(2)
sense.show_message(msg3, scroll_speed=0.05)
sleep(1)
sense.set_pixels(Temp)
sleep(2)
sense.show_message(msg4, scroll_speed=0.05)
sleep(1)
sense.set_pixels(Pressure)
sleep(2)
sense.show_message(msg5, scroll_speed=0.05)
sleep(1)
sense.set_pixels(Humidity)
sleep(2)
sense.show_message(msg6, scroll_speed=0.05)
sleep(1)

## Clear the screen and exit
sense.clear()
sys.exit()
