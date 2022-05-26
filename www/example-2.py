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
    
    draw.line(((30, 200), (130, 100), (80, 50)), fill=(255, 255, 0))
    draw.line(((80, 200), (180, 100), (130, 50)), fill=(255, 255, 0), width=10)
    draw.polygon(((200, 200), (300, 100), (250, 50)), fill=(255, 255, 0), outline=(0, 0, 0))
    draw.point(((350, 200), (450, 100), (400, 50)), fill=(255, 255, 0))

    send_png(img)