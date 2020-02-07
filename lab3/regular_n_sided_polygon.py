from graph import *
import math


n = 5                      # quantity of sides in regular n-sided polygon
r = 200                     # radius of sun
R = 150                     # radius of rays
x0, y0 = 200, 200           # centre of sun & rays
alpha = 2 * math.pi / n     # angle AOB (where AB - side of regular n-sided polygon, O - zero axis point)
points = []                 # coordinates' list for vertices of n-sided regular polygon  

# sun
penColor('black')
penSize(1)
brushColor('yellow')
circle(x0, y0, r)


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
        x, y = x0 + r * math.cos(math.pi / 2 - i * (alpha)), y0 - r * math.cos(i * (alpha))
        points.append((x, y))
        i += 1

    # vertices' coordinates for 4th quarter
    i = n2
    while i > 0:
        i -= 1
        x, y = x0 + r * math.cos(math.pi / 2 - (alpha / 2 + i * alpha)), y0 + r * math.cos(alpha / 2 + i * alpha)
        points.append((x, y))

    # vertices' coordinates for 3rd quarter
    i = 0
    while i < n2:
        x, y = x0 - r * math.cos(math.pi / 2 - (alpha / 2 + i * alpha)), y0 + r * math.cos(alpha / 2 + i * alpha)
        points.append((x, y))
        i += 1

    # vertices' coordinates for 2nd quarter
    i = n1 + 1
    while i > 0:
        i -= 1
        x, y = x0 - r * math.cos(math.pi / 2 - i * (alpha)), y0 - r * math.cos(i * (alpha))
        points.append((x, y))

    n1 = 0
    n2 = 0
    i = 0
    
# aliquot 4 sides case
elif n % 4 == 0:
    # 4 vertices are on axis
    # quantity of verticess in each quarter
    n1 = (n - 4) / 4                

    # vertices' coordinates for 1st quarter
    i = 1
    while i <= n1:
        x, y = x0 + r * math.cos(math.pi / 2 - i * (alpha)), y0 - r * math.cos(i * (alpha))
        points.append((x, y))
        i += 1

    # coordinates of vertice on axe X between 1st & 4th quarters
    x, y = x0 + r, y0
    points.append((x, y))

    # vertices' coordinates for 4th quarter
    i = n1
    while i > 0:
        x, y = x0 + r * math.cos(math.pi / 2 - i * alpha), y0 + r * math.cos(i * alpha)
        points.append((x, y))
        i -= 1

    # coordinates of vertice on axe Y between 4th & 3rd quarters
    x, y = x0, y0 + r
    points.append((x, y))

    # vertices' coordinates for 3rd quarter
    i = 0
    while i <= n1:
        x, y = x0 - r * math.cos(math.pi / 2 - i * alpha), y0 + r * math.cos(i * alpha)
        points.append((x, y))
        i += 1

    # coordinates of vertice on axe X between 3rd & 2nd quarters
    x, y = x0 - r, y0
    points.append((x, y))

    # vertices' coordinates for 2nd quarter
    i = n1
    while i > 0:
        x, y = x0 - r * math.cos(math.pi / 2 - i * alpha), y0 - r * math.cos(i * alpha)
        points.append((x, y))
        i -= 1

    # coordinates of vertice on axe Y between 2nd & 1st quarters
    x, y = x0, y0 - r
    points.append((x, y))

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
        x, y = x0 + r * math.cos(math.pi / 2 - i * (alpha)), y0 - r * math.cos(i * (alpha))
        points.append((x, y))
        i += 1

    # vertices' coordinates for 4th quarter
    i = n1
    while i > 0:
        x, y = x0 + r * math.cos(math.pi / 2 - i * alpha), y0 + r * math.cos(i * alpha)
        points.append((x, y))
        i -= 1

    # coordinates of vertice on axe Y between 4th & 3rd quarters
    x, y = x0, y0 + r
    points.append((x, y))

    # vertices' coordinates for 3rd quarter
    i = 0
    while i <= n1:
        x, y = x0 - r * math.cos(math.pi / 2 - i * alpha), y0 + r * math.cos(i * alpha)
        points.append((x, y))
        i += 1

    # vertices' coordinates for 2nd quarter
    i = n1
    while i > 0:
        x, y = x0 - r * math.cos(math.pi / 2 - i * alpha), y0 - r * math.cos(i * alpha)
        points.append((x, y))
        i -= 1

    # coordinates of vertice on axe Y between 2nd & 1st quarters
    x, y = x0, y0 - r
    points.append((x, y))

    n1 = 0
    i = 0

penColor('black')
penSize(1)
brushColor('yellow')
polyline(points)


run()
