import sys
from PIL import Image

container_image = Image.open("container.bmp")
hidden_image = Image.open("hidden.bmp")
result_image = Image.new("RGB", container_image.size)


for x in range(container_image.width):
    for y in range(container_image.height):
        c_pixel = container_image.getpixel((x, y))
        h_pixel = hidden_image.getpixel((x, y))
        new_pixel = tuple((c & 0xF0) | (h >> 4) for c, h in zip(c_pixel, h_pixel))
        result_image.putpixel((x, y), new_pixel)


result_image.save("result.bmp", "BMP")