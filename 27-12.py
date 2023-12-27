from turtle import Turtle,onscreenclick, onkey, listen, Screen
leo = Turtle ()
tela = Screen()
leo.speed(0)
resultado = 0
numero = 0

def trocar ():
    global resultado
    global numero
    numero = numero + 1
    resultado = numero % 2

leo.pensize(5)
leo.forward(100)
leo.backward(100)
leo.right(90)
leo.forward(100)
leo.left(180)
leo.forward(100)
leo.forward(100)
leo.backward(100)
leo.left(90)
leo.forward(100)
leo.left(180)
leo.forward(200)
leo.left(90)
leo.forward(100)
leo.backward(100)
leo.right(90)
leo.forward(100)
leo.backward(100)
leo.right(90)
leo.forward(100)
leo.right(90)
leo.forward(200)
leo.backward(300)
leo.forward(100)
leo.left(90)
leo.forward(100)
leo.backward(100)
leo.right(90)
leo.forward(100)
leo.left(90)
leo.forward(100)

def jogar(x, y): 
    leo.penup()
    leo.goto(x - (x % 100) + 50, y - (y % 100) + 50)
    if resultado == 0:
        x2()
    if resultado == 1:
        circulo()
    trocar()

def circulo():
    leo.pensize(10)
    leo.color('blue')
    leo.right(90)
    leo.forward(40)
    leo.left(90)
    r = 40
    leo.pendown()
    leo.circle(r)

def x2():
    leo.pensize(15)
    leo.color('red')
    leo.pendown()
    leo.right(45)
    for _ in range(4):
        leo.forward(50)
        leo.forward(-50)
        leo.right(90)
    leo.left(45)
    

tela.onscreenclick(jogar)

listen()
tela.mainloop()