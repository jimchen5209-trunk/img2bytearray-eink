from io import BytesIO
from PIL import Image
import sys

if len(sys.argv) > 1:
    path_to_image = str(sys.argv[1])
    width = int(sys.argv[2])
    height = int(sys.argv[3])

    im = Image.open(path_to_image).convert('1')
    im_resize = im.resize((width,height))

    buf = [0xFF] * (int(width/8) * height)
    pixels = im_resize.load()
    for y in range(height):
        for x in range(width):
            # Set the bits for the column of pixels at the current position.
            if pixels[x, y] == 0:
                buf[int((x + y * width) / 8)] &= ~(0x80 >> (x % 8))
    print(bytes(buf))
else:
    print("please specify the location of image i.e img2bytearray.py /path/to/image width heigh")
