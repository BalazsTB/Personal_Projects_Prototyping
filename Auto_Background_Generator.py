from PIL import Image
import random

width = 20
height = 10
image_size = (width, height)
#pixel_sql = [(255,0,0), (0,255,0), (0,0,255)]

def generate_random_colours_pixel_by_pixel(image_size:list) -> list:

    number_of_pixels = image_size[0]* image_size[1]

    list_of_all_pixels = []
    pixel_rgb_values = []

    for x in range(number_of_pixels):
        red_val = random.randint(0, 255)
        green_val = random.randint(0, 255)
        blue_val = random.randint(0, 255)

        pixel_rgb_values = [red_val, green_val, blue_val]

        list_of_all_pixels.append(tuple(pixel_rgb_values))

    return list_of_all_pixels

img  = Image.new( mode = "RGB", size = image_size )

pixel_sql = generate_random_colours_pixel_by_pixel(image_size)

img.putdata(pixel_sql)
img.show()

