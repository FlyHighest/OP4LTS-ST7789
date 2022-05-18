from PIL import Image, ImageFont, ImageDraw 

def open_image(path):
    return Image.open(path)

def resize_with_limits(image,WIDTH=240,HEIGHT=240):
    w,h=image.size
    if w>h:
        image = image.resize((WIDTH, int(h/ (w/WIDTH) ) ))
    else:
        image = image.resize((int(w/(h/HEIGHT)),HEIGHT))
    return image 


def default_fonts():
    font_English = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf')
    font_Chinese = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc')
    return font_English,font_Chinese

def expand2square(pil_img, background_color=(0,0,0)):
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

def black_image(width,height):
    return Image.new('RGB', (width, height)) 

def draw_rotated_text(image, text, position, angle, font, fill=(255,255,255)):
    #print position
    position = position[0], position[1]
    # Get rendered font width and height.
    draw = ImageDraw.Draw(image)
    width, height = draw.textsize(text, font=font)
    # Create a new image with transparent background to store the text.
    textimage = Image.new('RGBA', (width, height), (0,0,0,0))
    # Render the text.
    textdraw = ImageDraw.Draw(textimage)
    textdraw.text((0,0), text, font=font, fill=fill)
    # Rotate the text image.
    rotated = textimage.rotate(angle, expand=1)
    # Paste the text into the image, using it as a mask for transparency.
    image.paste(rotated, position, rotated)
    return image 
