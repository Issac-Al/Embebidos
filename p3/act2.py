from bluedot import BlueDot
from signal import pause
from time import sleep
from gpiozero import LED

def change_to_red(g,y,r):
	g.off()
	green_led_on = False
	y.on()
	sleep(1)
	y.off()
	r.on()
	sleep(3)
	r.off()
	g.on()
	green_led_on = True

bd = BlueDot()
led1 = LED(13)
led2 = LED(19)
led3 = LED(26)
green_led_on = True

led1.on()

while True:
	if(green_led_on):
		print(green_led_on)
		bd.wait_for_press()
		change_to_red(led1, led2, led3)



