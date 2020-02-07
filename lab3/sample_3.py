import math
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


# n - quantity of sides in regular n-sided polygon
# r - radius of sun
# R - radius of rays
# x0, y0 - coordinates of centre of sun & rays

def sun_and_rays(x0, y0, n, r, R):
    alpha = 2 * math.pi / n     # angle AOB (where AB - side of regular n-sided polygon, O - zero axis point)
    points = []                 # coordinates' list for vertices of n-sided regular polygon  

    # sun
    penColor('yellow')
    penSize(1)
    brushColor('yellow')
    circle(x0, y0, r)


    # rays based on
    # regular n-sided polygon (starting vertice is on OY axis)
    # starting point on OY axis
    x, y = x0, y0 - r
    points.append((x, y))


    # odd sides case
    if n % 2 == 1:
        n1 = n // 4                 # quantity of points in 1st & 2nd quarters
        n2 = n // 2 - n1            # quantity of points in 3rd & 4th quarters
        
        
        # vertices' coordinates for 1st quarter
        i = 1
        while i - 1 < n1:
            x, y = x0 + r * math.cos(math.pi / 2 - i * alpha), y0 - r * math.cos(i * alpha)
            points.append((x, y))
            i -= 1
            x, y = x0 + R * math.cos(math.pi / 2 - (alpha / 2 + i * alpha)), y0 - R * math.cos(alpha / 2 + i * alpha)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]
            i += 2

        # vertices' coordinates for 4th quarter
        i = n2
        while i > 0:
            i -= 1
            x, y = x0 + r * math.cos(math.pi / 2 - (alpha / 2 + i * alpha)), y0 + r * math.cos(alpha / 2 + i * alpha)
            points.append((x, y))
            x, y = x0 + R * math.cos(math.pi / 2 - (alpha + i * alpha)), y0 + R * math.cos(alpha + i * alpha)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]

        # vertices' coordinates for 3rd quarter
        i = 0
        while i < n2:
            x, y = x0 - r * math.cos(math.pi / 2 - (alpha / 2 + i * alpha)), y0 + r * math.cos(alpha / 2 + i * alpha)
            points.append((x, y))
            x, y = x0 - R * math.cos(math.pi / 2 - i * alpha), y0 + R * math.cos(i * alpha)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]
            i += 1

        # vertices' coordinates for 2nd quarter
        i = n1 + 1
        while i > 0:
            i -= 1
            x, y = x0 - r * math.cos(math.pi / 2 - i * (alpha)), y0 - r * math.cos(i * (alpha))
            points.append((x, y))
            x, y = x0 - R * math.cos(math.pi / 2 - (alpha / 2 + i * alpha)), y0 - R * math.cos(alpha / 2 + i * alpha)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]

        n1 = 0
        n2 = 0
        i = 0
        
    # aliquot 4 sides case
    elif n % 4 == 0:
        # 4 vertices are on axis
        # quantity of vertices in each quarter
        n1 = (n - 4) / 4                

        # vertices' coordinates for 1st quarter
        i = 1
        while i <= n1:
            x, y = x0 + r * math.cos(math.pi / 2 - i * alpha), y0 - r * math.cos(i * alpha)
            points.append((x, y))
            x, y = x0 + R * math.cos(math.pi / 2 - (i * alpha - alpha / 2)), y0 - R * math.cos(i * alpha - alpha / 2)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]
            i += 1

        # coordinates of vertice on axe X between 1st & 4th quarters
        x, y = x0 + r, y0
        points.append((x, y))
        x, y = x0 + R * math.cos(alpha / 2), y0 - R * math.cos(math.pi / 2 - alpha / 2)
        points.append((x, y))
        points.append(points[0])
        polygon(points)
        points = [points[1]]

        # vertices' coordinates for 4th quarter
        i = n1
        while i > 0:
            x, y = x0 + r * math.cos(math.pi / 2 - i * alpha), y0 + r * math.cos(i * alpha)
            points.append((x, y))
            x, y = x0 + R * math.cos(math.pi / 2 - i * alpha - alpha / 2), y0 + R * math.cos(i * alpha + alpha / 2)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]
            i -= 1

        # coordinates of vertice on axe Y between 4th & 3rd quarters
        x, y = x0, y0 + r
        points.append((x, y))
        x, y = x0 + R * math.cos(math.pi / 2 - alpha / 2), y0 + R * math.cos(alpha / 2)
        points.append((x, y))
        points.append(points[0])
        polygon(points)
        points = [points[1]]

        # vertices' coordinates for 3rd quarter
        i = 0
        while i <= n1:
            x, y = x0 - r * math.cos(math.pi / 2 - i * alpha), y0 + r * math.cos(i * alpha)
            points.append((x, y))
            x, y = x0 - R * math.cos(math.pi / 2 - (i * alpha - alpha / 2)), y0 + R * math.cos(i * alpha - alpha / 2)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]
            i += 1

        # coordinates of vertice on axe X between 3rd & 2nd quarters
        x, y = x0 - r, y0
        points.append((x, y))
        x, y = x0 - R * math.cos(alpha / 2), y0 + R * math.cos(math.pi /2 - alpha / 2)
        points.append((x, y))
        points.append(points[0])
        polygon(points)
        points = [points[1]]

        # vertices' coordinates for 2nd quarter
        i = n1
        while i > 0:
            x, y = x0 - r * math.cos(math.pi / 2 - i * alpha), y0 - r * math.cos(i * alpha)
            points.append((x, y))
            x, y = x0 - R * math.cos(math.pi / 2 - i * alpha - alpha / 2), y0 - R * math.cos(i * alpha + alpha / 2)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]
            i -= 1

        # coordinates of vertice on axe Y between 2nd & 1st quarters
        x, y = x0, y0 - r
        points.append((x, y))
        x, y = x0 - R * math.cos(math.pi / 2 - alpha / 2), y0 - R * math.cos(alpha / 2)
        points.append((x, y))
        points.append(points[0])
        polygon(points)
        points = [points[1]]

        n1 = 0
        i = 0

    # even sides case
    else:
        # 2 vertices are on axe Y
        # quantity of verticess in each quarter
        n1 = (n - 2) / 4                

        # vertices' coordinates for 1st quarter
        i = 1
        while i <= n1:
            x, y = x0 + r * math.cos(math.pi / 2 - i * alpha), y0 - r * math.cos(i * alpha)
            points.append((x, y))
            x, y = x0 + R * math.cos(math.pi / 2 - (i * alpha - alpha / 2)), y0 - R * math.cos(i * alpha - alpha / 2)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]
            i += 1

        # vertices' coordinates for 4th quarter
        i = n1
        while i > 0:
            x, y = x0 + r * math.cos(math.pi / 2 - i * alpha), y0 + r * math.cos(i * alpha)
            points.append((x, y))
            x, y = x0 + R * math.cos(math.pi / 2 - (i * alpha + alpha / 2)), y0 + R * math.cos(i * alpha + alpha / 2)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]
            i -= 1

        # coordinates of vertice on axe Y between 4th & 3rd quarters
        x, y = x0, y0 + r
        points.append((x, y))
        x, y = x0 + R * math.cos(math.pi / 2 - alpha / 2), y0 + R * math.cos(alpha / 2)
        points.append((x, y))
        points.append(points[0])
        polygon(points)
        points = [points[1]]

        # vertices' coordinates for 3rd quarter
        i = 0
        while i <= n1:
            x, y = x0 - r * math.cos(math.pi / 2 - i * alpha), y0 + r * math.cos(i * alpha)
            points.append((x, y))
            x, y = x0 - R * math.cos(math.pi / 2 - (i * alpha - alpha / 2)), y0 + R * math.cos(i * alpha - alpha / 2)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]
            i += 1

        # vertices' coordinates for 2nd quarter
        i = n1
        while i > 0:
            x, y = x0 - r * math.cos(math.pi / 2 - i * alpha), y0 - r * math.cos(i * alpha)
            points.append((x, y))
            x, y = x0 - R * math.cos(math.pi / 2 - (i * alpha + alpha / 2)), y0 - R * math.cos(i * alpha + alpha / 2)
            points.append((x, y))
            points.append(points[0])
            polygon(points)
            points = [points[1]]
            i -= 1

        # coordinates of vertice on axe Y between 2nd & 1st quarters
        x, y = x0, y0 - r
        points.append((x, y))
        x, y = x0 - R * math.cos(math.pi / 2 - alpha / 2), y0 - R * math.cos(alpha / 2)
        points.append((x, y))
        points.append(points[0])
        polygon(points)
        points = [points[1]]

        n1 = 0
        i = 0


