from gpiozero import CPUTemperature
from time import sleep, time
import datetime
import sys

now = datetime.datetime.now()
cpu = CPUTemperature()

with open("/home/pi/cpu_temp.csv", "a") as log:
    while True:
        temp = cpu.temperature
        log.write("{0},{1},{2}\n".format(now.strftime("%A, %B %d"),now.strftime("%-I:%M%p"),str(temp)))
        sys.exit()



