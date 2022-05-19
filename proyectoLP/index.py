
#-----------------------------------------MAIN-----------------------------------------#
import turtle
import time
import random
import Game2 as g
import Screen as s
import Rabbit as ser
import Comida as c
#-------------------------------------Serial-------------------------------------------#
#import serial, time, json
#hw_sensor = serial.Serial(port='COM3', baudrate=9600, timeout=1, write_timeout=1)
#raw_string_j = json.loads('{"x":"0","y":"0"}')
#---------------------------------------------------------------------------------------

# Instancia de Game
juego = g.Game(0.2)
juego.puntaje("white")
pos=[["1","1","1","1","1","1","1"],
     ["1","0","0","0","0","0","1"],
     ["1","0","0","0","0","0","1"],
     ["1","0","0","0","0","0","1"],
     ["1","0","0","0","0","0","1"],
     ["1","0","0","0","0","0","1"],
     ["1","1","1","1","1","1","1"]]
posx=3
posy=3
n=len(pos)
size=n*50
# Instancia de Screen
ventana = s.Screen(600,600,"Snake", "black", juego)
ventana.setArena(size,"white",False)

# Instancia de Serpiente
snake = ser.Serpiente("white","#834827",size,posx,posy)
snake.controles(ventana.ventana,"Up","Down", "Left", "Right")

# Instancia de comida
comida = c.Comida("blue",ventana,size)
comida.posMin(pos)
# Loop Principal
while juego.running:
#----------------------JOYSTIC-------------------------------------
    """raw_string_b = hw_sensor.readline()
    raw_string_s = raw_string_b.decode('utf-8')
    if(len(raw_string_s)>0):
            raw_string_j = json.loads(raw_string_s)"""
#-----------------------------------------------------------------------

    # Actualizacuón de la ventana
    ventana.ventana.update()
    # Comprueba la bandera de perder
    if juego.perder:
        juego.alPerder(snake)
#-----------------------------------------------------
    # Comprueba si colisionó con la comida
    if comida.alColisionar(snake, pos):
        juego.alPerder(snake)
#--------------------------------------------------
    # Mueve el cuerpo de la serpiente
    snake.moverCuerpo()

    # Mueve la cabeza de la serpiente
    snake.movimiento(juego,ventana)

    # Comprueba si la serpiente colisionó consigo misma
    snake.colision(juego)

    # Delay para regular la velocidad de juego
    time.sleep(juego.delay)
