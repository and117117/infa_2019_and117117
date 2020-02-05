from graph import *

# sky
penColor('cyan')
penSize(1)
brushColor('cyan')
rectangle(0, 0, 500, 200)

# sea
penColor('blue')
penSize(1)
brushColor('blue')
rectangle(0, 200, 500, 300)

# sand
penColor('yellow')
penSize(1)
brushColor('yellow')
rectangle(0, 300, 500, 450)

# sun
penColor('grey')
penSize(1)
brushColor('yellow')
circle(450, 50, 30)

# clouds
penColor('grey')
penSize(1)
brushColor('white')
circle(150, 50, 15)
circle(170, 50, 15)
circle(190, 50, 15)
circle(140, 70, 15)
circle(160, 70, 15)
circle(180, 70, 15)
circle(200, 70, 15)

# boat
penColor('black')
penSize(1)
brushColor('brown')
circle(250, 240, 20)

penColor('blue')
penSize(1)
brushColor('blue')
rectangle(230, 220, 270, 240)

penColor('black')
penSize(1)
brushColor('brown')
line(230, 240, 250, 240)
rectangle(250, 240, 400, 260)
polygon([(400, 240), (440, 240), (400, 260), (400, 240)])

penColor('black')
penSize(3)
brushColor('white')
circle(410, 246, 5)

penColor('black')
penSize(1)
brushColor('black')
rectangle(323, 120, 327, 240)

penColor('black')
penSize(1)
brushColor('white')
polygon([(327, 120), (480, 180), (350, 180), (327, 120)])
polygon([(327, 240), (480, 180), (350, 180), (327, 240)])

# sunshade
penColor('brown')
penSize(1)
brushColor('brown')
rectangle(100, 250, 104, 420)

penColor('black')
penSize(1)
brushColor('brown')

i = 0
x = 20
while i < 4:
    polygon([(100, 250), (100, 280), (x, 280), (100, 250)])
    x += 20
    i += 1

i = 0
x = 184
while i < 4:
    polygon([(104, 250), (104, 280), (x, 280), (104, 250)])
    x -= 20
    i += 1

run()
