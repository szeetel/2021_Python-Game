import tkinter
import turtle,time, sys, os, keyboard, random
from concurrent.futures import ThreadPoolExecutor
from tkinter import *

screen = turtle.Screen()
screen.delay(1/50)
screen.setup(1080,720)
screen.setworldcoordinates(0,0,500,500)
screen.title('Hard')
screen.bgcolor('white')
screen.cv._rootwindow.resizable(False, False)

screen.register_shape('background.gif')

backgroun = turtle.Turtle()
backgroun.shape('background.gif')
backgroun.penup()
backgroun.setposition(250,80)

human = turtle.Turtle()
human.shape('circle')
human.shapesize(0.5)
human.penup()
human.setposition(250,250)
human.speed(0)
human.color('black','white')

another = turtle.Turtle()
another.shape("triangle")
another.penup()
another.setposition(100,100)
another.color('black','red')

t = 0
timee = turtle.Turtle()
timee.hideturtle()
timee.penup()
timee.setposition(460, 460)

score = turtle.Turtle()
score.hideturtle()
score.penup()
score.setposition(430, 460)

healthc = turtle.Turtle()
healthc.hideturtle()
healthc.penup()
healthc.setposition(400, 460)
globals()['health'] = 100
healthc.write(globals()['health'], font=("Courier", 12, "normal"))

titleh = turtle.Turtle()
titleh.hideturtle()
titleh.penup()
titleh.setposition(400,480)
titleh.write("Health  Score   Time",font=('Courier',12,'normal'))

loot = turtle.Turtle()
loot.penup()
loot.setposition(random.randint(5,495),random.randint(5,245))
loot.shapesize(2)
loot.shape('square')
loot.color('black','orange')
globals()['counter'] = 0

def lose():
    if globals()['health'] <= 0:
        tkinter.messagebox.showinfo("",'You Lose!')
        screen.bye()
def healthy():
    hx, hy, ax, ay = human.xcor(), human.ycor(), another.xcor(), another.ycor()
    if abs(hx-ax) <= 10 and abs(hy-ay) <= 10:
        globals()['health'] -= 1
        healthc.clear()
        healthc.write(int(globals()['health']), font=("Courier", 12, "normal"))

def looter():
    hx,hy,ax,ay = human.xcor(),human.ycor(),loot.xcor(),loot.ycor()
    if abs(hx-ax) <= 10 and abs(hy-ay) <= 10:
        loot.setposition(random.randint(5,495),random.randint(5,245))
        globals()['counter'] += 1
        score.clear()
        score.write(globals()['counter'], font=("Courier", 12, "normal"))


def character():
    step = 2
    lx = human.xcor()
    ly = human.ycor()
    if keyboard.is_pressed('w'): human.sety(ly + step),
    if keyboard.is_pressed('a'): human.setx(lx - step),
    if keyboard.is_pressed('s'): human.sety(ly - step),
    if keyboard.is_pressed('d'): human.setx(lx + step),
    if keyboard.is_pressed('esc'):
        sys.exit()
        os.exit()
        screen.destroy
def boundaries():
    ny = human.ycor()
    nx = human.xcor()
    if nx <= 0: human.setx(0)
    if nx >= 500: human.setx(500)
    if ny >= 500: human.sety(500)
    if ny <= 0: human.sety(0)

def enemy():
    another.setheading(another.towards(human))
    another.forward(0.5)

def clock():
    clock = time.perf_counter()  # measer time in 1/60 seconds
    timee.clear()
    timee.write(int(clock), font=("Courier", 12, "normal"))

def main():
    while True:
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.submit(character())
            executor.submit(boundaries())
            executor.submit(enemy())
            executor.submit(clock())
            executor.submit(looter())
            executor.submit(healthy())
            executor.submit(lose())
    screen.mainloop()
main()

if __name__ == '__main__':
    main()

