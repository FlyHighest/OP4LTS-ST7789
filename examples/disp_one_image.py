from st7789_disp.st7789 import ST7789
from st7789_disp.image_tools import *
import time , traceback, os
import sys

path = sys.argv[1]


disp = ST7789(
        height=240,
        rotation=90,
        port=1,
        cs=0,  
        dc=7,
        backlight=5,               
        rst=8,
        spi_speed_hz=40000000,
        offset_left=0 ,
        offset_top= 0
    )
disp.set_backlight(1)

try:
    image = open_image(path)
    image = resize_with_limits(image)
    image = expand2square(image)
    disp.display(image)
except:
    traceback.print_exc()
    print("Done.")
