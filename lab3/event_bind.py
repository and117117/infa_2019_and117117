from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')


canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


colors = ['red', 'orange', 'yellow', 'green', 'blue']
score = 0

def new_ball():
    """ Draw new ball with random coordinates (x, y), random radius, random color
    """
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(1000, new_ball)

def click(event):
    """ xo, yo, hypo - sides of triangle
        (xo ** 2) + (yo ** 2) = (hypo ** 2)
        Pythagoras' theorem
    """
    global score

    xo = x - event.x
    yo = y - event.y
    hypo = (xo ** 2 + yo ** 2) ** 0.5
    
    if hypo <= r:
        score += 1
        print('GOAL', score)
    else:
        score -= 1
        print('MISSED', score)


new_ball()
canv.bind('<Button-1>', click)


root.mainloop()
