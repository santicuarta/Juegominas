import turtle
import time
import random

#Clase de la ventana
class Screen():


    def __init__(self, ancho, alto, titulo, fondoColor, juego):
        self.ventana = turtle.Screen()
        self.ventana.title(titulo)
        self.ventana.bgcolor(fondoColor)
        self.ventana.bgpic("img/FondoJuego.gif")
        self.ventana.setup(width = ancho, height = alto)
        self.ventana.tracer(0)

        #REGISTRAR IMAGENES
        self.ventana.register_shape("img/Comida.gif")
        self.ventana.register_shape("img/FondoJuego.gif")
        self.ventana.register_shape('img/abanave.gif')
        self.ventana.register_shape('img/Naveespacial.gif')
        self.ventana.register_shape('img/izqnave.gif')
        self.ventana.register_shape('img/dernave.gif')

        #Configuro boton de cerrar
        canvas = self.ventana.getcanvas()
        root = canvas.winfo_toplevel()
        def on_close():
            juego.running = False
        root.protocol("WM_DELETE_WINDOW", on_close)

    #Metodo para el espacio de juego
    def setArena(self, lado, colorBorde, cuadricula=False):
        self.lado = lado
        self.colorBorde=colorBorde

        arena = turtle.Turtle()
        arena.speed(0) 
        arena.penup()
        arena.hideturtle()
        arena.color(colorBorde)
        arena.goto(-(self.lado/2),-(self.lado/2))
        arena.pendown()
        arena.color(colorBorde)
        for i in range(4):
            arena.forward(self.lado)
            arena.left(90)

        for i in range(int(self.lado/50)):
            arena.goto(-(self.lado/2),-(self.lado/2)+50*i)
            arena.pendown()
            arena.forward(self.lado)
            arena.penup()
        
        arena.left(90)

        for i in range(int(self.lado/50)):
            arena.goto(-(self.lado/2)+50*i,-(self.lado/2))
            arena.pendown()
            arena.forward(self.lado)
            arena.penup()
        """"
        arena.goto(-(self.lado/2),-(self.lado/2))
        arena.pendown()
        arena.color(colorBorde)
        for i in range(4):
            arena.forward(self.lado)
            arena.left(90)

        for i in range(int(self.lado/50)):
            arena.goto(-(self.lado/2),-(self.lado/2)+50*i)
            arena.pendown()
            arena.forward(self.lado)
            arena.penup()
        
        arena.left(90)

        for i in range(int(self.lado/50)):
            arena.goto(-(self.lado/2)+50*i,-(self.lado/2))
            arena.pendown()
            arena.forward(self.lado)
            arena.penup()
        """
        self.ventana.update()
