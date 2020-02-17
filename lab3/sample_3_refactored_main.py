from sample_3_refactored_parts import *


# w_x, w_y - window starting point
# w_width, w_height - window width & height
w_x = 0
w_y = 0
w_width = 500
w_height = 600

def main():
    """Draw whole picture"""
    windowSize(w_width, w_height)
    
    sky(w_x, w_y, w_width, w_height)
    sea(w_x, w_y, w_width, w_height)
    sand(w_x, w_y, w_width, w_height)
    waves(w_x, w_y, w_width, w_height)
    clouds_1 = clouds(50, 40, 30, 1.5)
    clouds_2 = clouds(200, 10, 50, 1)
    clouds_3 = clouds(20, 110, 25, 2)
    boat_1 = boat(250, 300, 30)
    boat_2 = boat(100, 220, 18)
    sunshade(120, 500, 180)
    sunshade(250, 480, 100)
    sun_and_rays(450, 50, 14, 30, 45)


main()

run()
