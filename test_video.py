import glob
import os
import time
import ST7789
import sys 
import cv2
import numpy as np
from PIL import Image
print("""
test_video.py - Display a video on the LCD.
""")

display_type = "square"

# Create ST7789 LCD display class.

if display_type in ("square", "rect", "round"):
    disp = ST7789.ST7789(
        height=135 if display_type == "rect" else 240,
        rotation=180,
        port=1,
        cs=0,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
        dc=7,
        backlight=5,               # 18 for back BG slot, 19 for front BG slot.
        rst=8,
        spi_speed_hz=80000000,
        offset_left=0 if display_type == "square" else 40,
        offset_top=53 if display_type == "rect" else 0
    )

else:
    print ("Invalid display type!")

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

WIDTH = disp.width
HEIGHT = disp.height
disp.set_backlight(1)

video_file = "/home/zhangtianyu/Videos/bad_apple.mp4"
output_dir = "/home/zhangtianyu/Videos/bad_apple_frames"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# first frame

#cap = cv2.VideoCapture(video_file)
#success, frame = cap.read()
#i = 0
#while success:
#    print(i)
#    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#    frame = frame[:,420:1500,:]
#    frame = cv2.resize(frame,(240,240))
#    cv2.imwrite(output_dir+"/{:08d}.jpg".format(i),frame)
#    i+=1
#    success, frame = cap.read()
#exit()

i = 0
frames = glob.glob(output_dir+"/*.jpg")
frames.sort()
L = len(frames)
while i<L:
    image = Image.open(frames[i])
    bg =(0,0,0)
    disp.display(image)
    print(i,time.time())
    i+=1
# Initialize display.
#disp.begin()
# Load an image.
#disp.display(image)
