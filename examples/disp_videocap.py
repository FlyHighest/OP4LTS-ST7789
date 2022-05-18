from st7789 import ST7789
from image_tools import *
import time , traceback, os
import sys
from PIL import Image

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
    import cv2
    cap = cv2.VideoCapture(0)
    ret,frame = cap.read()
    while ret:
        image = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        image = resize_with_limits(image)
        image = expand2square(image)
        disp.display(image)
        time.sleep(0.1)
        ret,frame = cap.read()
except:
    traceback.print_exc()
    print("Done.")