sun_and_rays(450, 50, 33, 30, 45)


# waves blue
for x in range(25, 500, 100):
    penColor('blue')
    penSize(1)
    brushColor('blue')
    circle(x, 295, 25)


# waves yellow
for x in range(75, 500, 100):
    penColor('yellow')
    penSize(1)
    brushColor('yellow')
    circle(x, 305, 25)


# clouds 1
penColor('grey')
penSize(1)
brushColor('white')

i = 0
x = 150
radius = 15
while i < 3: 
    circle(x, 50, 15)
    x += 20
    i += 1    

i = 0
x = 140
radius = 15
while i < 4: 
    circle(x, 70, 15)
    x += 20
    i += 1    


# clouds 2
penColor('grey')
penSize(2)
brushColor('white')

circle(280, 26, 25)
circle(310, 26, 25)
circle(340, 26, 25)

circle(260, 56, 25)
circle(290, 56, 25)
circle(320, 56, 25)
circle(350, 56, 25)


# clouds 3
penColor('grey')
penSize(1)
brushColor('white')

circle(50, 105, 25)
circle(80, 105, 25)
circle(110, 105, 25)

circle(30, 135, 25)
circle(60, 135, 25)
circle(90, 135, 25)
circle(120, 135, 25)


# boat big
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


# boat small
penColor('black')
penSize(1)
brushColor('brown')
circle(140, 220, 10)

penColor('blue')
penSize(1)
brushColor('blue')
rectangle(130, 210, 150, 220)

penColor('black')
penSize(1)
brushColor('brown')
line(130, 220, 220, 220)
rectangle(140, 220, 220, 230)
polygon([(220, 220), (240, 220), (220, 230), (220, 220)])

penColor('black')
penSize(2)
brushColor('white')
circle(225, 223, 3)

penColor('black')
penSize(1)
brushColor('black')
rectangle(179, 150, 181, 220)

penColor('black')
penSize(1)
brushColor('white')
polygon([(181, 150), (280, 185), (190, 185), (181, 150)])
polygon([(181, 220), (280, 185), (190, 185), (181, 220)])


# sunshade big
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


# sunshade small
penColor('brown')
penSize(1)
brushColor('brown')
rectangle(170, 300, 172, 380)

penColor('black')
penSize(1)
brushColor('brown')

i = 0
x = 130
while i < 4:
    polygon([(170, 300), (170, 320), (x, 320), (170, 300)])
    x += 10
    i += 1

i = 0
x = 172 + 40
while i < 4:
    polygon([(172, 300), (172, 320), (x, 320), (172, 300)])
    x -= 10
    i += 1


run()
