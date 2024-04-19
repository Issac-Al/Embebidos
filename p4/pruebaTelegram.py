from config import *
import telebot
from gpiozero import LED
from time import sleep
from gpiozero import DistanceSensor

led = LED(26)
#sensor = DistanceSensor(echo=13, trigger=19)
#distSensor = 0
#turnOnSensor = False
#d = sensor.distance * 100
#print('Distance: ', d)

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start", "ayuda", "help"])

def cmd_start(message):
	#Da la bienvenida al usuario del bot
	bot.reply_to(message, "Bienvenido")

#@bot.message_handler(content_types=["text"])
#def bot_mensajes_texto(message):
#	if message.text.startswith("/"):
#		bot.send_message(message.chat.id, "comando no disponible")
#	else:
#		bot.send_message(message.chat.id, "cuentame mas :)")
@bot.message_handler(commands=["enciende"])
def turn_LED_on(message):
	led.on()
	bot.reply_to(message, "Encendiendo LEDS")

@bot.message_handler(commands=["apaga"])
def turn_LED_off(message):
	led.off()
	bot.reply_to(message, "Apagando LED")
@bot.message_handler(commands=["SensorON"])
def turn_sensor_on(message):
	global turnOnSensor
	turnOnSensor = True
	bot.reply_to(message, "Sensor encendido")
	while turnOnSensor:
		d = sensor.distance*100
		print(d)
		if(d < 20):
			bot.reply_to(message, "Alerta de proximidad en el sensor!!!")
		sleep(2)

@bot.message_handler(commands=["SensorOFF"])
def turn_sensor_off(message):
	global turnOnSensor
	turnOnSensor = False
	bot.reply_to(message, "Sensor apagado")

if __name__ == '__main__':
	print('Iniciando el bot')
	bot.infinity_polling()


