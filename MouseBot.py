"""La librería pyautogui de Python proporciona funciones para automatizar la interacción con 
la interfaz gráfica de usuario (GUI) de un sistema operativo. Permite controlar el mouse 
y el teclado para realizar acciones como hacer clic en botones, arrastrar y soltar elementos, 
escribir texto, entre otras."""

import pyautogui as botMouse
import random
import time

while True:
    x = random.randint(400,900)
    y = random.randint(100,700)
    
    botMouse.moveTo(x,y,0.5)
    time.sleep(2)