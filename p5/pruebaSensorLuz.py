from  gpiozero import LightSensor
# charge_time_limit default is 0.01 for 1uF capacitor
ldr = LightSensor(19, charge_time_limit=0.1)
while True:
    print (ldr.value)
