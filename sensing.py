from gpiozero import CPUTemperature
from sense_hat import SenseHat
from time import sleep, time
import datetime
import sys
sense = SenseHat()
now = datetime.datetime.now()
cpu = CPUTemperature()

## Fetch sensor readings and assign them to variables
t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

## Make the sensor readings more readable (down to 1 decimal place)
t = round(t, 1)
p = round(p, 1)
h = round(h, 1)

with open("/home/pi/sensing.csv", "a") as log:
    while True:
        temp = cpu.temperature
        log.write("{0},{1},{2},{3},{4}\n".format(now.strftime("%d/%m/%Y - %-I:%M%p"),str(temp),str(t),str(p),str(h)))
        sys.exit()