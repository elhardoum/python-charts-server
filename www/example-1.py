#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
from io import BytesIO
from sys import stdout

def send_png(img):
    imbytes = BytesIO()
    img.save(imbytes, format='PNG')
    contents = imbytes.getvalue().strip()

    stdout.write('Content-type: image/png\r\n\r\n')
    stdout.buffer.write(contents)

if __name__ == '__main__':
    img = Image.new('RGBA', (600, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
    draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
    draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

    send_png(img)