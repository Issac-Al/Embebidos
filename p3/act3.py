from bluedot import BlueDot
from signal import pause
from gpiozero import PWMLED

def set_brightness_and_color(pos):
	brightness = (pos.y + 1) / 2
	ledOn = (pos.x + 1) / 2
	if(ledOn <= 0.333):
		ledWhite.on()
		ledRed.off()
		ledYellow.off()
		ledWhite.value = brightness
	elif(ledOn > 0.333 and ledOn <= 0.666):
		ledWhite.off()
		ledRed.off()
		ledYellow.on()
		ledYellow.value = brightness
	else:
		ledWhite.off()
		ledRed.on()
		ledYellow.off()
		ledRed.value = brightness
	print("Brightness: ", brightness)
	print("LED VALUE: ", ledOn)

ledWhite = PWMLED(13)
ledYellow = PWMLED(19)
ledRed = PWMLED(26)

bd = BlueDot()
bd.when_moved = set_brightness_and_color

pause()

