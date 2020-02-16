import math
from graph import *


def odd_sides_case(x0, y0, n, r, R):
    """Draw rays 
        based on n-sided regular polygon
        n - odd
        n1 - quantity of points in 1st & 2nd quarters
        n2 - quantity of points in 3rd & 4th quarters
    """
    n1 = n // 4
    n2 = n // 2 - n1
    x, y = x0, y0 - r
    alpha = 2 * math.pi / n
    points = []
    points.append((x, y))
    
    
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


def alliqot_4_sides_case(x0, y0, n, r, R):
    """Draw rays
        based on n-sided regular polygon
        n - alliquot 4
        4 vertices are on axis
        n1 - quantity of vertices in each quarter
    """
    n1 = (n - 4) / 4                
    x, y = x0, y0 - r
    alpha = 2 * math.pi / n
    points = []
    points.append((x, y))

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


def even_sides_case(x0, y0, n, r, R):
    """Draw rays
        based on n-sided regular polygon
        n - even
        2 vertices are on axe Y
        n1 - quantity of vertices in each quarter
    """
    n1 = (n - 2) / 4                
    x, y = x0, y0 - r
    alpha = 2 * math.pi / n
    points = []
    points.append((x, y))

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
