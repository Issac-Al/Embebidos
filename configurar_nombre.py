from bluedot import BlueDot
from signal import pause
import os

actual_character = 0
adding_characters = True
edit_character = False
name_actual_char = 0
name = ['A']
executing = True
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
		'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
clear = lambda: os.system('clear')
first_edit = True
end = False

def Namepad(pos):
	global actual_character, adding_characters, edit_character, name_actual_char, name, characters, clear, first_edit, end, bd
	#characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'
	#, 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	#clear = lambda: os.system('clear')
	#print(name_actual_char)
	#print(edit_character)
		#clear()
		#print("Name: ", characters[actual_character])
	if pos.top:
		if(adding_characters or edit_character):
			if(actual_character < 25):
				actual_character += 1
				name[name_actual_char] = characters[actual_character]
			else:
				actual_character = 0
				name[name_actual_char] = characters[actual_character]
			Prints()
	elif pos.bottom:
		if(adding_characters or edit_character):
			actual_character -= 1
			name[name_actual_char] = characters[actual_character]
			Prints()
	elif pos.left:
		if(len(name) > 0 and name_actual_char > 0 and not adding_characters):
			edit_character = True
			if(not first_edit):
				name_actual_char -= 1
			else:
				first_edit = False
	elif pos.right:
		if(not adding_characters and not edit_character):
			adding_characters = True
			name_actual_char += 1
			name.append(characters[actual_character])
			Prints()
		elif(edit_character):
			if(name_actual_char < len(name) - 1):
				name_actual_char+=1
			else:
				name_actual_char = 0
	elif pos.middle:
		if(edit_character == True):
			name[name_actual_char] = characters[actual_character]
			name_actual_char = len(name)-1
			edit_character = False
			first_edit = True
		elif(adding_characters == True):
			name[name_actual_char] = characters[actual_character]
			adding_characters = False
			actual_character = 0;
		elif(edit_character == False and adding_characters == False):
			clear()
			print("Se guardo el nombre: ", *name, sep ='');
			bd.when_pressed = dpad
			#end = True

def dpad(pos):
	if pos.top:
		print('top')

def Prints():
	clear()
	print('Insertar nombre: ', *name, sep ='')

bd = BlueDot()
bd.set_when_client_connects(Prints, background=False)
bd.when_pressed = Namepad

pause()



