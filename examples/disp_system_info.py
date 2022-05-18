from st7789_disp.st7789 import ST7789
from st7789_disp.image_tools import *
import time , traceback, os

def get_cpu_temp():
    f = open("/sys/class/thermal/thermal_zone0/temp","r")
    temp = int(f.read())
    return int(temp/1000)

def get_gpu_temp():
    f = open("/sys/class/thermal/thermal_zone1/temp","r")
    temp = int(f.read())
    return int(temp/1000)

def get_wlan_ip():
    f = os.popen("nmcli dev show wlan0 | grep IP4.ADDRESS",'r')
    ip = f.read()
    ip = ip.split(" ")[-1].strip()[:-3] 
    return ip

def get_eth_ip():
    f = os.popen("nmcli dev show eth0 | grep IP4.ADDRESS",'r')
    ip = f.read()
    ip = ip.split(" ")[-1].strip()[:-3] 
    return ip

font = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',24)
font_20 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',20)

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
    while True:
        image = black_image(240,240)
        
        cpu_temp = get_cpu_temp()
        gpu_temp = get_gpu_temp()
        wlan_ip = get_wlan_ip()
        eth_ip = get_eth_ip()
        time_str = time.asctime()

        image = draw_rotated_text(image, "CPU温度: ", (10,10), 0, font, fill=(255,255,255))
        image = draw_rotated_text(image, str(cpu_temp), (120,10), 0, font, fill=(255,0,0))
        
        image = draw_rotated_text(image, "GPU温度: ", (10,50), 0, font, fill=(255,255,255))
        image = draw_rotated_text(image, str(gpu_temp), (120,50), 0, font, fill=(255,0,0))

        image = draw_rotated_text(image, "WiFi IP: "+wlan_ip, (10,90), 0, font_20, fill=(255,255,255))
        image = draw_rotated_text(image, "Eth0 IP: "+eth_ip, (10,130), 0, font_20, fill=(255,255,255))
        
        image = draw_rotated_text(image, time_str, (10,170), 0, font, fill=(255,255,255))

        disp.display(image)
        time.sleep(10)
except:
    traceback.print_exc()
    print("Done.")
