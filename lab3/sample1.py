from graph import *

# main face circle
penColor('black')
penSize(1)
brushColor('yellow')
circle(200, 200, 100)

# eyes
penColor('black')
penSize(1)
brushColor('red')
circle(150, 170, 22)

penColor('black')
penSize(1)
brushColor('red')
circle(250, 170, 18)

penColor('black')
penSize(1)
brushColor('black')
circle(150, 170, 8)

penColor('black')
penSize(1)
brushColor('black')
circle(250, 170, 8)

# mouth
penColor('black')
penSize(20)
line(150, 260, 250, 260)

# eyebrows
penColor('black')
penSize(10)
line(210, 170, 290, 120)

penColor('black')
penSize(10)
line(90, 110, 190, 170)

run()