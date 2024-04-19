from gpiozero import LightSensor, LED
from signal import pause

sensor = LightSensor(19)
led = LED(26)
#led2 = LED(19)

sensor.when_dark = led.off
sensor.when_light = led.on

pause()
