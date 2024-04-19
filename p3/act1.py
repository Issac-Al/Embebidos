from gpiozero import LED
from bluedot import BlueDot
from signal import pause
from time import sleep

# Definición de los pines GPIO para cada segmento del display de siete segmentos
# Puedes ajustar estos pines según la configuración de tu display
LEDS = {
    'A': LED(4),
    'B': LED(26),
    'C': LED(5),
    'D': LED(22),
    'E': LED(23),
    'F': LED(24),
    'G': LED(25)
}

# Mapeo de los nombres de los integrantes del equipo a sus respectivos nombres en el display de siete segmentos
nombres_segmentos = {
    'Issac': [['F', 'E'], ['A', 'F', 'G', 'C', 'D'], ['A', 'F', 'G', 'C', 'D'], ['A', 'B', 'C', 'E', 'F', 'G'], ['A'
, 'F', 'E', 'D']],
    'Alexis': [['A', 'B', 'C', 'E', 'F', 'G'], ['F', 'E', 'D'], ['A', 'F', 'E', 'G', 'D'], ['F', 'E', 'G', 'B', 'C'],
['F', 'E'], ['A', 'F', 'G', 'C', 'D']],
    'Ale': [['A', 'B', 'C', 'E', 'F', 'G'], ['F', 'E', 'D'], ['A', 'F', 'E', 'G', 'D']],
    'Fer': [['A', 'F', 'G', 'E'], ['A', 'F', 'E', 'G', 'D'], ['A', 'F', 'E']]
}

# Función para mostrar el nombre en el display de siete segmentos
def mostrar_nombre(nombre):
    for segmento, estado in LEDS.items():
        estado.off()  # Apaga todos los segmentos
    for segmentos in nombres_segmentos.get(nombre, []):
        print("Clave: ", segmentos)
        for segmento in segmentos:
                LEDS[segmento].on()  # Enciende los segmentos necesarios para mostrar el nombre
        sleep(1)
        reiniciar_segmentos()

# Ejemplo de uso

def reiniciar_segmentos():
	for segmento, estado in LEDS.items():
		estado.off()

def dpad(pos):
	if pos.top:
		mostrar_nombre('Issac')
	elif pos.bottom:
		mostrar_nombre('Alexis')
	elif pos.left:
		mostrar_nombre('Ale')
	elif pos.right:
		mostrar_nombre('Fer')

bd = BlueDot()
bd.when_pressed = dpad

pause()
