import turtle
import time
import random

# Clase de la comida
class Comida():

    def __init__(self, colorComida, screen,size):
        x=0
        y=0
        if (size/50)%2==0:
            x=-25
            y=-25
        else:
          x=50
          y=50

        self.lado = screen.lado
    def posMin(self,pos):
      #pos=[["1","1","1"],["1","1","1"],["1","0","1"]] 
      sizeMat=len(pos)
      #print(sizeMat)
      for i in range(sizeMat):
        for j in range(sizeMat):
          if pos[i][j]=="1":
            x=j*50-sizeMat*25+25
            y=-i*50+sizeMat*25-25
            self.comida = turtle.Turtle()
            self.comida.speed(0)
            self.comida.shape('img/Comida.gif')
            self.comida.penup()
            self.comida.goto(x,y)
      return True
          
    # Método de cuando la serpiente colisiona con la comida
    def alColisionar(self, serpiente, pos):
      x=serpiente.cabeza.xcor()
      y=serpiente.cabeza.ycor()
      #return pos[serpiente.cabeza.ycor()][serpiente.cabeza.xcor()]=="1"
      sizeMat=len(pos)
      #print(-(serpiente.cabeza.ycor()-50-des)/50,(serpiente.cabeza.xcor()+50+des)/50)
      return pos[int(-(y+25-sizeMat*25)/50)][int((x-25+sizeMat*25)/50)]=="1"
         

