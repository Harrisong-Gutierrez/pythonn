import turtle
import time
import random

# Configuración de la pantalla
ancho = 600
alto = 600
ventana = turtle.Screen()
ventana.title("Snake Game")
ventana.bgcolor("black")
ventana.setup(ancho, alto)
ventana.tracer(0)  # Desactivar actualizaciones automáticas de pantalla

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Segmentos del cuerpo de la serpiente
segmentos = []

# Funciones
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def mover():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")


while True:
    ventana.update()

    if cabeza.xcor() > ancho/2 - 10 or cabeza.xcor() < -ancho/2 + 10 or cabeza.ycor() > alto/2 - 10 or cabeza.ycor() < -alto/2 + 10:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        
     
        for segmento in segmentos:
            segmento.goto(1000, 1000)
        
 
        segmentos.clear()


    if cabeza.distance(comida) < 20:
        x = random.randint(-ancho/2 + 10, ancho/2 - 10)
        y = random.randint(-alto/2 + 10, alto/2 - 10)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)


    total_segmentos = len(segmentos)
    for index in range(total_segmentos - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if total_segmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mover()


    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"
            
        
            for segmento in segmentos:
                segmento.goto(1000, 1000)
            
  
            segmentos.clear()

    time.sleep(0.1)  