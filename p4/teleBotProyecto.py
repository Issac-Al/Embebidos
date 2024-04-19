from config import *
import telebot
from gpiozero import LED
from time import sleep
from telebot import types

class PersonasHuellas:
	def __init__(self, nombre, IDHuella):
		self.nombre = nombre
		self.IDHuella = IDHuella

lista_prueba = [PersonasHuellas("Issac", "1"), PersonasHuellas("Issac", "2"), PersonasHuellas("Ale", "1")]
lista_en_string = '\n'.join([f"Nombre: {item.nombre}, ID de Huella: {item.IDHuella}" for item in lista_prueba])
bot = telebot.TeleBot(TELEGRAM_TOKEN)
user_data = {}
nombre = ""
texto = ""

@bot.message_handler(commands=["comandos", "Comandos", "COMANDOS"])
def CMD_Comandos(message):
	bot.reply_to(message, "Los comandos implementados actualmente son: \ncerrar_puerta\nabrir_puerta\neliminar_huella\nlistar_huellas")

@bot.message_handler(commands=["eliminar_huella", "Eliminar_huella", "ELIMINAR_HUELLA", "Eliminar_Huella"])
def CMD_Eliminacion_Usuario(message):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add(types.KeyboardButton('Siguiente'))
	bot.reply_to(message, text=f"Aqui esta la lista de huellas disponibles: \n{lista_en_string}", reply_markup=markup)
	user_data[message.chat.id] = 1

@bot.message_handler(commands=["abrir_puerta", "Abrir_puerta", "Abrir_Puerta", "ABRIR_PUERTA"])
def CMD_Abrir_Puerta(message):
	#usr_text = message.text
	bot.reply_to(message, "entendido!")
	#print(usr_text)

@bot.message_handler(commands=["cerrar_puerta", "Cerrar_puerta", "Cerrar_Puerta", "CERRAR_PUERTA"])
def CMD_Abrir_Puerta(message):
        #usr_text = message.text
        bot.reply_to(message, "puertas cerradas!")
        #print(usr_text)

@bot.message_handler(commands=["listar_huellas"])
def CMD_Listar_Huellas(message):
	bot.reply_to(message, text=f"{lista_en_string}")

@bot.message_handler(func=lambda message: True)
def Manejo_Eliminacion_Usuario(message):
	global lista_prueba, nombre, lista_en_string
	chat_id = message.chat.id
	usr_text = message.text
	#IDHuella = ""
	if chat_id in user_data:
		step = user_data[chat_id]
		if step == 1:
			bot.send_message(chat_id, "Dime el nombre del propietario que deseas eliminar.")
			user_data[chat_id] = 2
		elif step == 2:
			nombre = usr_text
			print(nombre)
			bot.send_message(chat_id, "Dime que numero de huella desesas eliminar. Escribe (.) para eliminar todos")
			user_data[chat_id] = 3
		elif step == 3:
			#bot.send_message(chat_id, "Entrando al step 3")
			texto = usr_text
			list_len = len(lista_prueba)
			for item in lista_prueba[:]:
				print("Item: ", item.nombre)
				print("ID: ", item.IDHuella)
				if item.nombre == nombre:
					print("Entrando al ciclo if de nombre con texto: ", texto)
					if item.IDHuella == texto:
						lista_prueba.remove(item)
						bot.send_message(chat_id, f"Se elimino huella No. {texto} de: {nombre}")
						lista_en_string = '\n'.join([f"Nombre: {item.nombre}, ID de Huella: {item.IDHuella}" for item in lista_prueba])
					elif texto == ".":
						print("Entrando a elif")
						lista_prueba.remove(item)
						bot.send_message(chat_id, f"Se elimino huella No. {item.IDHuella} de: {nombre}")
						lista_en_string = '\n'.join([f"Nombre: {item.nombre}, ID de Huella: {item.IDHuella}" for item in lista_prueba])

			#bot.send_message(chat_id, f"Se eliminaron huellas de: {nombre}")
			#lista_en_string = '\n'.join([f"Nombre: {item.nombre}, ID de Huella: {item.IDHuella}" for item in lista_prueba])
			user_data.pop(chat_id)


if __name__ == '__main__':
	print("Activando a Cecil")
	bot.infinity_polling()
