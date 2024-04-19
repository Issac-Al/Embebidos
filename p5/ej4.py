from gpiozero import DistanceSensor, LED
from signal import pause
from time import sleep

sensor = DistanceSensor(19, 26, max_distance=1, threshold_distance=0.2)
led = LED(13)

#while True:
#	print(sensor.distance)
#	sleep(1)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

pause()
