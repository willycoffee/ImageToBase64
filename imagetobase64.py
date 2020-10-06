import os, base64
from PIL import Image

def base64_encode(string: str) -> str:
    return base64.urlsafe_b64encode(string.encode()).decode()

def base64_decode(string: str) -> str:
    return base64.urlsafe_b64decode(string.encode()).decode()

or file in os.listdir("/image"):
    if file.endswith(".png") or file.endswith('.jpg'):
        image_path = file
        img = Image.open(image_path)

        width, height = img.size
        aspect_ratio = height/width
        new_width = 120
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))
        img = img.convert('L')

        pixels = img.getdata()

        chars = ["B","S","#","&","@","$","%","*","!",":","."]
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        base64_image = base64_encode(ascii_image)
        print(file)
        print(base64_image)
