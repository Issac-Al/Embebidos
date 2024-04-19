from gpiozero import Motor
from time import sleep

motor = Motor(forward=19, backward=26)

while True:
	motor.forward()
	sleep(5)
	motor.backward()
	sleep(5)
