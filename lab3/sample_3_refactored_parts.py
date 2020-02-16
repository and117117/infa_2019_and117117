from sample_3_refactored_rays_math import *


def sky(w_x, w_y, w_width, w_height):
    """Draw sky
        sky_x, sky_y - sky starting point
    """
    sky_width = w_width
    sky_height = w_height / 3
    sky_x = w_x
    sky_y = w_y

    penColor('cyan')
    penSize(1)
    brushColor('cyan')
    rectangle(sky_x, sky_y, sky_x + sky_width, sky_y + sky_height)

def sea(w_x, w_y, w_width, w_height):
    """Draw sea
        sea_x, sea_y - sea starting point
    """
    sea_width = w_width
    sea_height = w_height / 3
    sea_x = w_x
    sea_y = w_y + w_height /3
    
    penColor('blue')
    penSize(1)
    brushColor('blue')
    rectangle(sea_x, sea_y, sea_x + sea_width, sea_y + sea_height)

def sand(w_x, w_y, w_width, w_height):
    """Draw sand
        sand_x, sand_y - sand starting point
    """
    sand_width = w_width
    sand_height = w_height / 3
    sand_x = w_x
    sand_y = w_y + w_height /3 * 2
    
    penColor('yellow')
    penSize(1)
    brushColor('yellow')
    rectangle(sand_x, sand_y, sand_x + sand_width, sand_y + sand_height)

def waves(w_x, w_y, w_width, w_height):
    """Draw waves"""
    # blue waves
    y_sand_line = w_y + w_height / 3 * 2 - 1
    
    for x in range(0, 500, 100):
        penColor('blue')
        penSize(1)
        brushColor('blue')

        arc(x, y_sand_line - 10, x + 50, y_sand_line + 10, 180, 360, 'chord')

    # yellow waves
    y_sand_line += 2
    for x in range(50, 500, 100):
        penColor('yellow')
        penSize(1)
        brushColor('yellow')

        arc(x, y_sand_line - 10, x + 50, y_sand_line + 10, 0, 180, 'chord')

def clouds(x_clouds, y_clouds, height_clouds, width_to_height_ratio_clouds):
    """Draw clouds"""
    penColor('grey')
    penSize(1)
    brushColor('white')

    i = 0
    x = x_clouds
    y = y_clouds
    h = height_clouds
    w = height_clouds * width_to_height_ratio_clouds
    while i < 3: 
        oval(x, y, x + w, y + h)
        x += w / 2
        i += 1    

    i = 0
    x = x_clouds - w / 4
    y = y_clouds + h / 2
    while i < 4: 
        oval(x, y, x + w, y + h)
        x += w / 2
        i += 1    

def boat(x_boat, y_boat, height_boat):
    """Draw boat
        x_boat, y_boat - boat's starting point, boat's bow
        height_boat - height of boat's hull
    """
    penColor('black')
    penSize(1)
    brushColor('brown')
    
    arc(x_boat, y_boat - height_boat, 
        x_boat + height_boat * 2, y_boat + height_boat, 
        180, 270, 'pieslice')
    rectangle(x_boat + height_boat, y_boat, 
        x_boat + height_boat * 5, y_boat + height_boat)
    polygon([(x_boat + height_boat * 5, y_boat), 
        (x_boat + height_boat * 7, y_boat), 
        (x_boat + height_boat * 5, y_boat + height_boat), 
        (x_boat + height_boat * 5, y_boat)])

    penSize(3)
    brushColor('white')
    circle(x_boat + height_boat * 5.5, y_boat + height_boat / 2.6, 
        height_boat / 4)

    penSize(1)
    brushColor('black')
    rectangle(x_boat + height_boat * 2, y_boat, 
        x_boat + height_boat * 2 + height_boat / 5, y_boat - height_boat * 4)

    brushColor('white')
    polygon([(x_boat + height_boat * 2 + height_boat / 5, y_boat - height_boat * 4), 
        (x_boat + height_boat * 7, y_boat - height_boat * 2), 
        (x_boat + height_boat * 3, y_boat - height_boat * 2), 
        (x_boat + height_boat * 2 + height_boat / 5, y_boat - height_boat * 4)])
    polygon([(x_boat + height_boat * 2 + height_boat / 5, y_boat), 
        (x_boat + height_boat * 7, y_boat - height_boat * 2), 
        (x_boat + height_boat * 3, y_boat - height_boat * 2), 
        (x_boat + height_boat * 2 + height_boat / 5, y_boat)])

def sunshade(x_sunshade, y_sunshade, height_sunshade):
    """Draw sunshade"""
    penColor('brown')
    penSize(1)
    brushColor('brown')
    
    rectangle(x_sunshade, y_sunshade, 
        x_sunshade + height_sunshade // 20, y_sunshade - height_sunshade)

    penColor('black')
    penSize(1)
    brushColor('brown')

    i = 0
    x = height_sunshade // 6 * 4
    while i < 4:
        polygon([(x_sunshade, y_sunshade - height_sunshade),
            (x_sunshade, y_sunshade - height_sunshade + height_sunshade // 5), 
            (x_sunshade - x, y_sunshade - height_sunshade + height_sunshade // 5),
            (x_sunshade, y_sunshade - height_sunshade)])
        x -= height_sunshade // 6
        i += 1

    i = 0
    x = height_sunshade // 6 * 4
    while i < 4:
        polygon([(x_sunshade + height_sunshade // 20, y_sunshade - height_sunshade), 
            (x_sunshade  + height_sunshade // 20, y_sunshade - height_sunshade + height_sunshade // 5), 
            (x_sunshade + height_sunshade // 20 + x, y_sunshade - height_sunshade + height_sunshade // 5), 
            (x_sunshade + height_sunshade // 20, y_sunshade - height_sunshade)])
        x -= height_sunshade // 6
        i += 1

def sun(x0, y0, r):
    """Draw sun"""
    penColor('yellow')
    penSize(1)
    brushColor('yellow')
    circle(x0, y0, r)


def rays(x0, y0, n, r, R):
    """Draw rays based on
        regular n-sided polygon 
        starting vertice is on OY axis
        starting point on OY axis
        alpha - angle AOB (where AB - side of regular n-sided polygon, O - zero axis point)
        points - coordinates' list for vertices of n-sided regular polygon
    """
    if n % 2 == 1:
        odd_sides_case(x0, y0, n, r, R)

    elif n % 4 == 0:
        alliqot_4_sides_case(x0, y0, n, r, R)

    else:
        even_sides_case(x0, y0, n, r, R)

def sun_and_rays(x0, y0, n, r, R):
    """Draw sun with rays
        x0, y0 - coordinates of centre of sun & rays
        n - quantity of sides in regular n-sided polygon
        r - radius of sun
        R - radius of rays
    """
    sun(x0, y0, r)
    rays(x0, y0, n, r, R)
