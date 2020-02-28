import sqlite3
from tkinter import *
from random import randint, choice


def main(n):
    """
        \nDraw 
        main window in full screen (root)
        canvas in main window
        n balls
        bind canvas with left mouse click
    """
    global root, canvas
    global root_width, root_height
    global balls, squares
    global score
    score = 0

    root = Tk()

    root_width = root.winfo_screenwidth()
    root_height = root.winfo_screenheight()

    root.geometry('{}x{}'.format(root_width, root_height))

    canvas = Canvas(root)
    canvas.pack(fill = BOTH, expand = 1)
    
    balls = [Ball() for i in range(n)]
    squares = [Square() for i in range(n)]

    canvas.bind('<Button-1>', click)
    
    root.mainloop()


class Ball:
    """\nInitiate ball with movement
        radius - random 20 - 50
        x, y - coordinates of ball's centre (random in canvas)
        dx, dy - move steps
        colors - list of colors, selected randomly
    """
    def __init__(self):
        self.radius = randint(20, 50)
        self.x = randint(0 + self.radius, root_width - self.radius)
        self.y = randint(0 + self.radius, root_height - self.radius)
        self.dx, self.dy = 2, 2
    
        self.colors = ['yellow', 'green', 'grey', 'blue', 'black', 'red', 'magenta']
        
        self.ball_draw()
        self.ball_move()

    def ball_draw(self):
        """
            \nDraw ball
        """
        self.ball = canvas.create_oval(
                                self.x - self.radius, self.y - self.radius, 
                                self.x + self.radius, self.y + self.radius, 
                                fill = choice(self.colors), 
                                width = 0)
    
    def ball_move(self):
        """
            \nMove the ball
            attributes from def __init_
        """
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0 + self.radius or self.x >= root_width - self.radius:
            self.dx = - self.dx
        if self.y <= 0 + self.radius or self.y >= root_height - self.radius:
            self.dy = - self.dy

        canvas.move(self.ball, self.dx, self.dy)
        root.after(50, self.ball_move)
    

class Square:
    """\nInitiate square with movement
        side - random 10 - 20
        x, y - coordinates of left upper square's vertex (random in canvas)
        dx, dy - move steps
        colors - list of colors, selected randomly
    """
    def __init__(self):
        self.side = randint(10, 20)
        self.x = randint(0, root_width - self.side)
        self.y = randint(0, root_height - self.side)
        self.dx, self.dy = 3, 0
    
        self.colors = ['yellow', 'green', 'grey', 'blue', 'black', 'red', 'magenta']
        
        self.square_draw()
        self.square_move()

    def square_draw(self):
        """
            \nDraw square
        """
        self.square = canvas.create_rectangle(
                                self.x, self.y, 
                                self.x + self.side, self.y + self.side, 
                                fill = choice(self.colors), 
                                width = 0)
    
    def square_move(self):
        """
            \nMove the square
            attributes from def __init_
        """
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0 or self.x >= root_width - self.side:
            self.dx = - self.dx
        if self.y <= 0 or self.y >= root_height - self.side:
            self.dy = - self.dy

        canvas.move(self.square, self.dx, self.dy)
        root.after(50, self.square_move)
    

def click(event):
    """ 
        \n:
        ball case:
        XO, YO, hypo - sides of right triangle
        (XO ** 2) + (YO ** 2) = (hypo ** 2)
        Pythagoras' theorem
        if hypo less or equal ball's radius
        then kill the ball from canvas and from balls list

        square case:
        if event x, y (left mouse click)
        more or equal square's x, y (left upper vertex)
        OR 
        less or equal square's x + side, y + side (right down vertex)
        then kill the square from canvas and from squares list

        print score
    """
    global score

    if len(balls) != 0:
        for i in range(len(balls)):
            x = balls[i].x
            y = balls[i].y
            r = balls[i].radius

            XO = x - event.x
            YO = y - event.y
            hypo = (XO ** 2 + YO ** 2) ** 0.5
            
            if hypo <= r:
                canvas.delete(balls[i].ball)
                balls.pop(i)
                
                score += 1
                break
                
    if len(squares) != 0:
        for i in range(len(squares)):
            x = squares[i].x
            y = squares[i].y
            s = squares[i].side

            if x <= event.x <= x + s or y <= event.y <= y + s:
                canvas.delete(squares[i].square)
                squares.pop(i)
                
                score += 2
                break
                
        save_score_to_file(score)

def save_score_to_file(score):
    """
        \nCreate SQLite database 'score'
        table 'score'
        save score to 'score' field
        print score
    """
    conn = sqlite3.connect('a:/a/score.db')
    c = conn.cursor()

    try:
        c.execute("""CREATE TABLE score(score)""")
        conn.commit()
    except:
        None

    c.execute('SELECT * FROM score')
    a = c.fetchall()

    if len(a) == 0:
        c.execute('INSERT INTO score VALUES ({})'.format(score))
    else:
        c.execute('UPDATE score SET score = :score', {'score': score})
    
    conn.commit()

    c.execute('SELECT * FROM score')
    a = c.fetchall()
    print('SCORE:', a[0][0])

    conn.close()


if __name__ == '__main__':
    main(3)
