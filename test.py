import time
import ST7789
import sys 
from PIL import Image 

print("""
image.py - Display an image on the LCD.
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
        spi_speed_hz=40000000,
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
import glob,random
files = glob.glob("/home/zhangtianyu/Pictures/精选双人照片v2/*g")
image_file = random.choice(files)
image = Image.open(image_file)
w,h=image.size
if w>h:
    image = image.resize((WIDTH, int(h/ (w/WIDTH) ) ))
else:
    image = image.resize((int(w/(h/HEIGHT)),HEIGHT))
bg =(random.randint(0,128),random.randint(0,128),random.randint(0,128))
image = expand2square(image, bg )
print(image_file,bg)
print(time.time())
disp.display(image)
print(time.time())

# Initialize display.
#disp.begin()
# Load an image.
#disp.display(image)
